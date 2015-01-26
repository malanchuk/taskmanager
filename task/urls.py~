# -*- coding: utf8 -*-

from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^tasks/all/$', 'task.views.tasks'),
	url(r'^tasks/get/(?P<task_id>\d+)/$', 'task.views.task'),
    url(r'^tasks/addcomment/(?P<task_id>\d+)/$', 'task.views.addcomment'),
    url(r'^page/(\d+)/$', 'task.views.tasks'),    
    url(r'^$', 'task.views.tasks'),
)

