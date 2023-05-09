from django.contrib.auth.models import User
from django.db import models

# Create your models here.
# modelos de dados : Produto, Carrinho, Encomenda, Utilizador
class Product(models.Model):
    name = models.CharField(max_length=30)
    stock = models.IntegerField(default=0)
    price = models.FloatField(default=0.0)
    # tags = models

class Client(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE())
    #product_list
    #last_change
    #is_active

#class Order(models.Model):
class Tag(models.Model):
    name = models.CharField(max_length=20)
