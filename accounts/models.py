import datetime

from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin


USER_TYPES = ((1, 'INVESTOR'),
              (2, 'FUND_SEEKER'))


class UserManager(BaseUserManager):
    """Create and save user"""

    def _create_user(self, email, first_name, password=None, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, email, first_name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, first_name, password, **extra_fields)

    def create_superuser(self, email, first_name, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')
        return self._create_user(email, first_name, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """ Creating customized user model """

    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64, blank=True, null=True)
    email = models.EmailField(unique=True, db_index=True)
    title = models.CharField(max_length=128, blank=True, default='')
    location = models.CharField(blank=True, default='', max_length=128)
    country = models.ForeignKey('listing.Country', blank=True, null=True, db_index=True, on_delete=models.CASCADE)
    fund = models.CharField(max_length=200, blank=True, default='')
    mobile = models.CharField(max_length=16, blank=True, default="")
    mobile_code = models.CharField(max_length=6, blank=True, null=True, default="")
    land_line = models.CharField(max_length=16, blank=True, null=True, default="")
    land_line_code = models.CharField(max_length=6, blank=True, null=True, default="")
    user_type = models.IntegerField(choices=USER_TYPES, blank=True, null=True)
    is_active = models.BooleanField(default=False)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']

    objects = UserManager()

    def __str__(self):
        return str(self.email)

    def get_full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def get_short_name(self):
        return str(self.first_name)



# from django.core.validators import RegexValidator
#
# class PhoneModel(models.Model):
#     ...
#     phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
#     phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
