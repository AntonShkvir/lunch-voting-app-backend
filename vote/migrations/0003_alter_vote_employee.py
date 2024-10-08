# Generated by Django 5.1.1 on 2024-09-28 01:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_alter_employee_department'),
        ('vote', '0002_alter_vote_unique_together_vote_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.employee'),
        ),
    ]
