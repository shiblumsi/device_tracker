from django.shortcuts import get_object_or_404
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from deviceio.rest.permissions import IsCompanyDepartment
from deviceio.models import Department
from accountio.models import CompanyProfile
from deviceio.rest.serializers.department import DepartmentSerializer

class DepartmentCreateView(CreateAPIView):
    queryset = Department.objects.filter()
    serializer_class = DepartmentSerializer


class DepartmentListView(ListAPIView):
    queryset = Department.objects.filter()
    serializer_class = DepartmentSerializer

    def get_queryset(self):
        company_obj = CompanyProfile.objects.get(company_user=self.request.user)
        return self.queryset.filter(company=company_obj)
    

class DepartmentDetailView(RetrieveAPIView):
    queryset = Department.objects.filter()
    serializer_class = DepartmentSerializer
    permission_classes = [IsCompanyDepartment]

    def get_object(self):
        kwargs = {
            "uuid": self.kwargs.get("uuid", None)
        }
        # Retrieve the department object based on the UUID
        return get_object_or_404(Department, **kwargs)
    

    
class DepartmentUpdateView(UpdateAPIView):
    queryset = Department.objects.filter()
    serializer_class = DepartmentSerializer
    permission_classes = [IsCompanyDepartment]

    def get_object(self):
        kwargs = {
            "uuid": self.kwargs.get("uuid", None)
        }
        # Retrieve the department object based on the UUID
        return get_object_or_404(Department, **kwargs)


class DepartmentDestroyView(DestroyAPIView):
    queryset = Department.objects.filter()
    serializer_class = DepartmentSerializer
    permission_classes = [IsCompanyDepartment]

    def get_object(self):
        kwargs = {
            "uuid": self.kwargs.get("uuid", None)
        }
        # Retrieve the department object based on the UUID
        return get_object_or_404(Department, **kwargs)