from django.shortcuts import render,redirect,HttpResponseRedirect,HttpResponse
from accounts.models import User 
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login,logout
from django.core.exceptions import ObjectDoesNotExist
import random


# sending mail
def sent(email,otp):
    try:
        msg = "Your otp is \n"+otp 
        subject= "One time password"
        sender =  settings.EMAIL_HOST_USER
        send_mail(subject,msg, sender,[email],fail_silently=False)
    except :
         messages.error("Check your intenet connection........ ")
          
# user signup page
def user_signup(request):
    if request.method=='POST':
        email=request.POST['email']
        full_name=request.POST['full_name']
        mobile_no=request.POST['mobile_no']     
        # otp_generate
        otp=str(random.randint(1000 ,9999))
        sent(email,otp)       
        try:
            check_user = User.objects.get(email=email)
            messages.error(request, "Your email  is already exists")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        except ObjectDoesNotExist:
            add_user = User.objects.create_user(email=email, full_name=full_name, mobile_no=mobile_no, OTP=otp)      
            # send mail
            request.session['email'] = email
            request.session['name'] = full_name
            return redirect('otp_verify')
    else:
        return render(request,"account/signup.html")

#verify_otp
def otp_verify(request):
    if request.method == 'POST': 
        Email = request.POST.get('email')
        otp = request.POST.get('otp')     
        try:
            user = User.objects.get(email=Email)
        except User.DoesNotExist:
            messages.error(request,"User does not exist")      
            return render(request,"account/otp.html")   
        if otp == user.OTP:
            login(request, user)
            messages.success(request,"OTP succesfully match")
            return redirect('products_display')  
        else:
            messages.error(request,"OTP does not match")
            return redirect("otp_verify")
    else:
        return render(request,"account/otp.html")



#user login page
def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user = User.objects.filter(email= email).first()
        if user is None:
            messages.error(request,"Your email id does not exist")
            return render(request, 'account/login.html')
        otp = str(random.randint(1000, 9999))
        
        #update otp field
        user.OTP=otp
        user.save()
        
        sent(email, otp)
        request.session['email'] = email
        messages.success(request,"OTP succesfully match")
        return redirect("otp_verify")
    else:
      return render(request, 'account/login.html')
    


def user_logout(request):
    logout(request)
    return redirect('user_login')


