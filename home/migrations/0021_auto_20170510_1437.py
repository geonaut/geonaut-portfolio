# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-10 14:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0018_remove_rendition_filter'),
        ('home', '0020_auto_20170510_1415'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactpage',
            old_name='body',
            new_name='body_header',
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='body_header',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='header_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='contactpage',
            name='header_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
    ]