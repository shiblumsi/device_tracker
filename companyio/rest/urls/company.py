from django.urls import path
from companyio.rest.views import company

app_name = 'company'

urlpatterns = [
    path('company/profile/create/', company.CompanyProfileCreateView.as_view(), name='company-profile-create'),
    path('company/profile/detail/', company.CompanyProfileDetailView.as_view(), name='company-profile-detail'),
    path('company/profile/update/', company.CompanyProfileUpdateView.as_view(), name='company-profile-update'),
]
