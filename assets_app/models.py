from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

class Device(models.Model):
    name = models.CharField(max_length=255)
    serial_number = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    condition_log = models.JSONField(default=list)
    is_checked_out = models.BooleanField(default=False)
    checked_out_by = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)
    checked_out_date = models.DateTimeField(null=True, blank=True)
    checked_in_date = models.DateTimeField(null=True, blank=True)

class DeviceLog(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    checked_out_by = models.ForeignKey(Employee, on_delete=models.CASCADE)
    checked_out_date = models.DateTimeField()
    checked_in_date = models.DateTimeField(null=True, blank=True)
    condition = models.JSONField()
