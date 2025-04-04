# Generated by Django 5.1.3 on 2024-11-22 16:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_comments'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='advantage',
            options={'verbose_name': 'Достижение', 'verbose_name_plural': 'Статьи'},
        ),
        migrations.AddField(
            model_name='advantage',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Владелец статьи'),
        ),
        migrations.AlterField(
            model_name='advantage',
            name='create_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
