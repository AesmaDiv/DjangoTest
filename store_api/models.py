from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    deleted = models.BooleanField(default=False)


class Product(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.IntegerField()
    categories = models.ManyToManyField(Category)
    posted = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False)
