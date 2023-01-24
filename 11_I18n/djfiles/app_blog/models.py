from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class BlogRecord(models.Model):
    title = models.CharField(max_length=200, blank=True, verbose_name=_('Заголовок'))
    body = models.TextField(verbose_name=_('Текст записи'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('Время создания'))
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='records', verbose_name=_('Автор'))
    cover = models.ImageField(upload_to='blog_images', blank=True, verbose_name=_('Обложка'))

    class Meta:
        ordering = ['-created', ]
        verbose_name_plural = _('blog_records')
        verbose_name = _('blog_record')

    def __repr__(self):
        return f"BlogRecord {self.id}: user {self.author.id}, {self.title}"

    def __str__(self):
        return self.__repr__()
