from rest_framework import permissions
from deviceio.models import Checkout, Device, ReturnLog
from django.shortcuts import get_object_or_404





class IsCompanyDevice(permissions.BasePermission):
    def has_permission(self, request, view):
        uuid = view.kwargs.get('uuid')
        device = get_object_or_404(Device, uuid=uuid)
        # Check if the logged-in user is the owner(company_user) of the device's company
        return request.user == device.company.company_user
    
    message = 'You do not have permission to access devices of other companies.'


class IsCompanyCheckout(permissions.BasePermission):
    def has_permission(self, request, view):
        uuid = view.kwargs.get('uuid')
        checkout = get_object_or_404(Checkout, uuid=uuid) 
        return request.user == checkout.company.company_user
    
    message = 'You do not have permission to access other companies.'


class IsCompanyReturnLog(permissions.BasePermission):
    def has_permission(self, request, view):
        uuid = view.kwargs.get('uuid')
        returnlog = get_object_or_404(ReturnLog, uuid=uuid) 
        return request.user == returnlog.company.company_user
    
    message = 'You do not have permission to access other companies.'