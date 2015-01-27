# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0006_auto_20150125_1352'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='task_pubdate',
            field=models.DateTimeField(default=2, verbose_name='Published date', auto_now=True),
            preserve_default=False,
        ),
    ]
