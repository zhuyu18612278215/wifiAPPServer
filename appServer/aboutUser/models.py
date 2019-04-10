#coding=utf-8
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.contrib.auth.models import User
import time

# Create your models here.

class UserOtherInfo(models.Model):
    """
    Description: Model Description
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='userOtherInfo')
    phone = models.CharField(max_length=20,blank=True,default='')
    nickName = models.CharField(max_length=32,blank=True,default='')
    lastLoginIp = models.GenericIPAddressField(default='0.0.0.0')
    headPic = models.ImageField(upload_to='photos/%Y/%m/%d',max_length=128,default=u"photos/headimg.png",blank=True)





class ACAccount(models.Model):
    """
    Description: Model Description
    """
    acUsername = models.CharField(max_length=64)
    acAddress = models.CharField(max_length=128)
    acUserPassword = models.CharField(max_length=128)
    acUserPermission = models.CharField(max_length=32)
    isDelete = models.BooleanField(default=False)
    # 只允许管理域创建者的account
    class Meta:
        unique_together = ('acUsername','acAddress')
        indexes = [
            models.Index(fields = ['acUsername','acAddress',]),
        ]

    def __unicode__(self):
        return 'user:{0},address:{1}'.format(self.acUsername,self.acAddress)

class ACInfo(models.Model):
    """
    Description: Model Description
    """
    acAddress = models.CharField(max_length=128,unique=True)
    acPrivateAddress = models.CharField(max_length=128)
    acMac = models.CharField(max_length=32)
    acCPU = models.CharField(max_length=32,blank=True,default='')
    acMem = models.CharField(max_length=32,blank=True,default='')
    acDisk = models.CharField(max_length=32,blank=True,default='')
    isDelete = models.BooleanField(default=False)

    class Meta:
        indexes = [
            models.Index(fields = ['acAddress',]),
        ]

    def __unicode__(self):
        return self.acAddress

class ACAccountBindInfo(models.Model):
    """
    Description: Model Description
    """
    bindUsername = models.CharField(max_length=128,unique=True)
    bindACUsername = models.CharField(max_length=128)
    bindACAddress = models.CharField(max_length=128)
    bindACUserPassword = models.CharField(max_length=128)
    isDelete = models.BooleanField(default=False)


    class Meta:
        indexes = [
             models.Index(fields = ['bindUsername']),
        ]

class EmailVerifyCode(models.Model):
    """
    Description: Model Description
    """
    code = models.CharField(max_length=64,default = '')
    email = models.CharField(max_length=64,default = '')
    sendType = models.CharField(max_length=32,default = '')
    sendTime = models.CharField(max_length=64,default = str(int(time.time())) )
    expirationTime = models.CharField(max_length=64, default = str(int(time.time()) + 86400))
    isUsed = models.BooleanField(default = False)
    class Meta:
        unique_together = ('email','sendType')
        indexes = [
            models.Index(fields = ['email','sendType']),
        ]
