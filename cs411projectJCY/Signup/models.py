from django.db import models

# Create your models here.


class Students(models.Model):
    EmailAddress = models.EmailField(max_length=254)
    PassWord = models.CharField(max_length=200)
    major = models.CharField(max_length=100)
    skills = models.CharField(max_length=100)
    interests = models.CharField(max_length=100)
