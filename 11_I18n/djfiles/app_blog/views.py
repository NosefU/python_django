import csv
from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View, generic
from django.utils.translation import gettext as _

from app_blog.forms import BlogRecordForm, BatchBlogRecordForm
from app_blog.models import BlogRecord


class AddBlogRecord(LoginRequiredMixin, View):
    def get(self, request):
        record_form = BlogRecordForm()
        context = {'form': record_form, 'title': _('Create post')}
        return render(request, 'app_blog/blogrecord_edit.html', context=context)

    def post(self, request):
        record_form = BlogRecordForm(request.POST, request.FILES)
        if not record_form.is_valid():
            context = {'form': record_form, 'title': _('Create post')}
            return render(request, 'app_blog/blogrecord_edit.html', context=context)

        record = BlogRecord(
            title=record_form.cleaned_data['title'],
            body=record_form.cleaned_data['body'],
            cover=record_form.cleaned_data['cover'],
            author=request.user
        )
        record.save()
        return HttpResponseRedirect(f'/record/{record.id}')


class BlogRecordListView(generic.ListView):
    model = BlogRecord


class BlogRecordDetailView(generic.DetailView):
    model = BlogRecord


class BatchAddBlogRecord(LoginRequiredMixin, View):
    def get(self, request):
        records_form = BatchBlogRecordForm()
        context = {'form': records_form}
        return render(request, 'app_blog/blogrecord_batch_add.html', context=context)

    def post(self, request):
        records_form = BatchBlogRecordForm(request.POST, request.FILES)
        if not records_form.is_valid():
            context = {'form': records_form}
            return render(request, 'app_blog/blogrecord_batch_add.html', context=context)

        try:
            decoded_file = records_form.files['posts_file'].read().decode('utf-8').splitlines()
            reader = csv.DictReader(decoded_file, delimiter=';')
        except (csv.Error, UnicodeDecodeError):
            records_form.add_error('posts_file', 'Invalid file format')
            context = {'form': records_form}
            return render(request, 'app_blog/blogrecord_batch_add.html', context=context)

        for row in reader:
            record = BlogRecord(
                body=row['body'],
                title=row.get('title'),
                cover=row.get('cover'),
                author=request.user
            )
            record.save()
            if row.get('date'):
                try:
                    record.created = datetime.strptime(row['date'], "%Y-%m-%d %H:%M:%S")
                except ValueError:
                    records_form.add_error('posts_file', f'Invalid datetime format in row "{row["date"]};{row["body"]}"')
                    context = {'form': records_form}
                    return render(request, 'app_blog/blogrecord_batch_add.html', context=context)
                record.save()
        return HttpResponseRedirect('/')
