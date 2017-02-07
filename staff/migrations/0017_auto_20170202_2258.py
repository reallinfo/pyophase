# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-02 21:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0003_auto_20170202_2258'),
        ('staff', '0016_auto_20170201_1604'),
        ('students', '0003_auto_20150913_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='tutor_for',
            field=models.ForeignKey(blank=True, help_text='Erstsemester welches Studiengangs möchtest du als Tutor betreuen?', null=True, on_delete=django.db.models.deletion.SET_NULL, to='ophasebase.OphaseCategory', verbose_name='Tutor für'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='group_categories_enabled',
            field=models.ManyToManyField(to='ophasebase.OphaseCategory', verbose_name='Freigeschaltete Kleingruppenkategorien'),
        ),
        migrations.AlterField(
            model_name='stafffiltergroup',
            name='tutor_for',
            field=models.ManyToManyField(blank=True, help_text='Welche Tutorengruppen sollen einbezogen werden?', to='ophasebase.OphaseCategory', verbose_name='Tutor für'),
        ),
        migrations.AlterField(
            model_name='tutorgroup',
            name='group_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ophasebase.OphaseCategory', verbose_name='Gruppenkategorie'),
        ),
        migrations.DeleteModel(
            name='GroupCategory',
        ),
    ]
