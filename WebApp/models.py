from django.contrib.auth.models import User
from django.core.checks import Tags
from django.db import models

# Create your models here.
# modelos de dados : Produto, Carrinho, Encomenda, Utilizador
class Product(models.Model):
    name = models.CharField(max_length=30)
    stock = models.IntegerField(default=0)
    price = models.FloatField(default=0.0)
    # tags = models.ManyToManyRel(Tags)

class Client(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, on_delete=models.CASCADE)
    last_change = models.DateTimeField()

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    cart = models.ForeignKey(Cart, on_delete=models.RESTRICT)
    payment_method = models.CharField()
    charged = models.FloatField()
