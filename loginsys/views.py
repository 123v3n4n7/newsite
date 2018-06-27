from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, User
from django.template.context_processors import csrf
from .forms import UserRegistrationForm, UserForm, ProfileForm
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, permissions
from loginsys.serializers import UserSerializer, UserAuthenticate, AuthCustomTokenSerializer
from rest_framework.authtoken.models import Token
from . import serializers
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser
from rest_framework.renderers import JSONRenderer
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib import messages


def login2(request):
    args = {}
    template_name = 'loginsys/login.html'
    args.update(csrf(request))
    if request.POST:

        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            args['login_error'] = 'Пользователь не найден'
            return render(request, template_name, args)
    else:
        return render(request, template_name, args)


def logout(request):
    auth.logout(request)
    return redirect('/')


def registration(request):
    template_name = 'loginsys/registration.html'
    args = {}
    args["form"] = UserRegistrationForm()
    args.update(csrf(request))
    if args["form"].is_valid():
        newuser_form = UserRegistrationForm(request.POST)
        newuser = User.objects.create_user(username=newuser_form.cleaned_data['username'],
                                           password=newuser_form.cleaned_data['password1'],
                                           email=newuser_form.cleaned_data['email'])
        login(request, newuser)
        return redirect('/')


    else:
        args['form'] = UserRegistrationForm()
    return render(request, template_name, args)


class UserCreate(APIView):
    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                token = Token.objects.create(user=user)
                json = serializer.data
                json['token'] = token.key
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RegisterUser(generics.CreateAPIView):
    serializer_class = serializers.RegisterSerializer
    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.create_user(username, email, password)

        user.save()
        token = Token.objects.create(user=user)
        return Response({'detail': 'User create'})


class ObtainAuthToken(APIView):
    serializer_class = serializers.AuthCustomTokenSerializer

    def post(self, request, format='json'):
        serializer = AuthCustomTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        token = Token.objects.get_or_create(user=user)

        return Response({'detail': 'User login'})


@login_required
@transaction.atomic
def ProfileListView(request):
    if request.method == "POST":
        user_form = UserForm(request.POST, instance=request.user)
        profile = Profile.objects.get(user=request.user)
        profile_form = ProfileForm(request.POST, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            messages.success(request, ("success updated!"))
            return redirect('/')
        else:
            messages.error(request, ('error'))
    else:
        user_form = UserForm(instance=request.user)
        profile = Profile.objects.get(user=request.user)
        profile_form = ProfileForm(instance=profile)
    return render(request, 'loginsys/profile.html', {'user_form': user_form, 'profile_form': profile_form})

# Create your views here.
