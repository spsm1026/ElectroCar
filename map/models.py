from django.db import models

class Sido(models.Model):
    sido_name = models.CharField(max_length=200)

    def __str__(self):
        return self.sido_name

class Goo(models.Model):
    sido = models.ForeignKey(Sido, on_delete=models.CASCADE)
    goo_name = models.CharField(max_length=200)

    def __str__(self):
        return self.goo_name