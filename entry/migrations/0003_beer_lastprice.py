# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-21 21:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entry', '0002_remove_beer_lastprice'),
    ]

    operations = [
        migrations.AddField(
            model_name='beer',
            name='lastPrice',
            field=models.FloatField(default=0.0),
        ),
    ]