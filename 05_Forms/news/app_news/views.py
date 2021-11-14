from django.shortcuts import render
from django.views.generic import ListView, DetailView
from app_news.models import Article


class ArticleList(ListView):
    model = Article
    context_object_name = 'article_list'
    queryset = Article.objects.all()[:20]


class ArticleDetail(DetailView):
    model = Article
    context_object_name = 'article'
