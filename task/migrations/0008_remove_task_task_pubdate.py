# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0007_task_task_pubdate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='task_pubdate',
        ),
    ]
