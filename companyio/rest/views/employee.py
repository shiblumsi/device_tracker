from django.shortcuts import get_object_or_404
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from companyio.models import Employee, CompanyProfile
from rest_framework.response import Response
from companyio.rest.permissions import IsCompanyEmployee
from companyio.rest.serializers.employee import EmployeeSerializer, EmployeeDeviceSerializer


class EmployeeCreateView(CreateAPIView):
    queryset = Employee.objects.filter()
    serializer_class = EmployeeSerializer
    permission_classes = [IsCompanyEmployee]

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
      


class EmployeeDeviceView(ListAPIView):
    """ View all employee with devices assigned """
    queryset = Employee.objects.all()
    serializer_class = EmployeeDeviceSerializer
    permission_classes = [IsCompanyEmployee]

class EmployeeDeviceListView(RetrieveAPIView):
    """ View devices assigned with specific employee """
    serializer_class = EmployeeDeviceSerializer
    permission_classes = [IsCompanyEmployee]

    def get(self, request, *args, **kwargs):
        uuid = kwargs.get('uuid')
        try:
            employee = Employee.objects.get(uuid=uuid)
        except Employee.DoesNotExist:
            return Response({"message": "Employee not found"}, status=404)
        
        serializer = self.get_serializer(employee)
        return Response(serializer.data)