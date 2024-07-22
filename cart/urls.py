from django.urls import path
# from .views import cart_view, add_to_cart, remove_from_cart
from . import views

app_name = 'cart'

#urls for the cart to show with the corresponding items that it has 

urlpatterns = [
    path('', views.cart_view, name='cart_view'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
]
