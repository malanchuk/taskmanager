# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0005_auto_20150125_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_description',
            field=ckeditor.fields.RichTextField(),
            preserve_default=True,
        ),
    ]
