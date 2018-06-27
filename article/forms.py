from django import forms
from django.contrib.auth.models import User
from .models import Article, Comments


class ArticleForm(forms.ModelForm):
    class Meta():
        model = Article
        fields = ['title', 'text', 'date', 'likes', 'author']


class CommentsForm(forms.ModelForm):
    class Meta():
        model = Comments
        fields = ['comment_text', 'date', 'author']
