from rest_framework.test import APITestCase
from django.urls import reverse
from accountio.models import CompanyProfile, CustomUser


class CompanyProfileTestcases(APITestCase):
    """Test for Company Profile APIs"""
    COMPANY_PROFILE_CREATE_URL = reverse('company:company-profile-create')
    COMPANY_PROFILE_DETAIL_URL = reverse('company:company-profile-detail')
    COMPANY_PROFILE_UPDATE_URL = reverse('company:company-profile-update')

    def setUp(self) -> None:
        LOGIN_URL = reverse('auth:company-login')
        self.company_user = CustomUser.objects.create_organization(
            username= "user1",
            email = "user@gmail.com",
            password  =  "123456789Aas",
        )

        login_payload = {
            "username": "user1",
            "password": "123456789Aas"
        }

        res = self.client.post(LOGIN_URL, login_payload, format="json")
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + res.data['Token']['access'])
        

    def test_company_profile_create(self):
        """Test Company Profile Create."""
        payload = {
            "name": "repliq",
            "email": "repliq@example.com",
            "phone_number": "+8801772115060",
            "address": "Dhaka,BD",
            "description": "Nothing"
            }

        response = self.client.post(self.COMPANY_PROFILE_CREATE_URL, payload)

        response_data = {
            "name": response.data['name'],
            "email": response.data['email'],
            "phone_number": response.data['phone_number'],
            "address": response.data['address'],
            "description": response.data['description'],
        }

        expected_data = {
            "name": "repliq",
            "email": "repliq@example.com",
            "phone_number": "+8801772115060",
            "address": "Dhaka,BD",
            "description": "Nothing"
        }

        self.assertEqual(response.status_code, 201)
        self.assertEqual(expected_data, response_data)

    def test_company_profile_detail(self):
        """Test Company Profile Detail"""
        
        CompanyProfile.objects.create(
            company_user=self.company_user,
            name="repliq",
            email="repliq@example.com",
            phone_number="+8801772115060",
            address="Dhaka, BD",
            description="Nothing"
        )

        response = self.client.get(self.COMPANY_PROFILE_DETAIL_URL)

        expected_data = {
            "name": "repliq",
            "email": "repliq@example.com",
            "phone_number": "+8801772115060",
            "address": "Dhaka, BD",
            "description": "Nothing"
        }
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, expected_data)

    def test_update_category(self):
        """Test Company Profile Update."""
        company_profile = CompanyProfile.objects.create(
            company_user=self.company_user,
            name="repliq",
            email="repliq@example.com",
            phone_number="+8801772115060",
            address="Dhaka, BD",
            description="Nothing"
        )

        payload = {
            'name': 'updated repliq',
        }
        
        response = self.client.put(self.COMPANY_PROFILE_UPDATE_URL, payload)
        company_profile.refresh_from_db()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], company_profile.name)