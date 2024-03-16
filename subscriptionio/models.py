from django.db import models
from django.utils import timezone
from companyio.models import CompanyProfile

from projectile.utils import BaseModelWithUUID


class SubscriptionPlan(models.Model):
    DURATION_CHOICES = (
        (1, '1 Month'),
        (6, '6 Months'),
        (12, '12 Months'),
    )

    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.IntegerField(choices=DURATION_CHOICES)

    
    




class Transaction(models.Model):
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
    plan = models.ForeignKey(SubscriptionPlan, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(default=timezone.now)
    expiration_date = models.DateTimeField()

    def save(self, *args, **kwargs):
        # Set expiration date based on plan duration
        self.expiration_date = self.purchase_date + timezone.timedelta(days=30 * self.plan.duration)
        super().save(*args, **kwargs)
