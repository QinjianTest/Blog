# Generated by Django 4.1.3 on 2022-12-06 04:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BlogV1', '0008_articles_excellent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articles',
            name='excellent',
        ),
    ]
