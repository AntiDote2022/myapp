# Generated by Django 4.1.5 on 2023-01-09 07:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_alter_comments_numbers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='numbers',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.texts', verbose_name='ид новости'),
        ),
    ]
