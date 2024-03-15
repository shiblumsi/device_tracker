from rest_framework.test import APITestCase
from django.urls import reverse
from accountio.models import CustomUser
from deviceio.models import  Device
from companyio.models import CompanyProfile



def create_device(company_user):

    company = CompanyProfile.objects.create(
        company_user = company_user,
        name = "repliq",
        email = "repliq@example.com",
        phone_number = "+8801772115060",
        address = "Dhaka, BD",
        description = "Something"
        )
    
    
    device = Device.objects.create(
        name = "S23",
        configuration = "12gb RAM",
        condition = "Full Fresh",
        status = "AV",
        device_type = "Phone",
        company = company
    )
    
    return device
    


def detail_device(uuid):
    return reverse('device:device.detail.update.destroy',args=[uuid])



class DeviceTestcases(APITestCase):
    """Test for device APIs"""
    DEVICE_CREATE_URL = reverse('device:device-create')
    
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
        

    def test_device_create(self):
        """Test device Create."""
        
        payload = {
            "name" : "S23",
            "configuration" : "12gb RAM",
            "condition" : "Full Fresh",
            "status" : "AV",
            "device_type" : "OTHER"
        
            }

        response = self.client.post(self.DEVICE_CREATE_URL, payload)

        response_data = {
             "name": response.data['name'],
            "configuration" : response.data["configuration"],
            "condition" : response.data["condition"],
            "status" : response.data["status"],
            "device_type" : response.data['device_type']
            }
            

        expected_data = {
            "name" : "S23",
            "configuration" : "12gb RAM",
            "condition" : "Full Fresh",
            "status" : "AV",
            "device_type" : "Phone"
            }

        self.assertEqual(response.status_code, 201)
        self.assertEqual(expected_data, response_data)

    def test_device_detail(self):
        """Test device Detail"""
        
        device = create_device(self.company_user)
        response = self.client.get(detail_device(device.uuid))

        expected_data = {
            "uuid": f"{response.data['uuid']}",
            "name" : "S23",
            "configuration" : "12gb RAM",
            "condition" : "Full Fresh",
            "status" : "AV",
            "device_type" : "Phone"
            
        }
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, expected_data)



    