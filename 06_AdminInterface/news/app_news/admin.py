from django.contrib import admin
from app_news.models import Article, Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Comment._meta.get_fields()]
    list_filter = ['username']


class CommentInline(admin.TabularInline):
    model = Comment


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'subtitle', 'image', 'created', 'modified', 'active']
    list_filter = ['active']
    inlines = [CommentInline, ]



