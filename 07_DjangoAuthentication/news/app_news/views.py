from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from app_news.forms import CommentForm, ArticleForm, NewsAuthForm
from app_news.models import Article, Comment


class NewsLoginView(LoginView):
    template_name = 'app_news/login.html'
    authentication_form = NewsAuthForm


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
            article = Article.objects.get(id=article_id)
            comments = article.comments.all()
            context = {
                'article': article,
                'comment_form': comment_form,
                'comments': comments
            }
            return render(request, 'app_news/article_detail.html', context=context)

        article = Article.objects.get(id=article_id)
        comment = Comment.objects.create(**comment_form.cleaned_data, article=article)
        return HttpResponseRedirect(f'{request.path_info}#comment_{comment.id}')


class AddArticle(View):
    def get(self, request):
        article_form = ArticleForm()
        context = {'article_form': article_form, 'title': 'Предложите свою новость'}
        return render(request, 'app_news/article_edit.html', context=context)

    def post(self, request):
        article_form = ArticleForm(request.POST, request.FILES)
        if not article_form.is_valid():
            context = {'article_form': article_form, 'title': 'Предложите свою новость'}
            return render(request, 'app_news/article_edit.html', context=context)

        article = Article.objects.create(**article_form.cleaned_data)
        return HttpResponseRedirect(f'/article/{article.id}')


class EditArticle(View):
    def get(self, request, article_id):
        article = Article.objects.get(id=article_id)
        article_form = ArticleForm(instance=article)
        context = {'article_form': article_form, 'title': 'Изменить новость'}
        return render(request, 'app_news/article_edit.html', context=context)

    def post(self, request, article_id):
        article = Article.objects.get(id=article_id)
        article_form = ArticleForm(request.POST, request.FILES, instance=article)
        if not article_form.is_valid():
            context = {'article_form': article_form, 'title': 'Изменить новость'}
            return render(request, 'app_news/article_edit.html', context=context)

        article.save()
        return HttpResponseRedirect(f'/article/{article.id}')
