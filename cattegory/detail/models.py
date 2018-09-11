from django.db import models


class Cattegory(models.Model):
    species = models.CharField(max_length=50)
    price = models.IntegerField()
    food = models.CharField(max_length=50)
    buy_place = models.CharField(max_length=50)
