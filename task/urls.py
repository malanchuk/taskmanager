# -*- coding: utf8 -*-

from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^tasks/get/(?P<task_id>\d+)/$', 'task.views.task', name='task detail'),
    url(r'^tasks/addcomment/(?P<task_id>\d+)/$', 'task.views.addcomment', name='addcomment'),
    url(r'^page/(\d+)/$', 'task.views.tasks', name='pagination'),    
    url(r'^$', 'task.views.tasks'),
    url(r'^ckeditor/', include('ckeditor.urls')),
  # url(r'^tasks/user/(?P<user_id>\d+)/$', 'task.views.user_tasks_list', name='user'),
)

