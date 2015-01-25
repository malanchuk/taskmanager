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
				    'task_priority'
				   ]
    ordering = ['task_startdate']

class CommentAdmin(admin.ModelAdmin):
	list_display = [
					'comments_user', 
					'comments_task', 
					'comments_text', 
					'comments_date'
				   ]	
	ordering = ['comments_task']

class ProfileAdmin(admin.ModelAdmin):
	list_display = [
					'user', 
					'job_title', 
					'avatar'
				   ]
	ordering = ['job_title']

admin.site.register(Task, TaskAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Profile, ProfileAdmin)