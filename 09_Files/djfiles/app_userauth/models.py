from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=50, blank=True, default=str, verbose_name='Имя')
    last_name = models.CharField(max_length=50, blank=True, default=str, verbose_name='Фамилия')
    about = models.TextField(max_length=200, blank=True, default=str, verbose_name='О себе')
