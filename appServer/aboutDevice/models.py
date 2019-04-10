#coding=utf-8
from django.db import models
from django.utils import timezone
import time

# Create your models here.
class Device(models.Model):
    """
    Description: Model Description
    """
    mac = models.CharField(max_length=32,unique=True)
    name = models.CharField(max_length=64,default='',blank=True)
    model = models.CharField(max_length=32,default='',blank=True)
    ownModel = models.CharField(max_length=32,default='',blank=True)
    sn = models.CharField(max_length=64,default='',blank=True)
    lastIP = models.GenericIPAddressField(default='0.0.0.0',blank=True,null=True)
    privateIP = models.GenericIPAddressField(default='0.0.0.0',blank=True,null=True)
    version = models.CharField(max_length=64,default='',blank=True)
    # lastHeartTime = models.DateTimeField(default=timezone.now)
    lastHeartTime = models.CharField(max_length=128,blank=True,default=int(time.time()))
    state = models.CharField(max_length=32,default='',blank=True)
    upload = models.BigIntegerField(default=0)
    download = models.BigIntegerField(default=0)

    accountName = models.CharField(max_length=64,default='',blank=True)
    supportMode = models.CharField(max_length=32,default='AP',blank=True)
    deviceMode = models.CharField(max_length=32,default='fitAP',blank=True)

    apUserNum = models.IntegerField(default=0,blank=True)
    guestsNum = models.IntegerField(default=0,blank=True)

    class Meta:
        indexes = [
            models.Index(fields = ['mac']),
        ]

class DeviceRadiosConfigs(models.Model):
    """
    Description: Model Description
    """
    device = models.OneToOneField(Device,on_delete=models.CASCADE,related_name='deviceRadiosConfigs')
    radiosType = models.CharField(u'射频类型',max_length=32,default='both',blank=True)
    radios2Channel = models.CharField(u'2g信道',max_length=32,default='auto',blank=True)
    radios2Ht = models.CharField(u'2ght',max_length=32,default='auto',blank=True)
    radios2Power = models.CharField(u'2gpower',max_length=32,default='auto',blank=True)
    radios2Com = models.CharField(u'2gcom',max_length=32,default='auto',blank=True)
    radios5Channel = models.CharField(u'5g信道',max_length=32,default='auto',blank=True)
    radios5Ht = models.CharField(u'5ght',max_length=32,default='auto',blank=True)
    radios5Power = models.CharField(u'5gpower',max_length=32,default='auto',blank=True)
    radios5Com = models.CharField(u'5gcom',max_length=32,default='auto',blank=True)
    # radios2Currstanum = models.IntegerField(u'2g当前用户数',default=0,blank=True)
    # radios2Guestsnum = models.IntegerField(u'2g来宾数量',default=0,blank=True)
    # radios5Currstanum = models.IntegerField(u'5g当前用户数',default=0,blank=True)
    # radios5Guestsnum = models.IntegerField(u'5g来宾数量',default=0,blank=True)


    class Meta:
        pass

class DeviceWlanConfigs(models.Model):
    """
    Description: Model Description
    """
    device = models.ForeignKey(Device,on_delete=models.CASCADE,related_name='deviceWlanConfigs')
    wlanID = models.CharField(max_length=32,default='0',blank=True)
    wlanSSID = models.CharField(max_length=64,default='',blank=True)
    wlanService = models.CharField(max_length=32,default='on',blank=True)
    passPhrase = models.CharField(max_length=64,default='',blank=True)
    radiosEnable = models.CharField(max_length=32,default='both',blank=True)


    class Meta:
        pass

class DeviceCommonConfig(models.Model):
    """
    Description: Model Description
    """
    device = models.OneToOneField(Device,on_delete=models.CASCADE,related_name='deviceCommonConfig')
    acAddress = models.CharField(max_length=128,default='',blank=True)
    networkSettingProtocol = models.CharField(max_length=32,default='DHCP',blank=True)
    PPPOEUsername = models.CharField(max_length=64,default='',blank=True)
    PPPOEPasswd = models.CharField(max_length=64,default='',blank=True)
    IpAddress = models.CharField(max_length=64,default='',blank=True)
    netMask = models.CharField(max_length=32,default='',blank=True)
    gateWay = models.CharField(max_length=32,default='',blank=True)
    mainDNSServer = models.CharField(max_length=32,default='',blank=True)
    spareDNSServer = models.CharField(max_length=32,default='',blank=True)

    class Meta:
        pass
