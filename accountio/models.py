from django.db import models
from accountio.rest.managers import CustomUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.conf import settings
from projectile.utils import BaseModelWithUUID


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_organization = models.BooleanField(default=False)

    objects = CustomUserManager()
    USERNAME_FIELD = 'username'


class CompanyProfile(BaseModelWithUUID):
    company_user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.name
