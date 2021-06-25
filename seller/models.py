from django.db import models


class Seller(models.Model):
    name = models.CharField(max_length=200)
    product = models.IntegerField()
