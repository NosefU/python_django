from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    subtitle = models.CharField(max_length=200, default='', verbose_name='Подзаголовок')
    image = models.ImageField(upload_to='article_images', verbose_name='Картинка')
    body = models.TextField(verbose_name='Текст новости')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    modified = models.DateTimeField(auto_now=True, verbose_name='Время изменения')

    class Meta:
        ordering = ['-created', ]

    def __str__(self):
        return f'{self.title} | {self.created}'


class Comment(models.Model):
    username = models.CharField(max_length=100, verbose_name='Имя пользователя')
    body = models.TextField(max_length=600, verbose_name='Комментарий')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    article = models.ForeignKey('Article', on_delete=models.CASCADE, related_name='comments', verbose_name='Новость')

    class Meta:
        ordering = ['-created', ]

    def __str__(self):
        return f'{self.username} | {self.body}'
