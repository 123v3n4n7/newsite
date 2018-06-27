from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    title = models.CharField(max_length=100, blank=False)
    text = models.TextField(blank=False)
    date = models.DateTimeField()
    likes = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta():
        db_table = "article"


class Comments(models.Model):
    article_comment = models.ForeignKey(Article, on_delete=models.CASCADE)
    comment_text = models.TextField()
    author = models.CharField(max_length=100, null=True)
    date = models.DateTimeField(null=True)
    class Meta():
        db_table = "comments"
