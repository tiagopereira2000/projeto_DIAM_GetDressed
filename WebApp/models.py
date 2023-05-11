from django.contrib.auth.models import User
# from django.core.checks import Tags
from django.db import models


# Create your models here.
# modelos de dados : Produto, Carrinho, Encomenda, Utilizador

class Category(models.Model):
    name = models.CharField(max_length=50)


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=300, default="Sem descrição")
    stock = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)
    image = models.ImageField(upload_to="images/", default=None)

    def __str__(self):
        return self.name


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Cart(models.Model):
    client = models.OneToOneField(Client, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product, through="CartProduct")

    # last_change = models.DateTimeField()
    def __str__(self):
        return self.client.name + str(self.product.all())


class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()

    def __str__(self):
        return "carrinho de:" + self.cart.client.name + "adicionado "\
            + self.product.name + ". quantidade: " + str(self.amount)


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.RESTRICT)
    products = models.ManyToManyField(Product, through="ProductOrder")
    payment_method = models.CharField(max_length=30)
    charged = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.client.name + " : " + str(self.products.all()) + \
            " : " + self.payment_method + " : " + str(self.charged)


class ProductOrder(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()

    def __str__(self):
        return self.product.name + " adicionado à encomenda de: " + \
            self.order.client.name + ". quantidade: " + str(self.amount)
