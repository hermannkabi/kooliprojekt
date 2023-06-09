# Generated by Django 4.2.1 on 2023-05-26 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_question_unit'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='only_for_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='question',
            name='explanation',
            field=models.TextField(blank=True, default=''),
        ),
    ]
