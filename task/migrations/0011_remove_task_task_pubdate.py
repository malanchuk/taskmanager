# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0010_auto_20150126_2305'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='task_pubdate',
        ),
    ]
