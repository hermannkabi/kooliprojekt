# Generated by Django 4.2.1 on 2023-05-21 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_alter_course_kasutajad_alter_lesson_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='type',
            field=models.CharField(default='one', max_length=50),
            preserve_default=False,
        ),
    ]