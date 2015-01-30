# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0013_auto_20150128_1837'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='task_pubdate',
            field=models.DateTimeField(null=True, verbose_name='End date', blank=True),
            preserve_default=True,
        ),
    ]
