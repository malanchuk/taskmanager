# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_auto_20150124_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_deadline',
            field=models.DateField(null=True, verbose_name='Deadline', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='task_enddate',
            field=models.DateField(null=True, verbose_name='End date', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='task_estimatedtime',
            field=models.DateField(null=True, verbose_name='Estimated time', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='task_startdate',
            field=models.DateField(null=True, verbose_name='Start date', blank=True),
            preserve_default=True,
        ),
    ]
