from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from datetime import datetime
from .models import Company, Employee, Device, DeviceLog
from .serializers import CompanySerializer, EmployeeSerializer, DeviceSerializer, DeviceLogSerializer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

    @action(detail=True, methods=['post'])
    def check_out(self, request, pk=None):
        device = self.get_object()
        serializer = DeviceLogSerializer(data=request.data)
        if serializer.is_valid():
            checked_out_by = Employee.objects.get(user=request.user)
            serializer.save(device=device, checked_out_by=checked_out_by)
            device.is_checked_out = True
            device.checked_out_by = checked_out_by
            device.checked_out_date = serializer.validated_data['checked_out_date']
            device.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'])
    def check_in(self, request, pk=None):
        device = self.get_object()
        device.is_checked_out = False
        device.checked_in_date = datetime.now()
        device.save()
        return Response({'message': 'Device checked in successfully'}, status=status.HTTP_200_OK)

class DeviceLogViewSet(viewsets.ModelViewSet):
    queryset = DeviceLog.objects.all()
    serializer_class = DeviceLogSerializer
