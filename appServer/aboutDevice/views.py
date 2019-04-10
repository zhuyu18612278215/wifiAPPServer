#coding=utf-8
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import DeviceSerializer,DeviceRadiosConfigsSerializer,DeviceWlanConfigsSerializer,DeviceCommonConfigSerializer
from .models import Device,DeviceWlanConfigs,DeviceRadiosConfigs,DeviceCommonConfig

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser


# Create your views here.
class DeviceViewSet(viewsets.ModelViewSet):
    """docstring for DeviceViewSet"""
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = (IsAuthenticated,)

class DeviceRadiosConfigsViewSet(viewsets.ModelViewSet):
    """docstring for DeviceRadiosConfigsViewSet"""
    queryset = DeviceRadiosConfigs.objects.all()
    serializer_class = DeviceRadiosConfigsSerializer
    permission_classes = (IsAuthenticated,)

    # @action(detail = True,methods = ['patch'])
    # def partial_update(self, request, pk=None):
    #     print (self,request,pk)

class DeviceWlanConfigsViewSet(viewsets.ModelViewSet):
    """docstring for DeviceWlanConfigsViewSet"""
    queryset = DeviceWlanConfigs.objects.all()
    serializer_class = DeviceWlanConfigsSerializer
    permission_classes = (IsAuthenticated,)

class DeviceCommonConfigViewSet(viewsets.ModelViewSet):
    """docstring for DeviceCommonConfigViewSet"""
    queryset = DeviceCommonConfig.objects.all()
    serializer_class = DeviceCommonConfigSerializer
    permission_classes = (IsAuthenticated,)




