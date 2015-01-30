# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0018_auto_20150129_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default=b'/12345.jpg', upload_to=b'', verbose_name='avatar'),
            preserve_default=True,
        ),
    ]
