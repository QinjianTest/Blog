# Generated by Django 4.1.3 on 2022-12-05 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogV1', '0005_alter_articles_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='tag',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='标签'),
        ),
    ]
