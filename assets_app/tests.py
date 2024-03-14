from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Company, Employee, Device, DeviceLog, Subscription
from .serializers import CompanySerializer, EmployeeSerializer, DeviceSerializer, DeviceLogSerializer
from datetime import datetime
from datetime import timedelta


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


class SubscriptionTestCase(APITestCase):
    def setUp(self):
        self.company = Company.objects.create(name='Test Company', description='Test Description')
        self.subscription = Subscription.objects.create(
            company=self.company,
            plan='Basic Plan',
            price=10.00,
            start_date=datetime.now().date(),
            end_date=datetime.now().date() + timedelta(days=30)
        )

    def test_subscription_creation(self):
        self.assertEqual(self.subscription.company.name, 'Test Company')
        self.assertEqual(self.subscription.plan, 'Basic Plan')
        self.assertEqual(self.subscription.price, 10.00)
        self.assertTrue(self.subscription.start_date <= self.subscription.end_date)

    def test_subscription_update(self):
        new_plan = 'Premium Plan'
        new_price = 20.00
        self.subscription.plan = new_plan
        self.subscription.price = new_price
        self.subscription.save()
        self.subscription.refresh_from_db()
        self.assertEqual(self.subscription.plan, new_plan)
        self.assertEqual(self.subscription.price, new_price)

    def test_subscription_deletion(self):
        subscription_id = self.subscription.id
        self.subscription.delete()
        with self.assertRaises(Subscription.DoesNotExist):
            Subscription.objects.get(pk=subscription_id)

    def test_subscription_str(self):
        expected_str = f"{self.company.name} - Plan: {self.subscription.plan}"
        self.assertEqual(str(self.subscription), expected_str)

