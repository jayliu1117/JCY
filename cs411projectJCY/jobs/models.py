from django.db import models

# Create your models here.
class jobrelated(models.Model):
    Company = models.CharField(max_length=200)
    JobTitle = models.CharField(max_length=200)
    CityState = models.CharField(max_length=200)
    Description = models.CharField(max_length=500)
    JobUrl = models.CharField(max_length=1000)
    AreaName = models.CharField(max_length=200)
    ResearchKeyWord = models.CharField(max_length=500)
    objects = models.Manager()