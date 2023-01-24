from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from app_blog.models import BlogRecord


class BlogRecordExtAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'


admin.site.register(BlogRecord, BlogRecordExtAdmin)
