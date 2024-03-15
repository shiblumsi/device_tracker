from django.shortcuts import get_object_or_404
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema

from companyio.models import CompanyProfile
from companyio.rest.serializers.company import CompanyProfileSerializer

class CompanyProfileCreateView(CreateAPIView):
    queryset = CompanyProfile.objects.all()
    serializer_class = CompanyProfileSerializer


class CompanyProfileDetailView(APIView):
    @extend_schema(request=CompanyProfileSerializer)
    def get(self, request, *args, **kwargs):
        # Get the currently logged-in user
        current_user = request.user
        try:
            # Retrieve the CompanyProfile associated with the current user
            company_profile = CompanyProfile.objects.get(company_user=current_user)
        except CompanyProfile.DoesNotExist:
            return Response({"message": "Company Profile does not exist"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = CompanyProfileSerializer(company_profile)
        return Response(serializer.data)
    


class CompanyProfileUpdateView(APIView):
    @extend_schema(request=CompanyProfileSerializer)
    def put(self, request, *args, **kwargs):
        company_profile = get_object_or_404(CompanyProfile, company_user=request.user)
        serializer = CompanyProfileSerializer(company_profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    
