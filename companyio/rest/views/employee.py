from django.shortcuts import get_object_or_404
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from companyio.models import Employee, CompanyProfile
from companyio.rest.permissions import IsCompanyEmployee
from companyio.rest.serializers.employee import EmployeeSerializer


class EmployeeCreateView(CreateAPIView):
    queryset = Employee.objects.filter()
    serializer_class = EmployeeSerializer


class EmployeeListView(ListAPIView):
    queryset = Employee.objects.filter()
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        company_obj = CompanyProfile.objects.get(company_user=self.request.user)
        return self.queryset.filter(company=company_obj)
    

class EmployeeRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.filter()
    serializer_class = EmployeeSerializer
    permission_classes = [IsCompanyEmployee]

    def get_object(self):
        kwargs = {
            "uuid": self.kwargs.get("uuid", None)
        }
        # Retrieve the employee object based on the UUID
        return get_object_or_404(Employee, **kwargs)
      