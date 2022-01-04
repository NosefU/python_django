from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import truncatechars
from django.conf import settings

from .utils import GetUUIDName


class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    subtitle = models.CharField(max_length=200, blank=True, default='', verbose_name='Подзаголовок')
    image = models.ImageField(upload_to=GetUUIDName('article_images'), verbose_name='Картинка')
    body = models.TextField(verbose_name='Текст новости')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    modified = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    active = models.BooleanField(default=False, verbose_name='Опубликовано')
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='articles', verbose_name='Автор')
    moderator = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,
                             related_name='accepted_articles', verbose_name='Модератор')

    @property
    def active_text(self):
        return 'Опубликовано' if self.active else 'Не опубликовано'

    active_text.fget.short_description = 'Статус публикации'

    class Meta:
        ordering = ['-created', ]
        permissions = (('can_publish_article', 'Может публиковать новости'),)

    def __str__(self):
        return f'{self.title} | {self.created.strftime("%Y-%m-%d %H:%M:%S")} | {self.active_text}'


class Comment(models.Model):
    username = models.CharField(max_length=100, verbose_name='Имя пользователя')
    body = models.TextField(max_length=600, verbose_name='Комментарий')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    article = models.ForeignKey('Article', on_delete=models.CASCADE, related_name='comments', verbose_name='Новость')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,
                             related_name='comments', verbose_name='Пользователь')

    @property
    def short_body(self):
        return truncatechars(self.body, 15)

    class Meta:
        ordering = ['-created', ]

    def __str__(self):
        return f'{self.username} | {self.short_body}'
