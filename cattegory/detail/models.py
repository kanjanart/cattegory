from django.db import models


class Cattegorys(models.Model):
    species = models.CharField(null=True, blank=True, max_length=50)
    price = models.IntegerField(null=True, blank=False, max_length=10)
    food = models.CharField(null=True, blank=True, max_length=50)
    buy_place = models.CharField(null=True, blank=True, max_length=50)
