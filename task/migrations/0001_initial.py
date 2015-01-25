# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comments_text', models.TextField(verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xba\xd1\x81\xd1\x82 \xd0\xba\xd0\xbe\xd0\xbc\xd0\xbc\xd0\xb5\xd0\xbd\xd1\x82\xd0\xb0\xd1\x80\xd0\xb8\xd1\x8f')),
                ('comments_date', models.DateTimeField(auto_now=True, verbose_name='Published date')),
            ],
            options={
                'db_table': 'comments',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('avatar', models.ImageField(upload_to=b'', max_length=1000, verbose_name='avatar')),
                ('job_title', models.CharField(max_length=100)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('task_name', models.CharField(max_length=255)),
                ('task_description', models.TextField(verbose_name=b'\xd0\x9f\xd0\xbe\xd0\xb4\xd1\x80\xd0\xbe\xd0\xb1\xd0\xbd\xd0\xbe\xd0\xb5 \xd0\xbe\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\xb7\xd0\xb0\xd0\xb4\xd0\xb0\xd1\x87\xd0\xb8')),
                ('task_deadline', models.DateField(auto_now=True, verbose_name='Deadline')),
                ('task_startdate', models.DateField(auto_now=True, verbose_name='Start date')),
                ('task_enddate', models.DateField(auto_now=True, verbose_name='End date')),
                ('task_estimatedtime', models.DateField(auto_now=True, verbose_name='Estimated time')),
                ('task_type', models.CharField(default=b'Task', max_length=10, choices=[(b'Task', b'Task'), (b'Error', b'Error'), (b'Correction', b'Correction'), (b'Check', b'Check')])),
                ('task_status', models.CharField(default=b'Open', max_length=10, choices=[(b'Open', b'Open'), (b'In work', b'In work'), (b'Closed', b'Closed'), (b'Overdue', b'Overdue')])),
                ('task_priority', models.CharField(default=b'Normal', max_length=10, choices=[(b'Low', b'Low'), (b'Normal', b'Normal'), (b'High', b'High')])),
                ('task_author', models.ForeignKey(related_name='user1', to=settings.AUTH_USER_MODEL)),
                ('task_users', models.ManyToManyField(related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'task',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='comments',
            name='comments_task',
            field=models.ForeignKey(to='task.Task'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comments',
            name='comments_user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
