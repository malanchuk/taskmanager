# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0015_auto_20150128_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_date',
            field=models.DateTimeField(null=True, verbose_name='Start date', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='task_startdate',
            field=models.DateTimeField(auto_now=True, verbose_name='Creation date'),
            preserve_default=True,
        ),
    ]
