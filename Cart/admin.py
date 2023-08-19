from django.contrib import admin
from Cart.models import *
# Register your models here.
@admin.register(Cart)
class Cart_admin(admin.ModelAdmin):
    list_display=['user_id','is_paid',]

@admin.register(CartItem)
class CartItem_admin(admin.ModelAdmin):
    list_display=['cart_id','product_id','size',"colour"]

@admin.register(order)
class order(admin.ModelAdmin):
    list_display=['cart_id','payment_id','order_id','total_amount','date']