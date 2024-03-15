from rest_framework import serializers
from companyio.models import CompanyProfile, Department

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['uuid', 'name', 'description']
        read_only_fields = ['uuid']

    def validate(self, attrs):
        user = self.context['request'].user
        name = attrs.get('name')
        if Department.objects.filter(company__company_user=user, name=name).exists():
            raise serializers.ValidationError("This department already exists")
        return attrs
    
    def create(self, validated_data):
        # Get the currently logged-in user
        user = self.context['request'].user
        company = CompanyProfile.objects.get(company_user=user)
        department = Department.objects.create(company=company, **validated_data)
        return department

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance