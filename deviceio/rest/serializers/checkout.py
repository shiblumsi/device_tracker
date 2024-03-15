from rest_framework import serializers

from companyio.models import CompanyProfile, Employee
from deviceio.models import Checkout, Device

class CheckoutSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        user = self.context['request'].user
        company = CompanyProfile.objects.get(company_user=user)
        # filter a perticular companies employee
        self.fields['employee'].queryset = Employee.objects.filter(company=company)
        # filter only a particular companies available devices
        self.fields['device'].queryset = Device.objects.filter(company=company, status='AV')
        

    class Meta:
        model = Checkout
        fields = ['uuid','employee', 'device', 'return_date']

    def create(self, validated_data):
        user = self.context['request'].user
        company = CompanyProfile.objects.get(company_user=user)

        # When a device handed out, its status should changed to In Progress
        device = validated_data['device']
        device.status = 'IS'
        device.save()

        # default status "AV" available
        checkout = Checkout.objects.create(company=company, status='AV', **validated_data)
        return checkout