# -*- coding: utf8 -*-

from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^tasks/get/(?P<task_id>\d+)/$', 'task.views.task', name='task detail'),
    url(r'^tasks/addcomment/(?P<task_id>\d+)/$', 'task.views.addcomment', name='addcomment'),
    url(r'^page/(\d+)/$', 'task.views.tasks', name='pagination'),    
    url(r'^$', 'task.views.tasks', name="default_tasks"),
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^task/add/(?P<user_id>\d+)/$', 'task.views.addtask', name='addtask'),
    url(r'^task/users_tasks/(?P<user_id>\d+)/$', 'task.views.task_list_users', name='task list users'),
    url(r'^task/author_tasks/(?P<user_id>\d+)/$', 'task.views.task_list_author', name='task list author'),
    url(r'^tasks_sorted_by_status_up/$', 'task.views.tasks_sorted_by_status_up', name="tasks_sorted_by_status_up"),
    url(r'^tasks_sorted_by_status_down/$', 'task.views.tasks_sorted_by_status_down', name="tasks_sorted_by_status_down"),
    url(r'^tasks_sorted_by_priority_up/$', 'task.views.tasks_sorted_by_priority_up', name="tasks_sorted_by_priority_up"),
    url(r'^tasks_sorted_by_priority_down/$', 'task.views.tasks_sorted_by_priority_down', name="tasks_sorted_by_priority_down"),
)

