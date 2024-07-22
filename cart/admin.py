# cart/admin.py
from django.contrib import admin
from .models import Cart, CartItem

#for the admin panel

admin.site.register(Cart)
admin.site.register(CartItem)
