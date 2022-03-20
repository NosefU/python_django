from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View, generic

from app_blog.forms import BlogRecordForm
from app_blog.models import BlogRecord


class EditBlogRecord(LoginRequiredMixin, View):
    def get(self, request, record_id):
        record = BlogRecord.objects.get(id=record_id)
        images = BlogRecord.image.all()
        init_form_data = {
            'title': record.title,
            'body': record.body,
            'images': images
        }
        record_form = BlogRecordForm(
            initial={'str_tag': getattr(article.tag, 'name', '')})
        context = {'article_form': article_form, 'title': 'Изменить новость'}
        return render(request, 'app_news/article_edit.html', context=context)


class BlogRecordListView(generic.ListView):
    model = BlogRecord


    # def get(self, request, record_id):
    #     record = BlogRecord.objects.get(id=record_id)
    #     images = record.images.all()
    #     return HttpResponse(str(record) + str(images))
