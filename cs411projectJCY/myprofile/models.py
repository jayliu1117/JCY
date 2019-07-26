from django.db import models

# Create your models here.
class hasTaken(models.Model):
    EmailAddress = models.EmailField(max_length=254)
    CourseNum = models.CharField(max_length=200)
    CourseName = models.CharField(max_length=200)
    objects = models.Manager()