from django.shortcuts import get_object_or_404
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from subscriptionio.rest.permissions import IsCompanyTransaction
from subscriptionio.rest.serializers.purchase import  TransactionSerializer, TransactionDetailSerializer
from subscriptionio.models import Transaction


class PurchaseSubscriptionView(CreateAPIView):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()


class PurchaseDetailview(RetrieveAPIView):
    """
    Retrieve details of a purchase.
    Only the company that made the purchase can view its details.
    """
    queryset = Transaction.objects.all()
    serializer_class = TransactionDetailSerializer
    permission_classes = [IsCompanyTransaction]

    def get_object(self):
        kwargs = {
            "pk": self.kwargs.get("pk", None)
        }
        # Retrieve the Transaction object based on the pk
        return get_object_or_404(Transaction, **kwargs)
    