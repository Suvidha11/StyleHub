from django.urls import path
from .import views
urlpatterns =[
   path('',views.products_display,name='products_display'),
   path('product_info/<slug>',views.product_info, name='product_info'),
   path('search',views.search,name='search'),
   path('sort_item',views.sort_item,name='sort_item'),
    ]
