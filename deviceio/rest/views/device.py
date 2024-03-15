from django.shortcuts import get_object_or_404
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from companyio.models import CompanyProfile
from deviceio.models import Device
from deviceio.rest.permissions import IsCompanyDevice
from deviceio.rest.serializers.device import DeviceSerializer


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
      