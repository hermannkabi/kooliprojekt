# Generated by Django 4.2.1 on 2023-05-23 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_alter_question_constant'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='unit',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
