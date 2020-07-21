from django.db import models

# Create your models here.

class User(models.Model):
    useremail = models.CharField(max_length=200)
    password = models.EmailField(max_length=200)
    cars = models.CharField(max_length=200)
