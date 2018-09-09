from django.db import models

# Create your models here.
class cattegory(models.Model):
    species = models.CharField(max_legth=50)
    Price = models.IntegerField()
    food = models.CharField(max_length=30)
    buy_place = models.CharField(max_length=50)
