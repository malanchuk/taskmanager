from django.db import models
from django.contrib.auth.models import User
    

class Task(models.Model):
    users = models.ManyToManyField(User)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    deadline = models.DateField(u'Date', auto_now=True)
    start_date = models.DateField(u'Date', auto_now=True)
    end_date = models.DateField(u'Date', auto_now=True)
    estimated_time = models.DateField(u'Date', auto_now=True)	
    
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
    task_type = models.CharField(max_length=10,
                                 choices=TASK_TYPE_CHOICES,
                                 default=TASK)


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
    task_status = models.CharField(max_length=10,
                                   choices=TASK_STATUS_CHOICES,
                                   default=OPEN)


    LOW = 'Low'
    NORMAL = 'Normal'
    HIGH = 'High'
    TASK_PRIORITY_CHOICES = (
        (LOW, 'Low'),
        (NORMAL, 'Normal'),
        (HIGH, 'High'),
    )
    task_priority = models.CharField(max_length=10,
                                     choices=TASK_PRIORITY_CHOICES,
                                     default=NORMAL)


class Comment(models.Model):
    user = models.ForeignKey(User)
    task = models.ForeignKey(Task)    
    comment = models.CharField(max_length=255)
    Date = models.DateField(u'Date', auto_now=True)

