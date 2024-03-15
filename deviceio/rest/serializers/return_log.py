from rest_framework import serializers

from companyio.models import Employee, CompanyProfile
from deviceio.models import Checkout, Device, ReturnLog

class ReturnLogSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        user = self.context['request'].user
        company = CompanyProfile.objects.get(company_user=user)
        
        # filter employees who has assigned with device
        self.fields['employee'].queryset = Employee.objects.filter(company=company)
        self.fields['device'].queryset = Device.objects.filter(company=company, status='IS')

    class Meta:
        model = ReturnLog
        fields = ['employee','device','return_condition']

    def create(self, validated_data):
        user = self.context['request'].user
        company = CompanyProfile.objects.get(company_user=user)
        device = validated_data['device']

        # when device return, status should be "AV" (Available)
        device.status="AV"

        # device condition is return condition
        device.condition=validated_data['return_condition']
        device.save()
        checkout_obj = Checkout.objects.get(device=device)

        # when device returned checkout status will be "RE" Returened
        checkout_obj.status='RE'
        checkout_obj.save()
        return_obj = ReturnLog.objects.create(company=company,**validated_data)

        return return_obj