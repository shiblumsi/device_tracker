from rest_framework import serializers
from companyio.models import CompanyProfile, Department, Employee

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