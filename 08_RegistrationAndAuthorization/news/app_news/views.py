from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView

from app_news.forms import CommentForm, ArticleForm
from app_news.models import Article, Comment, ArticleTag


class ArticleList(ListView):
    model = Article
    context_object_name = 'article_list'
    queryset = Article.objects.filter(active=True)[:20]


class UnpublishedArticleList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = "app_news.can_publish_article"
    model = Article
    context_object_name = 'article_list'
    queryset = Article.objects.filter(active=False)[:20]


class ArticleDetail(View):
    def get(self, request, article_id):
        article = Article.objects.get(id=article_id)
        if not article.active:
            if not request.user.has_perm('app_news.can_publish_article') and not article.author == request.user:
                raise PermissionDenied()
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


class AddArticle(LoginRequiredMixin, View):
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


class EditArticle(LoginRequiredMixin, View):
    def get(self, request, article_id):
        article = Article.objects.get(id=article_id)
        article_form = ArticleForm(
            initial={'str_tag': getattr(article.tag, 'name', '')},
            instance=article)
        context = {'article_form': article_form, 'title': 'Изменить новость'}
        return render(request, 'app_news/article_edit.html', context=context)

    def post(self, request, article_id):
        article = Article.objects.get(id=article_id)
        article_form = ArticleForm(request.POST, request.FILES, instance=article)
        if not article_form.is_valid():
            context = {'article_form': article_form, 'title': 'Изменить новость'}
            return render(request, 'app_news/article_edit.html', context=context)

        article.tag, _ = ArticleTag.objects.get_or_create(name=article_form.cleaned_data['str_tag'])
        article.save()
        return HttpResponseRedirect(f'/article/{article.id}')


class PublishArticle(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = "app_news.can_publish_article"

    def get(self, request, article_id):
        article = Article.objects.get(id=article_id)
        article.active = True
        article.save()
        return redirect(request.META.get('HTTP_REFERER', ''))
