# -*- coding: utf-8 -*-
from django.db import models
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
 

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    avatar = models.ImageField(u'avatar', max_length=1000)
    job_title = models.CharField(max_length=25)

    def __unicode__(self):
        return self.user.username
   
class Task(models.Model):
    users = models.ManyToManyField(User, related_name='user')
    author = models.ForeignKey(User, related_name='user1')    
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    deadline = models.DateField(u'Deadline', auto_now=True)
    start_date = models.DateField(u'Start date', auto_now=True)
    end_date = models.DateField(u'End date', auto_now=True)
    estimated_time = models.DateField(u'Estimated time', auto_now=True)
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
        return self.name


class Comment(models.Model):
    user = models.ForeignKey(User)
    task = models.ForeignKey(Task)    
    comment = models.TextField(verbose_name="Коментарии")
    Date = models.DateField(u'Date', auto_now=True)




