from django.contrib.auth.models import BaseUserManager
class UserManager(BaseUserManager):
    def create_user(self, email, full_name, mobile_no, OTP, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError("Users must have an email address")
        user = self.model(
            email=self.normalize_email(email),
            full_name = full_name,
            mobile_no = mobile_no,
            OTP= OTP,
             )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,mobile_no,OTP, full_name,password=None):
        """
        Creates and saves a superuser with the given email
        """
        user = self.create_user(
        email,
        password=password,
        full_name = full_name,
        mobile_no = mobile_no,
        OTP= OTP,
    
        )
        user.is_admin = True
        user.save(using=self._db)
        return user