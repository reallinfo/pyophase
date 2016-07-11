# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-10 09:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshops', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workshop_submission_enabled', models.BooleanField(default=False, verbose_name='Workshop-Einreichung aktiv')),
            ],
            options={
                'verbose_name': 'Einstellungen',
                'verbose_name_plural': 'Einstellungen',
            },
        ),
    ]