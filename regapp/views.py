from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.contrib import auth

def RegView(request):
	template_name = 'main.html'
	context = {}
	context['username'] = auth.get_user(request).username
	return render(request, template_name, context)

# Create your views here.
