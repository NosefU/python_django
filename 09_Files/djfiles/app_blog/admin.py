from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from app_blog.models import BlogRecord, BlogImage


# @admin.register(BlogRecord)
# class BlogRecordAdmin(admin.ModelAdmin):
#     pass


@admin.register(BlogImage)
class BlogImageAdmin(admin.ModelAdmin):
    pass


class BlogRecordExtAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'


admin.site.register(BlogRecord, BlogRecordExtAdmin)
