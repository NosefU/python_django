from django.contrib.auth.models import User
from django.db import models

from app_userauth.utils import GetPostDirectory


class BlogRecord(models.Model):
    title = models.CharField(max_length=200, blank=True, verbose_name='Заголовок')
    body = models.TextField(verbose_name='Текст записи')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='records', verbose_name='Автор')

    class Meta:
        ordering = ['-created', ]

    def __repr__(self):
        return f"BlogRecord {self.id}: user {self.author_id}, {self.title}"

    def __str__(self):
        return self.__repr__()


class BlogImage(models.Model):
    image = models.ImageField(upload_to=GetPostDirectory('blog_images'))
    record = models.ForeignKey(BlogRecord, on_delete=models.CASCADE,
                               related_name='images', verbose_name='Изображение')

    def __repr__(self):
        return f"BlogImage {self.id}: record {self.record.id}, {self.image.name}"

    def __str__(self):
        return self.__repr__()
