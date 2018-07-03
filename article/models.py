from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Article(models.Model):
    title = models.CharField(max_length=100, blank=False)
    text = models.TextField(blank=False)
    date = models.DateTimeField(auto_now_add=True,null=True)
    likes = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def get_absolute_url(self):
        url = reverse("article:article", kwargs={"article_id": self.id})
        return url
    class Meta():
        db_table = "article"


class Comments(models.Model):
    article_comment = models.ForeignKey(Article, on_delete=models.CASCADE)
    comment_text = models.TextField()
    date = models.DateTimeField(auto_now_add=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta():
        db_table = "comments"


