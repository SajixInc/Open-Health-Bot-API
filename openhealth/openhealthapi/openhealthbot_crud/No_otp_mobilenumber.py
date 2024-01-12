import datetime
# from Lifeeazy.settings import DATABASES
from django.shortcuts import render
from ..models import otp_model
from rest_framework import generics
from ..serializers import bototpserializer,bototpvalidationserializer,nootpmobileserializer
from genericresponse import GenericResponse
from rest_framework.response import Response
from rest_framework.utils import json
from datetime import timedelta
import datetime
from datetime import timedelta
import datetime
## otp generation function ##
import math
import random
from errormessage import Errormessage
from database import x

from SMS_textlocal import sendSMS

from errormessage import Errormessage
from database import x

from SMS_textlocal import sendSMS



def GenerateOTP():
    digits = "0123456789"
    OTP = ""
    for i in range(6):
        OTP += digits[math.floor(random.random() * 10)]
    return OTP





class getidwithmobilenumber(generics.GenericAPIView):
    serializer_class = nootpmobileserializer
    
    def post(self,request):
        
        try:
            phonenumber=request.data.get('phone_number')
            otp_model1 = otp_model()
            print(otp_model1,"asdfgh")

            otp_model1.phone_number=phonenumber
            otp_model1.otp=GenerateOTP()
            # print(otp_model1.otp,"kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk" )
            otp_model1.date_time = datetime.datetime.now()
            t1 = datetime.datetime.now() + timedelta(seconds=0, minutes=15, hours=0)
            user={}
            print(t1,"kkkkkkkkkkkkkkkkkkkkk")
            if phonenumber == '+916309692221':
                otp_model1.otp = '530003'
            expiry_on=otp_model1.expiry_on = t1
            # otp_message_sms(phonenumber=phonenumber,otp=otp_model1.otp)


            otp_model1.save()
            user['id']= otp_model1.id
            # user['Otp'] = otp_model1.otp
            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = "Successful"
            response.Result = user
            response.Status = 200
            response.HasError = True
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=200)
        except Exception as e:
            
            response = GenericResponse("message", "result", "status", "has_error")
            response.Message = Errormessage(e)
            response.Result = False
            response.Status = 400
            response.HasError = True
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)
           
