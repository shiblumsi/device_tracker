from django.shortcuts import get_object_or_404
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from companyio.models import CompanyProfile
from deviceio.models import Checkout
from deviceio.rest.permissions import IsCompanyCheckout
from deviceio.rest.serializers.checkout import CheckoutSerializer


class CheckoutCreateView(CreateAPIView):
    queryset = Checkout.objects.filter()
    serializer_class = CheckoutSerializer
    permission_classes = [IsCompanyCheckout]


class CheckoutListView(ListAPIView):
    queryset = Checkout.objects.filter()
    serializer_class = CheckoutSerializer

    def get_queryset(self):
        company_obj = CompanyProfile.objects.get(company_user=self.request.user)
        return self.queryset.filter(company=company_obj)
    

class CheckoutRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Checkout.objects.filter()
    serializer_class = CheckoutSerializer
    permission_classes = [IsCompanyCheckout]

    def get_object(self):
        kwargs = {
            "uuid": self.kwargs.get("uuid", None)
        }
        # Retrieve the checkout object based on the UUID
        return get_object_or_404(Checkout, **kwargs)
      