from django.db import models
from products.models import *

# Create your models here.
#  models for cart

class Cart(base_model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    is_paid=models.BooleanField(default=False)
     
#models for cart item

class CartItem(base_model):
    cart_id=models.ForeignKey(Cart,on_delete=models.CASCADE,related_name='cart')
    product_id=models.ForeignKey(products,on_delete=models.CASCADE,related_name='products')
    size=models.CharField( max_length=20,blank=True)
    colour=models.CharField(max_length=20,blank=True)


class order(base_model):
    cart_id=models.ForeignKey(Cart,on_delete=models.CASCADE,related_name='order_card')
    payment_id=models.CharField(max_length=100,unique=True,blank=True)
    order_id=models.CharField( max_length=100,blank=True)
    total_amount=models.IntegerField(default=0)
    date=models.DateTimeField(auto_now_add=True)
   


    
    