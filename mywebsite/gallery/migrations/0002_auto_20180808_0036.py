# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-08-07 19:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gallery',
            old_name='img',
            new_name='image',
        ),
    ]
