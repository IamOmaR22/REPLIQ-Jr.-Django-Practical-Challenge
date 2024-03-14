from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Company, Employee, Device, DeviceLog


class DeviceTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.force_authenticate(user=self.user)
        self.company = Company.objects.create(name='Test Company', description='A test company')
        self.employee = Employee.objects.create(user=self.user, company=self.company)
        self.device = Device.objects.create(
            name='Test Device',
            serial_number='123456',
            description='A test device',
            company=self.company,
        )

    def test_device_check_out(self):
        # Create a DeviceLogSerializer data with a properly formatted datetime
        data = {
            'device': self.device.id,
            'checked_out_by': self.employee.id,
            'checked_out_date': '2024-03-14T10:00:00Z',  # Properly formatted datetime
            'condition': 'Good condition',
        }
        response = self.client.post(f'/devices/{self.device.id}/check_out/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(Device.objects.get(id=self.device.id).is_checked_out)

    def test_device_check_in(self):
        self.device.is_checked_out = True
        self.device.save()

        response = self.client.post(f'/devices/{self.device.id}/check_in/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(Device.objects.get(id=self.device.id).is_checked_out)
