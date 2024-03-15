from django.db import models
from accountio.rest.managers import CustomUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin



class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_organization = models.BooleanField(default=False)

    objects = CustomUserManager()
    USERNAME_FIELD = 'username'


