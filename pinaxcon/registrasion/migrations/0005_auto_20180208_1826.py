# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-09 02:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pinaxcon_registrasion', '0004_attendeeprofile_agreement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendeeprofile',
            name='agreement',
            field=models.BooleanField(default=False, help_text=b"I agree to act according to the <a href='/code-of-conduct'> North Bay Python Code of Conduct</a>. I also agree with the North Bay Python <a href='/terms'>Terms and Conditions</a>.", verbose_name=b'Agreement'),
        ),
    ]
