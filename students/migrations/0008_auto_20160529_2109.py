# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-29 19:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0007_auto_20160228_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='E-Mail-Adresse'),
        ),
    ]