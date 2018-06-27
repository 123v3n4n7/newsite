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


def ArticleShow(request, article_id):
    form = CommentsForm()
    args = {}
    args.update(csrf(request))
    args['article'] = Article.objects.get(id=article_id)
    args['comments'] = Comments.objects.filter(article_comment=article_id)
    args['form'] = form
    args['username'] = auth.get_user(request).username
    args['author'] = request.user
    template_name = 'article/article.html'
    return render(request, template_name, args)


def ArticlesShow(request):
    args = {'articles': Article.objects.all().order_by('-date'), 'username': auth.get_user(request).username}
    template_name = 'article/articels.html'
    return render(request, template_name, args)


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
    if request.method == "POST" and ('pause' not in request.session) and request.user.is_authenticated:
        form = CommentsForm(request.POST)
        if form.is_valid():
            form.instance.article_comment = Article.objects.get(id=article_id)

            form.save()
            request.session.set_expiry(1)
            request.session['pause'] = True
    return redirect('/article/{}'.format(article_id))

# Create your views here.
