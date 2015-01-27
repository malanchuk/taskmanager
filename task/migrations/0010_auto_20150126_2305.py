# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0009_task_task_pubdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_pubdate',
            field=models.DateTimeField(auto_now=True, verbose_name='Published date'),
            preserve_default=True,
        ),
    ]
