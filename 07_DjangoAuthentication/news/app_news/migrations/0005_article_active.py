# Generated by Django 2.2 on 2021-11-21 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0004_auto_20211115_1811'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='active',
            field=models.BooleanField(default=False, verbose_name='Опубликовано'),
        ),
    ]
