from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Cart

def home(request):
    products = Product.objects.filter(available=True)
    return render(request, 'showroom/home.html', {'products': products})

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'showroom/product_detail.html', {'product': product})

def add_to_cart(request, id):
    product = get_object_or_404(Product, id=id)
    Cart.objects.create(user=request.user, product=product)
    return redirect('cart')

