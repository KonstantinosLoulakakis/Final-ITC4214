from django.shortcuts import render
from .models import Product
# Create your views here.

#just renders the products

def render_products(request):
    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(name__icontains=query)
    else:
        products = Product.objects.all()
    
    return render(request, 'products.html', {'products': products})

