# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_auto_20150121_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_deadline',
            field=models.DateField(verbose_name='Deadline'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='task_enddate',
            field=models.DateField(verbose_name='End date'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='task_estimatedtime',
            field=models.DateField(verbose_name='Estimated time'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='task_startdate',
            field=models.DateField(verbose_name='Start date'),
            preserve_default=True,
        ),
    ]
