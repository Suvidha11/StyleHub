from django.contrib import admin
from .models import User

# Register your models here.
@admin.register(User)
class user_admin(admin.ModelAdmin):
    list_display=['email','full_name','mobile_no','OTP']
