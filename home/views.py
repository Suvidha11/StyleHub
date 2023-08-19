from django.shortcuts import render,redirect,HttpResponse
from products.models import *
from django.db.models import Q

# home page for display all items
def products_display(request):
    items=products.objects.all()     
    return render(request,'home/index.html',{'items':items} ) 
 
def sort_item(request):
    if request.method=='GET':
        sortby_price=request.GET.get('sortby')
        sortby_category=request.GET.get('SortByCategory')
        
        if sortby_price=='low to heigh':
            items=products.objects.all().order_by('price') 
            return render(request,'home/index.html',{'items':items} ) 
        elif sortby_price=='heigh to low':
            items=products.objects.all().order_by('-price') 
            return render(request,'home/index.html',{'items':items} )
        else: 
            SortCategory=products.objects.filter(category__icontains=sortby_category)
            return render(request,'home/index.html',{'items':SortCategory} )  
    return render(request,'home/index.html',{'items':items} )  
        
#product detail page for only one product 
def product_info(request,slug):
    product=products.objects.get(slug=slug)
    return render(request,'home/product_detail.html',{'disp':product})
 
#search
def search(request):
    if request.method=='GET':
       user_search=request.GET['search']
       SearchProduct=products.objects.filter(Q(category__icontains=user_search)|Q(product_name__icontains=user_search))
    return render(request,'home/search.html',{'SearchProduct':SearchProduct})