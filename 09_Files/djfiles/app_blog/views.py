from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View, generic

from app_blog.forms import BlogRecordForm
from app_blog.models import BlogRecord, BlogImage


class AddBlogRecord(LoginRequiredMixin, View):
    def get(self, request):
        record_form = BlogRecordForm()
        context = {'form': record_form, 'title': 'Создать пост'}
        return render(request, 'app_blog/blogrecord_edit.html', context=context)

    def post(self, request):
        record_form = BlogRecordForm(request.POST, request.FILES)
        if not record_form.is_valid():
            context = {'form': record_form, 'title': 'Создать пост'}
            return render(request, 'app_blog/blogrecord_edit.html', context=context)

        record = BlogRecord(
            title=record_form.cleaned_data['title'],
            body=record_form.cleaned_data['body'],
            author=request.user
        )
        record.save()
        for f in record_form.files.getlist('images'):
            image = BlogImage(
                image=f,
                record=record
            )
            image.save()
        return HttpResponseRedirect(f'/record/{record.id}')


class BlogRecordListView(generic.ListView):
    model = BlogRecord


class BlogRecordDetailView(generic.DetailView):
    model = BlogRecord
