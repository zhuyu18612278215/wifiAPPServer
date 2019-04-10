#coding=utf-8from django.shortcuts import renderfrom rest_framework import viewsets,statusfrom .serializers import UserSerializer,UserOtherInfoSerializer,ACAccountSerializers,ACInfoSerializers,ACAccountBindInfoSerializers,EmailVerifyCodeSerializersfrom .models import UserOtherInfo,ACAccount,ACInfo,ACAccountBindInfo,EmailVerifyCodefrom django.contrib.auth.models import Userfrom rest_framework.decorators import action,permission_classesfrom rest_framework.response import Responsefrom rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUserfrom random import Random # 用于生成随机码from django.core.mail import send_mail # 发送邮件模块from appServer.settings import EMAIL_HOST_USERimport time,stringfrom django.db.models import Q# Create your views here.class UserViewSet(viewsets.ModelViewSet):    """docstring for DeviceViewSet"""    queryset = User.objects.all()    serializer_class = UserSerializer    # permission_classes = (IsAdminUser,)    def get_permissions(self):        """        Instantiates and returns the list of permissions that this view requires.        """        if self.action == 'create' or self.action == 'fixPassWD':            permission_classes = [AllowAny]        elif self.action == 'getOwnDetailInfo':            permission_classes = [IsAuthenticated]        else:            permission_classes = [IsAdminUser]        return [permission() for permission in permission_classes]    def create(self, request, *args, **kwargs):        #add        checkResult = {'result':False,'detail':'unknownError'}        if request.data['registerCodeType'] == 'emailCode':            checkResult = self.checkEmailCode(request)        if User.objects.filter(username = request.data['username']).exists():            checkResult = {'result':False,'detail':'userExists'}        if not checkResult['result']:            return Response({'status':'checkError','detail':checkResult['detail']},status = status.HTTP_400_BAD_REQUEST)        # old        serializer = self.get_serializer(data=request.data)        # print (serializer,serializer.data)        serializer.is_valid(raise_exception=True)        self.perform_create(serializer)        headers = self.get_success_headers(serializer.data)        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)    def perform_create(self, serializer):        # print (serializer.validated_data)        # pass        serializer.save()    def checkEmailCode(self,request):        emailCode = (request.data['emailCode']).upper()        # print (emailCode)        email = request.data['email']        sendType = request.data['sendType']        # print (str(int(time.time())))        if EmailVerifyCode.objects.filter(email = email,sendType = sendType,code = emailCode,expirationTime__gte = str(int(time.time())),isUsed = False).exists():            emailVerifyCode = EmailVerifyCode.objects.get(email = email,sendType = sendType,code = emailCode,expirationTime__gte = str(int(time.time())),isUsed = False)            emailVerifyCode.isUsed = True            emailVerifyCode.save()            return {'result':True,'detail':'checkSuccess'}        else:            return {'result':False,'detail':'codeError'}    @action(detail = False,methods = ['post'],permission_classes = [AllowAny])    def fixPassWD(self,request):        checkResult = {'result':False,'detail':'unknownError'}        if request.data['registerCodeType'] == 'emailCode':            checkResult = self.checkEmailCode(request)        if not User.objects.filter(username = request.data['username']).exists():            checkResult = {'result':False,'detail':'userUnExists'}        if not checkResult['result']:            return Response({'status':'checkError','detail':checkResult['detail']},status = status.HTTP_400_BAD_REQUEST)        user = User.objects.get(username = request.data['username'])        user.set_password(request.data['password'])        user.save()        return Response({'status':'fixPassWDSuccess'})    @action(detail = False,methods = ['get'],permission_classes = [IsAuthenticated])    def getOwnDetailInfo(self,request):        serializer = self.get_serializer(instance = request.user)        return Response(serializer.data)class UserOtherInfoViewSet(viewsets.ModelViewSet):    """docstring for DeviceViewSet"""    queryset = UserOtherInfo.objects.all()    serializer_class = UserOtherInfoSerializerclass ACAccountViewSet(viewsets.ModelViewSet):    """docstring for DeviceViewSet"""    queryset = ACAccount.objects.all()    serializer_class = ACAccountSerializersclass ACInfoViewSet(viewsets.ModelViewSet):    """docstring for DeviceViewSet"""    queryset = ACInfo.objects.all()    serializer_class = ACInfoSerializersclass ACAccountBindInfoViewSet(viewsets.ModelViewSet):    """docstring for DeviceViewSet"""    queryset = ACAccountBindInfo.objects.all()    serializer_class = ACAccountBindInfoSerializers    def get_permissions(self):        """        Instantiates and returns the list of permissions that this view requires.        """        if self.action == 'getOwnBindACInfo' or self.action == 'bindAC':            permission_classes = [IsAuthenticated]        else:            permission_classes = [IsAdminUser]        return [permission() for permission in permission_classes]    @action(detail = False,methods = ['get'],permission_classes = [IsAuthenticated])    def getOwnBindACInfo(self,request):        if ACAccountBindInfo.objects.filter(bindUsername = request.user.username,isDelete = False).exists():            instance = ACAccountBindInfo.objects.get(bindUsername = request.user.username,isDelete = False)            serializer = self.get_serializer(instance = instance)            return Response(serializer.data)        else:            return Response({})    @action(detail = False,methods = ['post'],permission_classes = [IsAuthenticated])    def bindAC(self,request):        checkResult = {'result':False,'detail':'unknownError'}        if ACAccountBindInfo.objects.filter(Q(bindUsername = request.user.username,isDelete = False)|Q(bindACUsername = request.data['bindACUsername'],bindACAddress = request.data['bindACAddress'],isDelete = False)).exists():            checkResult = {'result':False,'detail':'bindExists'}        elif not ACAccount.objects.filter(acAddress = request.data['bindACAddress'],acUsername = request.data['bindACUsername'],acUserPassword = request.data['bindACUserPassword']).exists():            checkResult = {'result':False,'detail':'ACInfoNotExists'}        if not checkResult['result']:            return Response({'status':'checkError','detail':checkResult['detail']},status = status.HTTP_400_BAD_REQUEST)        info = ACAccountBindInfo()        info.bindUsername = request.user.username        info.bindACUsername = request.data['bindACUsername']        info.bindACAddress = request.data['bindACAddress']        info.bindACUserPassword = request.data['bindACUserPassword']        info.isDelete = False        info.save()        serializer = self.get_serializer(instance = info)        return Response({'status':'bindSuccess','data':serializer.data})class EmailVerifyCodeViewSet(viewsets.ModelViewSet):    """docstring for ClassName"""    queryset = EmailVerifyCode.objects.all()    serializer_class = EmailVerifyCodeSerializers    # 生成随机字符串    def randomStr(self,codelength=6):        code = ''        chars = string.ascii_uppercase + string.digits        length = len(chars) - 1        random = Random()        for i in range(codelength):            code += chars[random.randint(0, length)]        return code.upper()    def sendMail(self,email,sendType):        code = (self.randomStr(6)).upper()        emailTitle = u'APP邮件验证码'        emailBody = ''        sendResult = 0        # if sendType == 'register':        emailBody = '<p>尊敬的用户您好</p><p>您本次的邮件验证码为:</p><p><h1>{code}</h1></p><p>本验证码有效期为24小时</p>'.format(code = code)        sendResult = send_mail(subject = emailTitle, message = emailBody, from_email = EMAIL_HOST_USER, recipient_list = [email],html_message = emailBody,fail_silently = True)        if sendResult:            if EmailVerifyCode.objects.filter(email = email,sendType = sendType).exists():                emailVerifyCode = EmailVerifyCode.objects.get(email = email,sendType = sendType)            else:                emailVerifyCode = EmailVerifyCode()            emailVerifyCode.code = code            emailVerifyCode.email = email            emailVerifyCode.sendType = sendType            emailVerifyCode.sendTime = str(int(time.time()))            emailVerifyCode.expirationTime = str(int(time.time()) + 86400)            emailVerifyCode.isUsed = False            emailVerifyCode.save()        return sendResult    @action(detail = False,methods = ['post'],permission_classes = [AllowAny])    def applyEmailVerifyCode(self,request):        data = request.data        if 'email' in data and 'sendType' in data:            result = self.sendMail(data['email'],data['sendType'])            if result:                return Response({'status':'sendSuccess'})        return Response({'status':'sendFail'},status = status.HTTP_400_BAD_REQUEST)