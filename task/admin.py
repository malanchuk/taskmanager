# -*- coding: utf8 -*-

from django.contrib import admin
from task.models import Task, Comment, Profile

# Register your models her

class TaskAdmin(admin.ModelAdmin):
    list_display = [				     
				    'task_name', 
				    'task_startdate',
				    'task_description',
				    'task_author',			     
				    'task_deadline', 				     
				    'task_enddate', 
				    'task_estimatedtime', 
				    'task_type', 
				    'task_status', 
				    'task_priority',				    
				   ]
    list_filter = ['task_status']
    search_fields = ['task_name', 'task_description']


class CommentAdmin(admin.ModelAdmin):
	list_display = [
					'comments_task',
					'comments_user',					 
					'comments_text', 
					'comments_date'
				   ]	
	list_filter = ['comments_task'] # фильтр по полю comments_task
	search_fields = ['comments_text']


class ProfileAdmin(admin.ModelAdmin):
	list_display = [
					'user', 
					'job_title', 
					'avatar'
				   ]
	list_filter = ['job_title'] # фильтр по полю job_title

admin.site.register(Task, TaskAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Profile, ProfileAdmin)