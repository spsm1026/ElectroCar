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

class Carcharger(models.Model):
    car_name = models.CharField(max_length=200)
    car_chger_type = models.CharField(max_length=10, null=True) 
    # 1 : DC 차데모, 2 : DC 콤보, 3 : DC 차데모 + DC 콤보, 4 : AC3상