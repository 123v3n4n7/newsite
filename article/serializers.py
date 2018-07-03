from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Article, Comments


class addArticle(serializers.ModelSerializer):
    title = serializers.CharField(max_length=100)
    text = serializers.CharField(max_length=1000)
    class Meta():
        model = Article
        fields=['title', 'text']

class addComment(serializers.ModelSerializer):
    comment_text = serializers.CharField(max_length=500)
