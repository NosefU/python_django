from django.db import models


class Advertisement(models.Model):
    title = models.CharField(max_length=100, db_index=True, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.FloatField(default=0, verbose_name='Цена')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    modified = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    expiration_date = models.DateTimeField(default=None, null=True, verbose_name='Дата окончания публикации')
    views_count = models.IntegerField(default=0, verbose_name='Количество просмотров')
    author = models.ForeignKey('User', default=None, null=True, verbose_name='Автор',
                               on_delete=models.CASCADE, related_name='advertisements')
    category = models.ForeignKey('AdvertisementCategory', default=None, null=True, verbose_name='Категория',
                                 on_delete=models.CASCADE, related_name='advertisements')
    status = models.ForeignKey('AdvertisementStatus', default=None, null=True, verbose_name='Статус',
                               on_delete=models.CASCADE, related_name='advertisements')


class User(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Имя')
    email = models.EmailField(verbose_name='email')
    phone = models.CharField(max_length=30, verbose_name='Телефон')

    def __str__(self):
        return self.name


class AdvertisementCategory(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Наименование')

    def __str__(self):
        return self.name


class AdvertisementStatus(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Наименование')

    def __str__(self):
        return self.name
