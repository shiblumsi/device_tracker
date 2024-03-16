from rest_framework import permissions
from subscriptionio.models import Transaction
from django.shortcuts import get_object_or_404



class IsCompanyTransaction(permissions.BasePermission):
    def has_permission(self, request, view):
        pk = view.kwargs.get('pk')
        transaction = get_object_or_404(Transaction, pk=pk)
        
        # Check if the logged-in user is the same as the user associated with the company in the transaction
        return request.user == transaction.company.company_user
    
    message = 'You do not have permission to access transactions of other companies.'
