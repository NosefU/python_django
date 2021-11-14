from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from app_news.forms import CommentForm, ArticleForm
from app_news.models import Article, Comment


class ArticleList(ListView):
    model = Article
    context_object_name = 'article_list'
    queryset = Article.objects.all()[:20]


class ArticleDetail(View):
    def get(self, request, article_id):
        article = Article.objects.get(id=article_id)
        comment_form = CommentForm()
        comments = article.comments.all()
        context = {
            'article': article,
            'comment_form': comment_form,
            'comments': comments
        }
        return render(request, 'app_news/article_detail.html', context=context)

    def post(self, request, article_id):
        comment_form = CommentForm(request.POST)
        if not comment_form.is_valid():
            return HttpResponseBadRequest(f'Некорректный комментарий: {comment_form.errors}')

        article = Article.objects.get(id=article_id)
        comment = Comment.objects.create(**comment_form.cleaned_data, article=article)
        return HttpResponseRedirect(f'{request.path_info}#comment_{comment.id}')


class AddArticle(View):
    def get(self, request):
        article_form = ArticleForm()
        return render(request, 'app_news/article_edit.html', context={'article_form': article_form})

    def post(self, request):
        article_form = ArticleForm(request.POST, request.FILES)
        if not article_form.is_valid():
            return render(request, 'app_news/article_edit.html', context={'article_form': article_form})

        article = Article.objects.create(**article_form.cleaned_data)
        return HttpResponseRedirect(f'/article/{article.id}')
