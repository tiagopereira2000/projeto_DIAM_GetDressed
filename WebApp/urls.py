from django.urls import include, path
from . import views
# (. significa que importa views da mesma directoria)

urlpatterns = [
    path("", views.home, name="home"),
    path("login", views.loginview, name="login"),
    path('cart/', views.cart, name='cart'),
    # path('register', views.register, name="register"),
    # path('order', views.order, name='order'),
    # path('<int: product_id>/product', views.product, name='product'),

]