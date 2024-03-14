from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet, EmployeeViewSet, DeviceViewSet, DeviceLogViewSet

router = DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'devices', DeviceViewSet)
router.register(r'devicelogs', DeviceLogViewSet)

urlpatterns = router.urls


# API Endpoints
# The following endpoints are available:
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
#
# The API is now complete and ready for use. You can test the API using the Django admin interface or by using the Django REST framework's browsable API. You can also use the Swagger or ReDoc UIs to test the API.
