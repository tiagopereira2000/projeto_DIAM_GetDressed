from django.urls import include, path
from . import views
# (. significa que importa views da mesma directoria)

urlpatterns = [
    path("", views.home, name="home"),
    path("login", views.loginview, name="login"),
    path('mycart', views.cart, name='cart'),
    # path('register', views.register, name="register"),
]