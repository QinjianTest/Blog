# Generated by Django 4.1.3 on 2022-12-05 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogV1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='tag',
            field=models.TextField(blank=True, null=True, verbose_name='文章标签'),
        ),
    ]