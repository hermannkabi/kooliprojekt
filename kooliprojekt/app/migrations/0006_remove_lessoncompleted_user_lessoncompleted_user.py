# Generated by Django 4.2.1 on 2023-05-19 08:18

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0005_course_kasutajad'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lessoncompleted',
            name='user',
        ),
        migrations.AddField(
            model_name='lessoncompleted',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
