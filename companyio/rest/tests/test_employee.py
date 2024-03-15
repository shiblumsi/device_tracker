from rest_framework.test import APITestCase
from django.urls import reverse
from accountio.models import  CustomUser
from companyio.models import Department, Employee, CompanyProfile



def create_employee(company_user):

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
    
    employee = Employee.objects.create(
        name = "shiblu",
        position = "S.E",
        email = "s@gmail.com",
        phone_number = "01772115060",
        department = department,
        company = company
    )
    
    return employee
    


def detail_employee(uuid):
    return reverse('employee:employee.detail.update.destroy',args=[uuid])



class EmployeeTestcases(APITestCase):
    """Test for employee APIs"""
    EMPLOYEE_CREATE_URL = reverse('employee:employee-create')
    
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
        

    def test_employee_create(self):
        """Test employee Create."""
        department = Department.objects.create(
        name = "Development",
        description = "Something",
        )
        payload = {
            "name" :"shiblu",
            "position" : "S.E",
            "email" : "s@gmail.com",
            "phone_number" : "01772115060",
            "department" : department,
            }

        response = self.client.post(self.EMPLOYEE_CREATE_URL, payload)
        response_data = {
            "name" :response.data['name'],
            "position" : response.data["S.E"],
            "email" : response.data["s@gmail.com"],
            "phone_number" : response.data["01772115060"],
            
            }
            

        expected_data = {
            "name" :"shiblu",
            "position" : "S.E",
            "email" : "s@gmail.com",
            "phone_number" : "01772115060",
           
            }

        self.assertEqual(response.status_code, 201)
        self.assertEqual(expected_data, response_data)

    def test_employee_detail(self):
        """Test employee Detail"""
        
        employee = create_employee(self.company_user)
        response = self.client.get(detail_employee(employee.uuid))

        expected_data = {
            "uuid": f"{response.data['uuid']}",
            "name" :"shiblu",
            "position" : "S.E",
            "email" : "s@gmail.com",
            "phone_number" : "01772115060",
            "department": response.data['department']
            
        }
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, expected_data)



    