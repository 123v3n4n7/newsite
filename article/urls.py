from django.urls import path
from django.conf.urls import url
from . import views
from rest_framework.authtoken import views as vm

app_name = 'article'

urlpatterns = [
    url(r'^article/(?P<article_id>[0-9]+)$', views.ArticleShow, name='article'),
    url(r'^$', views.ArticlesShow, name='articles'),
    url(r'^article/like/(?P<article_id>[0-9]+)$', views.ArticleAddLike, name='addlike'),
    url(r'^article/addcomment/(?P<article_id>[0-9]+)$', views.AddComment, name='addcomment'),
    url(r'^article/addarticle/$', views.addArticle, name='addarticle'),
    url(r'^article/addarticleSerializer/$', views.addArticleSerializers.as_view(), name='addarticle'),
]
