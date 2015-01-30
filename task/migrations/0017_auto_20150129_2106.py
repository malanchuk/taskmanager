# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0016_auto_20150128_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='job_title',
            field=models.CharField(max_length=25),
            preserve_default=True,
        ),
    ]
