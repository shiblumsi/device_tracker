from rest_framework import serializers
from companyio.models import CompanyProfile
from subscriptionio.models import  Transaction, SubscriptionPlan
from datetime import datetime


class TransactionSerializer(serializers.ModelSerializer):
    plan = serializers.PrimaryKeyRelatedField(queryset=SubscriptionPlan.objects.all())
   

    class Meta:
        model = Transaction
        fields = ['id', 'plan']

    def create(self, validated_data):
        user = self.context['request'].user
        company = CompanyProfile.objects.get(company_user=user)
        plan = validated_data.pop('plan')
        transaction = Transaction.objects.create(company=company, plan=plan, **validated_data)
        return transaction
    

class TransactionDetailSerializer(serializers.ModelSerializer):
    remaining_days = serializers.SerializerMethodField()

    class Meta:
        model = Transaction
        fields = ['plan', 'purchase_date', 'expiration_date', 'remaining_days']

    def get_remaining_days(self, obj):
        # Calculate remaining days based on current date
        current_date = datetime.now().date()
        expiration_date = obj.expiration_date.date()
        remaining_days = (expiration_date - current_date).days
        return remaining_days
