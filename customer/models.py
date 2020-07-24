from django.db import models

# Create your models here.

class User(models.Model):
    useremail = models.CharField(max_length=200)
    password = models.EmailField(max_length=200)
    cars = models.CharField(max_length=200)

class Bookmark(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    bookmark_address = models.CharField(max_length=200)