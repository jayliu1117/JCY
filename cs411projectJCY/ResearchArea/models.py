from django.db import models

# Create your models here.
class CourseRelated(models.Model):
    CourseNum = models.CharField(max_length=200)
    AreaName = models.CharField(max_length=500)
    objects = models.Manager()
