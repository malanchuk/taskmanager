# -*- coding: utf8 -*-
from django.forms import ModelForm
from models import Comment, Task

class CommentForm(ModelForm):
	class Meta:
		model = Comment
		fields = [
				 				 
				 'comments_text'
				 ] # перечисление отображаемых полей


class TaskForm(ModelForm):
	class Meta:
		model = Task
		fields = [
				    'task_users',
				    'task_name',			    
				    'task_description',			     
				    'task_deadline',
				    'task_date', 				     
				    'task_enddate', 
				    'task_estimatedtime', 
				    'task_type', 
				    'task_status', 
				    'task_priority',  				 
				 ] # перечисление отображаемых полей

