# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-21 04:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GameAdmin', '0003_auto_20171021_1030'),
    ]

    operations = [
        migrations.CreateModel(
            name='Judge',
            fields=[
                ('ID', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('JudgeAccount', models.CharField(max_length=20)),
                ('Password', models.CharField(max_length=20)),
                ('Name', models.CharField(max_length=20)),
                ('PhoneNum', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('MatchID', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('Group', models.CharField(max_length=20)),
                ('Event', models.CharField(max_length=20)),
                ('ChiefID', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('PlayerID', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('ID', models.CharField(max_length=20)),
                ('Name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('Group', models.CharField(max_length=20)),
                ('CultrueScore', models.IntegerField()),
                ('TeamName', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('Name', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('TeamAccount', models.CharField(max_length=20)),
                ('Password', models.CharField(max_length=20)),
                ('File', models.FileField(upload_to='uploads/')),
            ],
        ),
        migrations.CreateModel(
            name='TeamCoach',
            fields=[
                ('ID', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=20)),
                ('PhoneNum', models.CharField(max_length=20)),
                ('Gender', models.CharField(max_length=1)),
                ('TeamName', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='TeamLeader',
            fields=[
                ('ID', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=20)),
                ('PhoneNum', models.CharField(max_length=20)),
                ('TeamName', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='TeamMedic',
            fields=[
                ('ID', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=20)),
                ('PhoneNum', models.CharField(max_length=20)),
                ('TeamName', models.CharField(max_length=20)),
            ],
        ),
    ]
