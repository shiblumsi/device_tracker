from django.db import models
from django.conf import settings
from projectile.utils import BaseModelWithUUID

class CompanyProfile(BaseModelWithUUID):
    company_user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.name
    

class Department(BaseModelWithUUID):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['name', 'company']

    def __str__(self):
        return f"{self.name} ({self.company.name})"


class Employee(BaseModelWithUUID):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.name