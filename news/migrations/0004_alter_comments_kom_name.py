# Generated by Django 4.1.5 on 2023-01-09 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_comments_delete_articles_alter_texts_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='kom_name',
            field=models.CharField(max_length=20, verbose_name='Имя комментатора'),
        ),
    ]