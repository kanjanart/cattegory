from django.db import models


class Cattegorys(models.Model):
    species = models.CharField(null=True, blank=True, max_length=50)
    price = models.IntegerField(null=True, blank=False)
    food = models.CharField(null=True, blank=True, max_length=50)
    buy_place = models.CharField(null=True, blank=True, max_length=50)
