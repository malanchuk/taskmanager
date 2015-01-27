# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0011_remove_task_task_pubdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_deadline',
            field=models.DateTimeField(null=True, verbose_name='Deadline', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='task_enddate',
            field=models.DateTimeField(null=True, verbose_name='End date', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='task_estimatedtime',
            field=models.DateTimeField(null=True, verbose_name='Estimated time', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='task_startdate',
            field=models.DateTimeField(auto_now=True, verbose_name='Start date'),
            preserve_default=True,
        ),
    ]
