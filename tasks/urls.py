# -*- coding: utf8 -*-
from django.conf.urls import patterns, include, url
urlpatterns = patterns('',
    url(r'^tasks/get/(?P<task_id>\d+)/$', 'tasks.views.task', name='task detail'),
    url(r'^tasks/addcomment/(?P<task_id>\d+)/$', 'tasks.views.addcomment'),
    url(r'^page/(\d+)/$', 'tasks.views.tasks'),
    url(r'^$', 'tasks.views.tasks'),

)
