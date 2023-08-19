from django.urls import path
from .import views
urlpatterns = [
    path('Add_Cart/<uid>', views.Add_Cart, name='Add_Cart'),
    path('cart', views.cart, name='cart'),
    path('remove_product/<uid>', views.remove_product, name='remove_product')
]
