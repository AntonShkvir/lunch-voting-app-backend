# Generated by Django 5.1.1 on 2024-09-28 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_alter_menu_restaurant_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='votes_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
