# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-06 13:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0006_auto_20160530_0117'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupcategory',
            name='max_threshold',
            field=models.IntegerField(null=True, verbose_name='Harte Maximalanzahl'),
        ),
        migrations.AddField(
            model_name='groupcategory',
            name='warning_threshold',
            field=models.IntegerField(null=True, verbose_name='Anzahl bis Warnung'),
        ),
    ]
