from django.contrib import admin
from app_news.models import Article, Comment, ArticleTag
from app_userauth.models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = [field.name for field in UserProfile._meta.get_fields()]


@admin.register(ArticleTag)
class TagAdmin(admin.ModelAdmin):
    pass


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
    list_filter = ['active', 'tag']
    inlines = [CommentInline, ]
    actions = ['mark_as_active', 'mark_as_inactive']

    def mark_as_active(self, request, queryset):
        queryset.update(active=True, moderator=request.user)

    def mark_as_inactive(self, request, queryset):
        queryset.update(active=False, moderator=request.user)

    mark_as_active.short_description = 'Опубликовать'
    mark_as_inactive.short_description = 'Снять с публикации'




