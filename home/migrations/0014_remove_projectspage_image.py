# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-18 16:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20170418_1144'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectspage',
            name='image',
        ),
    ]