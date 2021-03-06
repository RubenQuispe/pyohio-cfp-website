# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-09 14:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proposals', '0007_auto_20180208_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conferencespeaker',
            name='home_city',
            field=models.CharField(blank=True, help_text='Which city (and state, and country) will you be traveling from to get to PyOhio?', max_length=127),
        ),
        migrations.AlterField(
            model_name='conferencespeaker',
            name='lodging_assistance',
            field=models.BooleanField(default=False, help_text='Check this field if you require lodging assistance during PyOhio.', verbose_name='Lodging assistance required?'),
        ),
        migrations.AlterField(
            model_name='conferencespeaker',
            name='travel_assistance',
            field=models.BooleanField(default=False, help_text='Check this field if you require travel assistance to get to PyOhio.', verbose_name='Travel assistance required?'),
        ),
    ]
