from django.contrib import admin
from tasks.models import Task, Comment, UserProfile

class TaskAdmin(admin.ModelAdmin):
    list_display = ['name', 'task_status', 'task_priority', 'start_date', 'end_date', 'estimated_time', 'deadline', 'description']
    ordering = ['start_date']

class CommentAdmin(admin.ModelAdmin):
	list_display = ['user', 'task', 'comment', 'Date']
	ordering = ['task']


class UserProfileAdmin(admin.ModelAdmin):
	list_display = ['user', 'job_title', 'avatar']
	ordering = ['job_title']
	


admin.site.register(Task, TaskAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(UserProfile, UserProfileAdmin)

