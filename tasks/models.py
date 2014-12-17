from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50)
    
class Task(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    status = models.CharField(max_length=50)

class Comment(models.Model):
    user = models.ForeignKey(User)
    task = models.ForeignKey(Task)    
    comment = models.CharField(max_length=255)
    
    
