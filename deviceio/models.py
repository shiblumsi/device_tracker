from django.db import models
from accountio.models import CompanyProfile
from deviceio.choices import DEVICE_STATUS, DEVICE_TYPE, CHECKOUT_STATUS
from projectile.utils import BaseModelWithUUID


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


class Device(BaseModelWithUUID):
    name = models.CharField(max_length=255)
    configuration = models.TextField()
    condition = models.TextField()
    status = models.CharField(max_length=2, choices=DEVICE_STATUS, default='AV')
    device_type = models.CharField(max_length=10, choices=DEVICE_TYPE, default='OTHER')
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.company.name})"


class Checkout(BaseModelWithUUID):
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=2, choices=CHECKOUT_STATUS, default='AC')
    checkout_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateField()

    def __str__(self):
        return f"{self.employee.name} - {self.device.name}"


class ReturnLog(BaseModelWithUUID):
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)
    return_condition = models.TextField()
