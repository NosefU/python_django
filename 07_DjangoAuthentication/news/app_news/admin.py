from django.contrib import admin
from app_news.models import Article, Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Comment._meta.get_fields()]
    list_filter = ['username']
    actions = ['delete_as_admin']

    def delete_as_admin(self, request, queryset):
        queryset.update(body='Удалено администратором')

    delete_as_admin.short_description = 'Зацензурить'


class CommentInline(admin.TabularInline):
    model = Comment


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'subtitle', 'image', 'created', 'modified', 'active']
    list_filter = ['active']
    inlines = [CommentInline, ]
    actions = ['mark_as_active', 'mark_as_inactive']

    def mark_as_active(self, request, queryset):
        queryset.update(active=True)

    def mark_as_inactive(self, request, queryset):
        queryset.update(active=False)

    mark_as_active.short_description = 'Опубликовать'
    mark_as_inactive.short_description = 'Снять с публикации'




