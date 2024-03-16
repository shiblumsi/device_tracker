from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from rest_framework import status
from companyio.models import CompanyProfile
from deviceio.models import Device, Checkout
from deviceio.rest.permissions import IsCompanyDevice
from deviceio.rest.serializers.device import DeviceSerializer
from deviceio.rest.serializers.checkout import CheckoutSerializer



class DeviceCreateView(CreateAPIView):
    queryset = Device.objects.filter()
    serializer_class = DeviceSerializer


class DeviceListView(ListAPIView):
    queryset = Device.objects.filter()
    serializer_class = DeviceSerializer

    def get_queryset(self):
        company_obj = CompanyProfile.objects.get(company_user=self.request.user)
        return self.queryset.filter(company=company_obj)
    

class DeviceRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Device.objects.filter()
    serializer_class = DeviceSerializer
    permission_classes = [IsCompanyDevice]

    def get_object(self):
        kwargs = {
            "uuid": self.kwargs.get("uuid", None)
        }
        # Retrieve the device object based on the UUID
        return get_object_or_404(Device, **kwargs)
      


class DeviceDetailView(RetrieveAPIView):
    serializer_class = DeviceSerializer
    permission_classes = [IsCompanyDevice]

    def retrieve(self, request, *args, **kwargs):
        uuid = kwargs.get('uuid')
        try:
            device = Device.objects.get(uuid=uuid)
        except Device.DoesNotExist:
            return Response({"message": "Device not found"}, status=status.HTTP_404_NOT_FOUND)

        if device.status == 'AV':
            # status Available
            serializer = self.get_serializer(device)
            return Response(serializer.data)
        elif device.status == 'IS':
            # status is In Service
            checkouts = Checkout.objects.filter(device=device).order_by('-checkout_date')
            checkout = checkouts.first()
            serializer = CheckoutSerializer(checkout)
            return Response(serializer.data)
        else:
            return Response({"message": "Invalid device status"}, status=status.HTTP_400_BAD_REQUEST)
