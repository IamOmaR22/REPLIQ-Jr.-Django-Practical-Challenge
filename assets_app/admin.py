from django.contrib import admin

# Register your models here.
from .models import Company, Employee, Device, DeviceLog, Subscription
admin.site.register(Company)
admin.site.register(Employee)
admin.site.register(Device)
admin.site.register(DeviceLog)
admin.site.register(Subscription)
