# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-04 21:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djreservation', '0002_auto_20160903_0030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='status',
            field=models.SmallIntegerField(choices=[(0, 'Building'), (1, 'Requested'), (2, 'Acepted'), (3, 'Denied'), (4, 'Borrowed'), (5, 'Returned')], default=0),
        ),
    ]
