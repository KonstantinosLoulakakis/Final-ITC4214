from django.db import models
# from django.contrib.auth.models import User
# Create your models here.

#the info that the created products will have


class Product(models.Model):
   
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', default='Final/media/products/image.jpg')

    def __str__(self):
        return self.name
