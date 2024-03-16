from rest_framework.generics import CreateAPIView
from rest_framework import status
from rest_framework.response import Response
from subscriptionio.models import SubscriptionPlan,Transaction
from subscriptionio.rest.serializers.purchase import  TransactionSerializer

class PurchaseSubscriptionView(CreateAPIView):
    
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()
