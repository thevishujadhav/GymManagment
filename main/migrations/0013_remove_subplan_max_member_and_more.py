# Generated by Django 5.0.1 on 2024-02-04 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_remove_subscriber_user_subplan_highlight_status_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subplan',
            name='max_member',
        ),
        migrations.RemoveField(
            model_name='subplan',
            name='validity_days',
        ),
    ]
