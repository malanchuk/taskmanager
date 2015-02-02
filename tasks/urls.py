# -*- coding: utf8 -*-
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^tasks/get/(?P<task_id>\d+)/$', 'tasks.views.task', name='task detail'),
    url(r'^tasks/addcomment/(?P<task_id>\d+)/$', 'tasks.views.addcomment'),
    url(r'^tasks/addtask/(?P<user_id>\d+)/$', 'tasks.views.addtask', name='add task'),
    url(r'^tasks/set/(?P<user_id>\d+)/$', 'tasks.views.set', name='set task'),
    url(r'^tasks/performs/(?P<user_id>\d+)/$', 'tasks.views.performs', name='performs task'),
    #url(r'^task/add/(?P<user_id>\d+)/$', 'tasks.views.addtask', name='add task'),
    #url(r'^task/add/add/$', 'tasks.views.addt'),
    url(r'^page/(\d+)/$', 'tasks.views.tasks'),
    url(r'^$', 'tasks.views.tasks'),

)


