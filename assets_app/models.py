from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Device(models.Model):
    name = models.CharField(max_length=255)
    serial_number = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    is_checked_out = models.BooleanField(default=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    checked_out_by = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)
    checked_out_date = models.DateTimeField(null=True, blank=True)
    checked_in_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

class DeviceLog(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    checked_out_by = models.ForeignKey(Employee, on_delete=models.CASCADE)
    checked_out_date = models.DateTimeField()
    checked_in_date = models.DateTimeField(null=True, blank=True)
    condition = models.TextField()

    def __str__(self):
        return f"{self.device.name} - Checked Out by: {self.checked_out_by.user.username}"
