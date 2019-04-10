#coding=utf-8
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserOtherInfo,ACAccount,ACInfo,ACAccountBindInfo,EmailVerifyCode

class UserSerializer(serializers.HyperlinkedModelSerializer):
    userOtherInfo = serializers.HyperlinkedRelatedField(read_only = True,view_name = 'userOtherInfo-detail')
    class Meta:
        model = User
        fields = ('username','email','password','userOtherInfo')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class UserOtherInfoSerializer(serializers.HyperlinkedModelSerializer):
    """docstring for UserOtherInfoSerializer"""

    class Meta:
        model = UserOtherInfo
        fields = ('user','phone','nickName','lastLoginIp','headPic')

class ACAccountSerializers(serializers.HyperlinkedModelSerializer):
    """docstring for ACAccountSerializers"""
    class Meta:
        model = ACAccount
        fields = ('acUsername','acAddress','acUserPassword','acUserPermission',)

class ACInfoSerializers(serializers.HyperlinkedModelSerializer):
    """docstring for ACInfoSerializers"""
    class Meta:
        model = ACInfo
        fields = ('acAddress','acPrivateAddress','acMac','acCPU','acMem','acDisk')

class ACAccountBindInfoSerializers(serializers.HyperlinkedModelSerializer):
    """docstring for ACAccountBindInfoSerializers"""
    class Meta:
        model = ACAccountBindInfo
        fields = ('bindUsername','bindACUsername','bindACAddress','bindACUserPassword',)
        extra_kwargs = {'bindACUserPassword': {'write_only': True}}

class EmailVerifyCodeSerializers(serializers.HyperlinkedModelSerializer):
    """docstring for EmailVerifyCodeSerializers"""
    class Meta:
        model = EmailVerifyCode
        fields = ('code','email','sendType','sendTime')


