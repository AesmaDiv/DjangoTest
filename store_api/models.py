from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.IntegerField()


class Category(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()


class Chain(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
