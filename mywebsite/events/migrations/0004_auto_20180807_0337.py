# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-08-06 22:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_participant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='events_name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='participant',
            name='member2',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='participant',
            name='member3',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='participant',
            name='member4',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='participant',
            name='member5',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='participant',
            name='team_name',
            field=models.CharField(max_length=30, null=True),
        ),
    ]