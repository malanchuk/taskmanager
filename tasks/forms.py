# -*- coding: utf-8 -*-

from django.forms import ModelForm
from models import Comment
from models import Task

class CommentForm(ModelForm):
	class Meta:
		model = Comment
		fields = [ 'comment',
				 ]

class TaskForm(ModelForm):
	class Meta:
		model = Task
		fields = [ 'users', 'name', 'description', 'deadline', 'start_date', 'end_date', 'task_type', 'task_status', 'task_priority'] 
