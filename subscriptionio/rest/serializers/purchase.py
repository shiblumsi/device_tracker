from rest_framework import serializers
from companyio.models import CompanyProfile
from subscriptionio.models import  Transaction, SubscriptionPlan


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
