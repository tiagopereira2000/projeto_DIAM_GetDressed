from django.urls import include, path
from . import views
# (. significa que importa views da mesma directoria)

urlpatterns = [
    path("", views.home, name="home"),
    path("login", views.loginview, name="login"),
    path('cart/', views.cart, name='cart'),
    # path('register', views.register, name="register"),
    # path('order', views.order, name='order'),
    path('<int:product_id>/product', views.product_detail, name='product'),
    path('<int:product_id>/edit_product', views.edit_product, name='edit_product'),
    path('cart/<int:product_id>/add/', views.add2cart, name='add2cart'),
    path('cart/<int:product_id>/remove/', views.removefromcart, name='removefromcart'),
    path('logout', views.logoutview, name='logout'),
    path('checkout', views.checkout, name='checkout'),
    path('end_order/', views.end_order, name='end_order'),
    path('create_product/', views.create_product, name='create_product'),

]

