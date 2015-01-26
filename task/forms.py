# -*- coding: utf8 -*-
from django.forms import ModelForm
from models import Comment, Task

class CommentForm(ModelForm):
	class Meta:
		model = Comment
		fields = [
				 'comments_user',				 
				 'comments_text'
				 ] # перечисление отображаемых полей


class TaskForm(ModelForm):
	class Meta:
		model = Task
		fields = [ 
				 'task_users', 
				 'task_author',
				 'task_name',
				 'task_description',  
				 'task_type',
				 'task_status', 
				 'task_priority'
				 ] # перечисление отображаемых полей