#coding=utf-8
from .views import DeviceViewSet,DeviceRadiosConfigsViewSet,DeviceWlanConfigsViewSet,DeviceCommonConfigViewSet
from rest_framework.routers import DefaultRouter

deviceRouter = DefaultRouter()
deviceRouter.register(r'Device',DeviceViewSet,base_name = 'device')
deviceRouter.register(r'DeviceRadiosConfigs',DeviceRadiosConfigsViewSet,base_name = 'deviceRadiosConfigs')
deviceRouter.register(r'DeviceWlanConfigs',DeviceWlanConfigsViewSet,base_name = 'deviceWlanConfigs')
deviceRouter.register(r'DeviceCommonConfig',DeviceCommonConfigViewSet,base_name = 'deviceCommonConfig')
