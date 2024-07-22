from django.contrib import admin
from .models import Product
from django.db import models

# Register your models here.
# admin panel for the products

class Products(models.Model):
    list_display=['name']

admin.site.register(Product)