# Generated by Django 5.1.3 on 2024-11-21 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_rename_articles_advantage'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Advantage',
            new_name='Articles',
        ),
    ]
