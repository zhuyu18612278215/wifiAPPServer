#coding=utf-8
from rest_framework import serializers
from .models import Device,DeviceWlanConfigs,DeviceRadiosConfigs,DeviceCommonConfig


class DeviceSerializer(serializers.HyperlinkedModelSerializer):
    deviceRadiosConfigs = serializers.HyperlinkedRelatedField(read_only = True,view_name = 'deviceRadiosConfigs-detail')
    deviceWlanConfigs = serializers.HyperlinkedRelatedField(read_only = True,many = True,view_name = 'deviceWlanConfigs-detail')
    deviceCommonConfig = serializers.HyperlinkedRelatedField(read_only = True,view_name = 'deviceCommonConfig-detail')

    class Meta:
        model = Device
        fields = ('pk','mac','name','model','ownModel','sn','lastIP','privateIP','version','lastHeartTime','state','upload','download','accountName','supportMode','deviceMode','apUserNum','guestsNum','deviceRadiosConfigs','deviceWlanConfigs','deviceCommonConfig')

class DeviceRadiosConfigsSerializer(serializers.HyperlinkedModelSerializer):
    """docstring for DeviceRadiosConfigsSerializer"""

    class Meta:
        model = DeviceRadiosConfigs
        fields = ('device','radiosType','radios2Channel','radios2Ht','radios2Power','radios2Com','radios5Channel','radios5Ht','radios5Power','radios5Com')

class DeviceWlanConfigsSerializer(serializers.HyperlinkedModelSerializer):
    """docstring for DeviceWlanConfigsSerializer"""

    class Meta:
        model = DeviceWlanConfigs
        fields = ('device','wlanID','wlanSSID','wlanService','passPhrase','radiosEnable')

class DeviceCommonConfigSerializer(serializers.HyperlinkedModelSerializer):
    """docstring for DeviceCommonConfigSerializer"""

    class Meta:
        model = DeviceCommonConfig
        fields = ('device','acAddress','networkSettingProtocol','PPPOEUsername','PPPOEPasswd','IpAddress','netMask','gateWay','mainDNSServer','spareDNSServer')


