# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0012_auto_20150126_2324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_description',
            field=ckeditor.fields.RichTextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
