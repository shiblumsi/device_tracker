from django.urls import path
from companyio.rest.views import department

app_name = 'department'

urlpatterns = [
    path('department/create', department.DepartmentCreateView.as_view(),name='department-create'),
    path('department/list', department.DepartmentListView.as_view(),name='department-list'),
    path('department/details/<uuid:uuid>', department.DepartmentDetailView.as_view(),name='department-detail'),
    path('department/update/<uuid:uuid>', department.DepartmentUpdateView.as_view(),name='department-update'),
    path('department/delete/<uuid:uuid>', department.DepartmentDestroyView.as_view(),name='department-delete'),
]
