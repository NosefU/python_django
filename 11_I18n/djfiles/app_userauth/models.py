from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

from app_userauth.utils import GetUserDirectory


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', verbose_name=_('Username'))
    first_name = models.CharField(max_length=50, blank=True, default=str, verbose_name=_('First name'))
    last_name = models.CharField(max_length=50, blank=True, default=str, verbose_name=_('Last name'))
    about = models.TextField(max_length=200, blank=True, default=str, verbose_name=_('About'))
    avatar = models.ImageField(upload_to=GetUserDirectory('avatars'),
                               default='avatars/default.svg', verbose_name=_('Avatar'))

    class Meta:
        verbose_name_plural = _('user_profiles')
        verbose_name = _('user_profile')
