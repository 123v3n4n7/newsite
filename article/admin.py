from django.contrib import admin
from .models import Article, Comments

class ArticleComment(admin.TabularInline):
	model = Comments
	extra = 2

class AdminArticle(admin.ModelAdmin):
	fields = ['title', 'text']
	inlines = [ArticleComment,]

admin.site.register(Article, AdminArticle)

# Register your models here.
