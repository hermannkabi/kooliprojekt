# Generated by Django 4.2.1 on 2023-05-19 07:40

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0004_lesson_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='kasutajad',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
