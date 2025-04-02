# Generated by Django 5.1.3 on 2024-12-04 19:13

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_remove_advantage_likes_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='advantage',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='advantage',
            name='users_who_liked',
            field=models.ManyToManyField(blank=True, related_name='liked_advantages', to=settings.AUTH_USER_MODEL),
        ),
    ]
