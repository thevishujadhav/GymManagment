# Generated by Django 5.0.1 on 2024-01-13 17:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_subplanfeature'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subplan',
            name='highlight_status',
        ),
        migrations.RemoveField(
            model_name='subplan',
            name='max_member',
        ),
        migrations.RemoveField(
            model_name='subplan',
            name='validity_days',
        ),
        migrations.RemoveField(
            model_name='subplanfeature',
            name='subplan',
        ),
        migrations.AddField(
            model_name='subplanfeature',
            name='subplan',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.subplan'),
        ),
    ]
