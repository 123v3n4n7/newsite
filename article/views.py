from django.shortcuts import render, redirect
from django.http import Http404
from django.urls import reverse
from django.views import generic
from .models import Article, Comments
from django.template.context_processors import csrf
from django.core.exceptions import ObjectDoesNotExist
from .forms import CommentsForm, ArticleForm
from django.contrib import auth
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework import status, generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers

def ArticleShow(request, article_id):
    form = CommentsForm()
    args = {}
    args.update(csrf(request))
    args['article'] = Article.objects.get(id=article_id)
    args['comments'] = Comments.objects.filter(article_comment=article_id)
    args['form'] = form
    args['username'] = auth.get_user(request).username
    template_name = 'article/article.html'
    return render(request, template_name, args)


def addArticle(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        form.instance.author = User.objects.get(username=request.user.username)
        form.instance.likes = 0
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ArticleForm()
    return render(request, 'article/newarticle.html', {"form": form, "username": auth.get_user(request).username})


def ArticlesShow(request):
    template_name = 'article/articels.html'
    article_list = Article.objects.all().order_by('-date')
    paginator = Paginator(article_list, 5)
    page = request.GET.get('page')
    articles = paginator.get_page(page)
    return render(request, template_name, {'articles': articles, 'username': auth.get_user(request).username})


def ArticleAddLike(request, article_id):
    try:
        if article_id in request.COOKIES:
            redirect('/')
        else:
            article = Article.objects.get(id=article_id)
            article.likes += 1
            article.save()
            response = redirect('/')
            response.set_cookie(article_id)
            return response
    except ObjectDoesNotExist:
        raise Http404
    return redirect('/')


def AddComment(request, article_id):
    if request.method == "POST" and ('pause' not in request.session):
        form = CommentsForm(request.POST)
        if form.is_valid() and request.user.is_authenticated:
            form.instance.article_comment = Article.objects.get(id=article_id)
            form.instance.author = User.objects.get(username=request.user.username)
            form.save()
            request.session.set_expiry(1)
            request.session['pause'] = True
    return redirect('/article/{}'.format(article_id))

class addArticleSerializers(generics.CreateAPIView):
    serializer_class = serializers.addArticle
    def addArticle(self, request):
        form = ArticleForm()
        form.title = request.POST.get('title')
        form.text = request.POST.get('text')
        form.instance.author = request.user.username
        form.instance.likes = 0
        if form.is_valid():
            form.save()
            return redirect({'article': 'articles'})
        else:
            form = ArticleForm()
        return Response({'article': 'articles'})

# Create your views here.
