from rest_framework.test import APITestCase
from django.urls import reverse


class AuthenticationTestcases(APITestCase):
    """Test for superuser Register API"""
    REGISTRATION_URL = reverse('auth:company-registration')
    LOGIN_URL = reverse('auth:company-login')


    def test_user_registration(self):
        """Test User Registration"""
        payload = {
            "username": "user1",
            "email": "user@gmail.com",
            "password": "123456789Aas",
            "password2": "123456789Aas"
        }

        response = self.client.post(self.REGISTRATION_URL, payload)
        
        response_data = {
            "username": response.data['serializer']['username'],
            "email": response.data['serializer']['email']
        }

        expected_data = {
            "username": "user1",
            "email": "user@gmail.com",
        }
        
        self.assertEqual(response.status_code, 201)
        self.assertEqual(expected_data, response_data)



    def test_user_login(self):
        """Test User Login"""

        registration_payload = {
            "username": "user1",
            "email": "user@gmail.com",
            "password": "123456789Aas",
            "password2": "123456789Aas"
        }
        self.client.post(self.REGISTRATION_URL, registration_payload)
        

        login_payload = {
            "username": "user1",
            "password": "123456789Aas"
        }

        response = self.client.post(self.LOGIN_URL, login_payload)
        response_data = {
            "username": response.data['serializer']['username']
        }

        expected_data = {
            "username": "user1"
        }
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(expected_data, response_data)
