from rest_framework.test import APITestCase
from django.urls import reverse
from accountio.models import  CustomUser
from companyio.models import CompanyProfile, Department




def create_department(company_user):

    company = CompanyProfile.objects.create(
        company_user = company_user,
        name = "repliq",
        email = "repliq@example.com",
        phone_number = "+8801772115060",
        address = "Dhaka, BD",
        description = "Something"
        )
    
    department = Department.objects.create(
        name = "Development",
        description = "Something",
        company = company
        )
    
    return department
    


def detail_department(uuid):
    return reverse('department:department-detail',args=[uuid])


def update_department(uuid):
    return reverse('department:department-update',args=[uuid])


def delete_department(uuid):
    return reverse('department:department-delete',args=[uuid])


class DepartmentTestcases(APITestCase):
    """Test for Department APIs"""
    DEPARTMENT_CREATE_URL = reverse('department:department-create')
    DEPARTMENT_LIST_URL = reverse('department:department-list')
    
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
        

    def test_department_create(self):
        """Test department Create."""
        CompanyProfile.objects.create(
            company_user = self.company_user,
            name = "repliq",
            email = "repliq@example.com",
            phone_number = "+8801772115060",
            address = "Dhaka, BD",
            description = "Something"
            )
        payload = {
            "name": "Development",
            "description": "Something"
            }

        response = self.client.post(self.DEPARTMENT_CREATE_URL, payload)

        response_data = {
            "name": response.data['name'],
            "description": response.data['description']
            }

        expected_data = {
            "name": "Development",
            "description": "Something"
            }

        self.assertEqual(response.status_code, 201)
        self.assertEqual(expected_data, response_data)

    def test_department_detail(self):
        """Test department Detail"""
        
        dep = create_department(self.company_user)
        response = self.client.get(detail_department(dep.uuid))

        expected_data = {
            "uuid": f"{response.data['uuid']}",
            "name": "Development",
            "description": "Something"
        }
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, expected_data)

    def test_department_update(self):
        """Test department Update."""
        department = create_department(self.company_user)

        payload = {
            'name': 'updated repliq',
        }
        
        response = self.client.put(update_department(department.uuid), payload)
        department.refresh_from_db()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], department.name)

    def test_department_remove(self):
            """Test department remove."""
            department = create_department(self.company_user)

            response = self.client.delete(delete_department(department.uuid))
            self.assertEqual(response.status_code, 204)