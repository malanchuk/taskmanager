# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0008_remove_task_task_pubdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='task_pubdate',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 26, 22, 53, 58, 104720), verbose_name='Published date', blank=True),
            preserve_default=True,
        ),
    ]
