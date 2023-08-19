from django.contrib import admin
from .models import *

# Register your models here.
    

@admin.register(size_varient)
class size_admin(admin.ModelAdmin):
    list_display=['size_name']
    

@admin.register( colour_varient)
class colour_admin(admin.ModelAdmin):
    list_display=['colour_name']
    
@admin.register(products)
class product_admin(admin.ModelAdmin):
    list_display=['product_name','category','slug','price','product_disc','image']
       

    