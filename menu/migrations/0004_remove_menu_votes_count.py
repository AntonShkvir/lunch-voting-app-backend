# Generated by Django 5.1.1 on 2024-09-28 01:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_menu_votes_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='votes_count',
        ),
    ]
