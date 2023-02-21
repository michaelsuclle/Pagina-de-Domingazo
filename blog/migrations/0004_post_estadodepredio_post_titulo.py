# Generated by Django 4.1.5 on 2023-02-07 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_post_estadodepredio'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='estadodepredio',
            field=models.IntegerField(choices=[(1, 'En construccion'), (2, 'En planos'), (3, 'Departamento'), (4, 'Casa'), (5, 'Terreno')], default=1),
        ),
        migrations.AddField(
            model_name='post',
            name='titulo',
            field=models.CharField(default='casaaa', max_length=200),
            preserve_default=False,
        ),
    ]
