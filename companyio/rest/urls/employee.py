from django.urls import path
from companyio.rest.views import employee

app_name = 'employee'

urlpatterns = [
    path('employee/create', employee.EmployeeCreateView.as_view(),name='employee-create'),
    path('employee/list', employee.EmployeeListView.as_view(),name='employee-list'),
    path('employee/detail/<uuid:uuid>', employee.EmployeeRetrieveUpdateDestroyView.as_view(),name='employee.detail.update.destroy'),
   
]
