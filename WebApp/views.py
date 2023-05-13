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
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('edit_product', product_id=product_id)
    else:
        form = ProductForm(instance=product)
    return render(request, 'editProduct.html', {"form": form, "product": product})


@login_required(login_url='login')
def cart(request):
    # Obtém o cliente associado ao usuário atual
    client = request.user.client

    # Obtém o carrinho do cliente
    cart = client.cart

    # Obtém todos os produtos do carrinho
    products = cart.product.all()

    # Renderiza o template de exibição do carrinho com os produtos
    return render(request, 'cart.html', {'products': products})


def removefromcart(request, product_id):
    cart = request.user.client.cart
    product = get_object_or_404(Product, id=product_id)
    existing_cart_product = CartProduct.objects.filter(cart=cart, product=product)
    if existing_cart_product:
        existing_cart_product = existing_cart_product[0]
    if existing_cart_product.amount > 1:
        existing_cart_product.amount -= 1
        existing_cart_product.save()
    else:
        existing_cart_product.delete()
        cart.product.remove(product)
        cart.save()

    return redirect('cart')


@login_required(login_url='login')
def add2cart(request, product_id):
    cart = request.user.client.cart
    product = get_object_or_404(Product, id=product_id)
    existing_cart_product = CartProduct.objects.filter(cart=cart, product=product)
    if existing_cart_product:
        existing_cart_product = existing_cart_product[0]
        existing_cart_product.amount += 1
        existing_cart_product.save()
    else:
        new_cart_product = CartProduct(cart=cart, product=product, amount=1)
        new_cart_product.save()
    cart.product.add(product)
    cart.save()
    return redirect('home')


def checkout(request):
    cart = request.user.client.cart
    cart_products = CartProduct.objects.filter(cart=cart)
    products = cart.product.all()
    total = sum(cp.product.price * cp.amount for cp in cart_products)
    context = {
        'products': products,
        'total': total
    }
    return render(request, 'checkout.html', context)


def end_order(request):
    cart = request.user.client.cart
    CartProduct.objects.filter(cart=cart).delete()
    return redirect('home')


def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductForm()
    return render(request, 'create_product.html', {'form': form})


def delete_product(request, product_id):
    Product.objects.filter(id=product_id).delete()
    return redirect('home')


def user_profile(request):
    return render(request, 'profile.html')


def edit_profile(request):
    client = Client.objects.get(user=request.user)
    if request.method == 'POST':
        form = ClientForm(request.POST, request.FILES, instance=client)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ClientForm(instance=client)

    return render(request, 'editProfile.html', {'form': form})

def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # log in the user
            login(request, user)
            return redirect('home') # replace 'home' with the name of your homepage url
    else:
        form = RegistrationForm()
    return render(request, 'registration.html', {'form': form})


