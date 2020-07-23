from django.db import models

# Create your models here.

class User(models.Model):
    useremail = models.CharField(max_length=200)
    password = models.EmailField(max_length=200)
    cars = models.CharField(max_length=200)

# class user_bookmark(models.Model):
#     user_id = ForeignKey(User, on_delete=models.CASCADE)
#     bookmark_name = CharField(max_length=200)
#     bookmark_address = CharField(max_length=200)