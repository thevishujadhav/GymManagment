# Generated by Django 5.0.1 on 2024-02-05 14:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_subplan_max_member_subplan_validity_days'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AppSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo_img', models.ImageField(upload_to='app_logos/')),
            ],
        ),
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100, null=True)),
                ('pwd', models.CharField(max_length=50, null=True)),
                ('mobile', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('is_active', models.BooleanField(default=False)),
                ('detail', models.TextField()),
                ('img', models.ImageField(upload_to='trainers/')),
                ('salary', models.IntegerField(default=0)),
                ('facebook', models.CharField(max_length=200, null=True)),
                ('twitter', models.CharField(max_length=200, null=True)),
                ('pinterest', models.CharField(max_length=200, null=True)),
                ('youtube', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TrainerNotification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notif_msg', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Notify',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notify_detail', models.TextField()),
                ('read_by_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('read_by_trainer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.trainer')),
            ],
        ),
        migrations.CreateModel(
            name='NotifUserStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('notif', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.notify')),
            ],
            options={
                'verbose_name_plural': 'Notification Status',
            },
        ),
        migrations.CreateModel(
            name='PlanDiscount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_months', models.IntegerField()),
                ('total_discount', models.IntegerField()),
                ('subplan', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.subplan')),
            ],
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(max_length=20)),
                ('address', models.TextField()),
                ('img', models.ImageField(null=True, upload_to='subs/')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.CharField(max_length=50)),
                ('reg_date', models.DateField(auto_now_add=True, null=True)),
                ('plan', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.subplan')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AssignSubscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.trainer')),
            ],
        ),
        migrations.CreateModel(
            name='TrainerAchivement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('detail', models.TextField()),
                ('img', models.ImageField(upload_to='trainers_achivements/')),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.trainer')),
            ],
        ),
        migrations.CreateModel(
            name='TrainerMsg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('trainer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.trainer')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Messages For Trainer',
            },
        ),
        migrations.CreateModel(
            name='NotifTrainerStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.trainer')),
                ('notif', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.trainernotification')),
            ],
            options={
                'verbose_name_plural': 'Trainer Notification Status',
            },
        ),
        migrations.CreateModel(
            name='TrainerSalary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amt', models.IntegerField()),
                ('amt_date', models.DateField()),
                ('remarks', models.TextField(blank=True)),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.trainer')),
            ],
            options={
                'verbose_name_plural': 'Trainer Salary',
            },
        ),
        migrations.CreateModel(
            name='TrainerSubscriberReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_msg', models.TextField()),
                ('report_for_trainer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='report_for_trainer', to='main.trainer')),
                ('report_for_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='report_for_user', to=settings.AUTH_USER_MODEL)),
                ('report_from_trainer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='report_from_trainer', to='main.trainer')),
                ('report_from_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='report_from_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
