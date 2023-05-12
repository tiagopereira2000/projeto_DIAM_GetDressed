# Create your views here.
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Product, Cart, Order, Client
from .forms import *

@login_required(login_url='login')
def home(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, 'home.html', context)


def loginview(request):
    form = AuthenticationForm(request, data=request.POST or None)
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect('home')
    return render(request, 'login.html', {'form': form})

def logoutview(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def cart(request):
    # in_cart = Cart.user.cart_set
    return render(request, 'cart.html')

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    context = {"product": product}
    return render(request, 'product.html', context)

def edit_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method=='POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('edit_product', product_id=product_id)
    else:
        form = ProductForm(instance=product)
    return render(request, 'editProduct.html', {"form":form, "product":product})