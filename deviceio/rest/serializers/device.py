from rest_framework import serializers
from companyio.models import CompanyProfile
from deviceio.models import Device


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ['uuid', 'name', 'configuration', 'condition', 'status', 'device_type']

    def create(self, validated_data):
        user = self.context['request'].user
        company = CompanyProfile.objects.get(company_user=user)
        device = Device.objects.create(company=company, **validated_data)
        return device
