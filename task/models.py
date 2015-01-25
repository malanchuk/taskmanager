# -*- coding: utf8 -*-
from django.db import models
from django import forms
from django.contrib.auth.models import User


TASK = 'Task'
ERROR = 'Error'
CORRECTION = 'Correction'
CHECK ='Check'
TASK_TYPE_CHOICES = (
	(TASK, 'Task'),
	(ERROR, 'Error'),
	(CORRECTION, 'Correction'),
	(CHECK, 'Check'),
)
OPEN = 'Open'
IN_WORK = 'In work'
CLOSED = 'Closed'
OVERDUE = 'Overdue'
TASK_STATUS_CHOICES = (
	(OPEN, 'Open'),
	(IN_WORK, 'In work'),
	(CLOSED, 'Closed'),
	(OVERDUE, 'Overdue'),
)
LOW = 'Low'
NORMAL = 'Normal'
HIGH = 'High'
TASK_PRIORITY_CHOICES = (
	(LOW, 'Low'),
	(NORMAL, 'Normal'),
	(HIGH, 'High'),
)
 
  
class Profile(models.Model):
    user   = models.OneToOneField(User)
    avatar = models.ImageField(u'avatar', max_length=1000)
    job_title = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.user.username

class Task(models.Model):
	class Meta:
		db_table = "task"

	task_users = models.ManyToManyField(User, related_name='user')
	task_author = models.ForeignKey(User, related_name='user1')    
	task_name = models.CharField(max_length=255)
	task_description = models.TextField(verbose_name="Подробное описание задачи")
	task_deadline = models.DateField(u'Deadline', blank=True, null=True)
	task_startdate = models.DateField(u'Start date', blank=True, null=True)
	task_enddate = models.DateField(u'End date', blank=True, null=True)
	task_estimatedtime = models.DateField(u'Estimated time', blank=True, null=True)
	task_type = models.CharField(max_length=10,
	                             choices=TASK_TYPE_CHOICES,
	                             default=TASK)
	task_status = models.CharField(max_length=10,
	                               choices=TASK_STATUS_CHOICES,
	                               default=OPEN)
	task_priority = models.CharField(max_length=10,
	                                 choices=TASK_PRIORITY_CHOICES,
	                                 default=NORMAL)

	def __unicode__(self):
		return self.task_name


class Comment(models.Model):
	class Meta():
		db_table = 'comments'

	comments_user = models.ForeignKey(User)
	comments_task = models.ForeignKey(Task)    
	comments_text = models.TextField(verbose_name="Текст комментария")
	comments_date = models.DateTimeField(u'Published date', auto_now=True)



