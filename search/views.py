from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views import View
from django.http import Http404
from django.db.models import Q
from article.models import Article


class ESearchView(View):

    def get(self, request, *args, **kwargs):
        context = {}
        template_name = 'search/index.html'
        question = request.GET.get('q')
        if question is not None:
            articles = Article.objects.filter(Q(text__icontains=question) | Q(title__icontains=question))

            # формируем строку URL, которая будет содержать последний запрос
            # Это важно для корректной работы пагинации
            context['last_question'] = '?q={}'.format(question)
            page = request.GET.get('page')
            current_page = Paginator(articles, 10)
            try:
                context['articles'] = current_page.page(page)
            except PageNotAnInteger:
                context['articles'] = current_page.page(1)
            except EmptyPage:
                context['articles'] = current_page.page(current_page.num_pages)

        return render(request, template_name, context)