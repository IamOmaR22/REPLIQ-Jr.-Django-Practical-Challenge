from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet, EmployeeViewSet, DeviceViewSet, DeviceLogViewSet, SubscriptionViewSet

router = DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'devices', DeviceViewSet)
router.register(r'devicelogs', DeviceLogViewSet)
router.register(r'subscriptions', SubscriptionViewSet)

urlpatterns = router.urls


# The following API Endpoints are available:
# 
# /companies/ - GET, POST
# /companies/{id}/ - GET, PUT, DELETE
# /employees/ - GET, POST
# /employees/{id}/ - GET, PUT, DELETE
# /devices/ - GET, POST
# /devices/{id}/ - GET, PUT, DELETE
# /devicelogs/ - GET, POST
# /devicelogs/{id}/ - GET, PUT, DELETE
# /devices/{id}/check_out/ - POST
# /devices/{id}/check_in/ - POST
# /subscriptions/ - GET, POST
# /subscriptions/{id}/ - GET, PUT, DELETE
#
# The API is now complete and ready for use. You can test the API using the Django admin interface or by using the Django REST framework's browsable API. 
#You can also use the Swagger or ReDoc UIs to test the API. I implemented swagger and redoc in the asset_tracker/urls.py file.
# Endpoints for the API are as follows:
#
# /admin/ - Django admin interface
# /companies/ - List of companies
# /employees/ - List of employees
# /devices/ - List of devices
# /devicelogs/ - List of device logs
# /subscriptions/ - List of subscriptions
# /swagger/ - Swagger UI
# /redoc/ - ReDoc UI
#
# You can access the API using the following URLs:
#
# http://localhost:8000/admin/
# http://localhost:8000/companies/
# http://localhost:8000/employees/
# http://localhost:8000/devices/
# http://localhost:8000/devicelogs/
# http://localhost:8000/subscriptions/
# http://localhost:8000/swagger/
# http://localhost:8000/redoc/
