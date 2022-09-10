from django.db import models

# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length=122)
    mob = models.CharField(max_length=122)
    username = models.CharField(max_length=122)
    password = models.CharField(max_length=122)
    email = models.CharField(max_length=122)

class Task(models.Model):
    name = models.CharField(max_length=122)
    do = models.CharField(max_length=122)
    status = models.CharField(max_length=122)
    
