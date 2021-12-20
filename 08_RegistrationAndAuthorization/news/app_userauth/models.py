from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone = models.CharField(max_length=20, blank=True, verbose_name='Телефон')
    city = models.CharField(max_length=50, blank=True, verbose_name='Город')
    is_verified = models.BooleanField(default=False, verbose_name='Подтвержденный пользователь')

    # TODO количество опубликованных новостей: стоит ли вычисляемое значение делать полем?
    #  при увеличении нагрузки на бд согласен, есть смысл хранить это значение как отдельное поле
    #  (при условии частого его использования) и вычислять при одобрении либо удалении новости.
    #  но на данном этапе, как мне кажется, гораздо более явной будет реализация property
    @property
    def published_articles_number(self):
        return self.user.articles.filter(active=True).count()
