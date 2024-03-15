from django.shortcuts import get_object_or_404
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from companyio.models import CompanyProfile
from deviceio.models import ReturnLog
from deviceio.rest.permissions import IsCompanyReturnLog
from deviceio.rest.serializers.return_log import ReturnLogSerializer


class ReturnLogCreateView(CreateAPIView):
    queryset = ReturnLog.objects.filter()
    serializer_class = ReturnLogSerializer


class ReturnLogListView(ListAPIView):
    queryset = ReturnLog.objects.filter()
    serializer_class = ReturnLogSerializer

    def get_queryset(self):
        company_obj = CompanyProfile.objects.get(company_user=self.request.user)
        return self.queryset.filter(company=company_obj)
    

class ReturnLogRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = ReturnLog.objects.filter()
    serializer_class = ReturnLogSerializer
    permission_classes = [IsCompanyReturnLog]

    def get_object(self):
        kwargs = {
            "uuid": self.kwargs.get("uuid", None)
        }
        # Retrieve the ReturnLog object based on the UUID
        return get_object_or_404(ReturnLog, **kwargs)
      