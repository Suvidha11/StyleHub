from django.shortcuts import render,redirect,HttpResponse
from products.models import *
from Cart.models import *
from django.http import HttpResponseRedirect
from django.db.models import Sum
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
import razorpay


#add to cart function
@login_required(login_url="user_login")
def Add_Cart(request,uid):
       # creating and getting objects from models cart
    cart,_= Cart.objects.get_or_create(user_id=User(id=request.user.id),is_paid=False)
    product=products.objects.get(uid=uid)
    if request.method=='GET':   
        size=request.GET.get('size')
        colour=request.GET.get('colour')
    cart_item=CartItem.objects.create(cart_id=cart,product_id=product,size=size,colour=colour)
    return redirect('cart')

  
def cart(request):
    try:
        cart= Cart.objects.get(user_id=request.user.id,is_paid=False)
        item = CartItem.objects.filter(cart_id__user_id=request.user.id, cart_id__is_paid=False)
        if not item:
            raise ObjectDoesNotExist  # Manually raise the exception if item is empty
    except ObjectDoesNotExist:
        
        return render(request, 'cart/cart.html', {'msg': 'cart is empty'})
    amount=CartItem.objects.filter(cart_id__user_id=request.user.id, cart_id__is_paid=False).aggregate(Sum('product_id__price'))
    total_sum=amount["product_id__price__sum"]
    print(total_sum)
    
    client = razorpay.Client(auth=("rzp_test_pxJNNIHcr3CxZ6", "CopjVOWS9RX0gJBZplC5p6HN"))
    data = { "amount":total_sum, "currency": "INR", "receipt": "order_rcptid_11" }
    payment = client.order.create(data=data)
    print(payment)
    # create_order=order.objects.create(cart_id=cart,order_id=payment['id'])
    return render(request,'cart/cart.html', {'item': item,',payment':payment,'total_sum':total_sum})

def remove_product(request,uid):
    dlt=CartItem.objects.get(uid=uid)
    dlt.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



