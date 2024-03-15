from django.urls import path
from accountio.rest.views import auth

app_name = 'auth'

urlpatterns = [
    path('company/registration',auth.CompanyRegistrationView.as_view(), name='company-registration'),
    path('company/login',auth.LoginView.as_view(), name='company-login'),
]
