from rest_framework import serializers
from companyio.models import CompanyProfile, Department, Employee
from deviceio.models import Checkout
from deviceio.rest.serializers.device import DeviceSerializer
class EmployeeSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        user = self.context['request'].user
        company = CompanyProfile.objects.get(company_user=user)
        self.fields['department'].queryset = Department.objects.filter(company=company)

    class Meta:
        model = Employee
        fields = ['uuid','name', 'position', 'email', 'phone_number', 'department']

    def create(self, validated_data):
        user = self.context['request'].user
        company = CompanyProfile.objects.get(company_user=user)
        employee = Employee.objects.create(company=company, **validated_data)
        return employee
    

class EmployeeDeviceSerializer(serializers.ModelSerializer):
    devices = serializers.SerializerMethodField()

    class Meta:
        model = Employee
        fields = ['id', 'name', 'devices']

    def get_devices(self, obj):
        checkouts = Checkout.objects.filter(employee=obj)
        devices = [checkout.device for checkout in checkouts]
        return DeviceSerializer(devices, many=True).data