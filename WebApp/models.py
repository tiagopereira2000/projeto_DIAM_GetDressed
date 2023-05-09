from django.contrib.auth.models import User
from django.db import models

# Create your models here.
# modelos de dados : Produto, Carrinho, Encomenda, Utilizador
class Produto(models.Model):
    nome = models.CharField(max_length=30)
class Utilizador(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
