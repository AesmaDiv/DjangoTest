from django.contrib import admin
from store_api.models import Product, Category, Chain


# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Chain)
