from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Company, Employee, Device, DeviceLog
from .serializers import CompanySerializer, EmployeeSerializer, DeviceSerializer, DeviceLogSerializer
from datetime import datetime

class DeviceViewSetTestCase(APITestCase):
    def setUp(self):
        self.company = Company.objects.create(name='Test Company', description='A test company')
        self.user = User.objects.create_user(username='testuser', password='password')
        self.employee = Employee.objects.create(user=self.user, company=self.company)
        self.device = Device.objects.create(name='Test Device', serial_number='123456', description='A test device', company=self.company)

    def test_device_check_out(self):
        self.client.force_login(self.user)
        data = {
            'device': self.device.id,
            'checked_out_by': self.employee.id,
            'checked_out_date': datetime.now().isoformat(),
            'condition': 'Good'
        }
        response = self.client.post(f'/devices/{self.device.id}/check_out/', data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.device.refresh_from_db()
        self.assertTrue(self.device.is_checked_out)
        self.assertEqual(self.device.checked_out_by, self.employee)

    def test_device_check_in(self):
        self.device.is_checked_out = True
        self.device.checked_out_by = self.employee
        self.device.save()

        self.client.force_login(self.user)
        response = self.client.post(f'/devices/{self.device.id}/check_in/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.device.refresh_from_db()
        self.assertFalse(self.device.is_checked_out)
        self.assertIsNone(self.device.checked_out_by)  # Ensure checked_out_by is None after check-in

class DeviceLogViewSetTestCase(APITestCase):
    def setUp(self):
        self.company = Company.objects.create(name='Test Company', description='A test company')
        self.user = User.objects.create_user(username='testuser', password='password')
        self.employee = Employee.objects.create(user=self.user, company=self.company)
        self.device = Device.objects.create(name='Test Device', serial_number='123456', description='A test device', company=self.company)
        self.device_log = DeviceLog.objects.create(device=self.device, checked_out_by=self.employee, checked_out_date=datetime.now(), condition='Good')

    def test_create_devicelog(self):
        self.client.force_login(self.user)
        data = {
            'device': self.device.id,
            'checked_out_by': self.employee.id,
            'checked_out_date': datetime.now().isoformat(),
            'condition': 'Good'
        }
        response = self.client.post('/devicelogs/', data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_devicelog_list(self):
        self.client.force_login(self.user)
        response = self.client.get('/devicelogs/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Assuming only one log is created

