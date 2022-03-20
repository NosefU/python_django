from django.contrib import admin

from app_blog.models import BlogRecord, BlogImage


@admin.register(BlogRecord)
class BlogRecordAdmin(admin.ModelAdmin):
    pass


@admin.register(BlogImage)
class BlogImageAdmin(admin.ModelAdmin):
    pass
