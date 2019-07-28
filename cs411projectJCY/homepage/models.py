from django.db import models

#Create your models here.
class Courses(models.Model):
    CourseNum = models.CharField(max_length=200)
    CourseName = models.CharField(max_length=200)
    Credits = models.CharField(max_length=100)
    Description = models.CharField(max_length=1000)
    Topics = models.CharField(max_length=1000)
    objects = models.Manager()