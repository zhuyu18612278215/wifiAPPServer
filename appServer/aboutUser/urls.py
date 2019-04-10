#coding=utf-8
from .views import UserViewSet,UserOtherInfoViewSet,ACAccountViewSet,ACInfoViewSet,ACAccountBindInfoViewSet,EmailVerifyCodeViewSet
from rest_framework.routers import DefaultRouter

userRouter = DefaultRouter()
userRouter.register(r'User',UserViewSet,base_name = 'user')
userRouter.register(r'UserOtherInfo',UserOtherInfoViewSet,base_name = 'userOtherInfo')
userRouter.register(r'ACAccount',ACAccountViewSet,base_name = 'acAccount')
userRouter.register(r'ACInfo',ACInfoViewSet,base_name = 'acInfo')
userRouter.register(r'ACAccountBindInfo',ACAccountBindInfoViewSet,base_name = 'acAccountBindInfo')
userRouter.register(r'EmailVerifyCode',EmailVerifyCodeViewSet,base_name = 'emailVerifyCode')
