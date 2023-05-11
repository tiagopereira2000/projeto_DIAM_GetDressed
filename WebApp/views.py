# Create your views here.
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product, Cart, Order, Client
from django.shortcuts import get_object_or_404, redirect
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
    return redirect('/login')

def cart(request):
    # Obtém o cliente associado ao usuário atual
    client = request.user.client

    # Obtém o carrinho do cliente
    cart = client.cart

    # Obtém todos os produtos do carrinho
    products = cart.product.all()

    # Renderiza o template de exibição do carrinho com os produtos
    return render(request, 'cart.html', {'products': products})


def remove_product(request, product_id):
    cart = request.user.client.cart
    product = get_object_or_404(Product, id=product_id)
    cart.product.remove(product)
    cart.save()
    return redirect('cart')

def add2cart(request, product_id):
    cart = request.user.client.cart
    product = get_object_or_404(Product, id=product_id)
    cart.product.add(product)
    cart.save()
    return redirect('home')