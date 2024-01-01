from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


# Create your models here.

class CustomAccountManager(BaseUserManager):
    def create_superuser(self,  email, user_name, first_name, password, **other_fields):
        
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_admin', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_admin') is not True:
            raise ValueError(
                'Superuser must be assigned to is_admin=True.')
        return self.create_user( email, user_name, first_name, password, **other_fields)

    def create_user(self, email, user_name, first_name,password, **other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model( email=email, user_name=user_name, first_name=first_name,**other_fields)
        user.set_password(password)
        user.save()
        return user


class NewUser(AbstractBaseUser, PermissionsMixin):
    IS_VENDOR = "V"
    IS_USER = "U"
    CHOOSE = ""

    ACCOUNT_TYPE = [
        (IS_VENDOR, 'Vendor'),
        (IS_USER, 'User'),
        (CHOOSE, 'Type of account')
    ]

    image = models.ImageField(blank=True, verbose_name='User Image', null=True, upload_to='uploads', default='')
    email = models.EmailField(_('email address'), unique=True)
    user_name = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    start_date = models.DateTimeField(default=timezone.now)
    phone_number = models.CharField(max_length=100, blank=True)
    about = models.TextField(_('about'), max_length=500, blank=True)
    account_type = models.CharField(max_length=40, choices=ACCOUNT_TYPE, default=CHOOSE)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin= models.BooleanField(default=False)
    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'first_name', 'last_name']

    def __str__(self):
        return self.user_name
    
    def image_url(self):
        if self.image:
            return self.image.url

