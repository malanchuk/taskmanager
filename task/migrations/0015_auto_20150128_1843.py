# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0014_task_task_pubdate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='task_pubdate',
            new_name='task_date',
        ),
    ]
