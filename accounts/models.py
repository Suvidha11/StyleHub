
# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .manager import UserManager
 
class User(AbstractBaseUser):
    email = models.EmailField(verbose_name="email address", max_length=255,unique=True,)
    full_name = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=12,blank=True)
    OTP = models.CharField(max_length=6,blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

# calling from this UserManager class from file name is manager.py for use this manager
    objects = UserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["full_name","OTP","mobile_no"]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):

    # "Does the user have a specific permission?"
    # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
    # "Does the user have permissions to view the app `app_label`?"
    # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
    # "Is the user a member of staff?"
    # Simplest possible answer: All admins are staff
    
        return self.is_admin
        