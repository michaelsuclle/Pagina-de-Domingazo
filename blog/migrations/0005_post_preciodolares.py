# Generated by Django 4.1.5 on 2023-02-08 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_estadodepredio_post_titulo'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='preciodolares',
            field=models.IntegerField(default=0),
        ),
    ]