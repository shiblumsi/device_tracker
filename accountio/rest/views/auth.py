from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from django.contrib.auth import authenticate, login
from rest_framework_simplejwt.tokens import RefreshToken
from drf_spectacular.utils import  extend_schema

from accountio.rest.serializers.auth import CompanyRegistrationSerializer, LoginSerializer



def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class CompanyRegistrationView(APIView):
    @extend_schema(request=CompanyRegistrationSerializer)
    def post(self, request):
        serializer = CompanyRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = get_tokens_for_user(user)
            return Response({'Token': token, 'serializer':serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    @extend_schema(request=LoginSerializer)
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.data['username']
            password = serializer.data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                token = get_tokens_for_user(user)
                login(request, user)
                return Response({'Token': token,'serializer':serializer.data}, status=status.HTTP_200_OK)
        return Response({"Error": "Username or Password is not valid!!!"}, status=status.HTTP_400_BAD_REQUEST)


