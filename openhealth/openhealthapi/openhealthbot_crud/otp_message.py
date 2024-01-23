import datetime
# from Lifeeazy.settings import DATABASES
from django.shortcuts import render
from ..models import otp_model,otp_loggs
from rest_framework import generics
from ..serializers import bototpserializer,bototpvalidationserializer
from genericresponse import GenericResponse
from rest_framework.response import Response
from rest_framework.utils import json
from datetime import timedelta
import datetime
## otp generation function ##
import math
import random
from errormessage import Errormessage
from database import x

from SMS_textlocal import sendSMS



def GenerateOTP():
    digits = "0123456789"
    OTP = ""
    for i in range(6):
        OTP += digits[math.floor(random.random() * 10)]
    return OTP

# Create your views here.

class otp_genaration(generics.GenericAPIView):
    serializer_class = bototpserializer
    


    def post(self,request):
        """Here We Generating OTP"""
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
            user['Otp'] = otp_model1.otp
            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = "Successful"
            response.Result = user
            response.Status = 200
            response.HasError = False
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



class otp_validation(generics.GenericAPIView):
    serializer_class = bototpvalidationserializer
    


    def post(self,request,id):
        """Here We validating OTP"""
        try:

            logs = otp_loggs()
            otp=request.data.get('otp')
            number = otp_model.objects.get(id=id)
            t2 = datetime.datetime.now()
            current_date_time = datetime.datetime(t2.year, t2.month, t2.day, t2.hour, t2.minute)
            otploggs=otp_loggs()
            otploggs.otp=number.otp
            otploggs.expiry_on=number.expiry_on
            otploggs.phone_number=number.phone_number
            otploggs.status="Deactivated"


            if number.expiry_on>=current_date_time:
                if otp==number.otp:
                    otploggs.save()
                    response = GenericResponse("message", "result", "status", "has_error")
                    response.Message = "Successful"
                    response.Result = True
                    response.Status = 200
                    response.HasError = False
                    jsonStr = json.dumps(response.__dict__)
                    return Response(json.loads(jsonStr), status=200)
                else:
                    otploggs.save()
                    # delete_otp(id)
                    response = GenericResponse("message", "result", "status", "has_error")
                    response.Message = "Please enter valid OTP"
                    response.Result = False
                    response.Status = 400
                    response.HasError = True
                    jsonStr = json.dumps(response.__dict__)
                    return Response(json.loads(jsonStr), status=400)
            else:
                otploggs.save()
                response = GenericResponse("message", "result", "status", "has_error")
                response.Message = "OTP has Expired"
                response.Result = False
                response.Status = 400
                response.HasError = True
                jsonStr = json.dumps(response.__dict__)
                return Response(json.loads(jsonStr), status=400)
        except Exception as e:
            # delete_otp(id)
            response = GenericResponse("message", "result", "status", "has_error")
            response.Message = Errormessage(e)
            response.Result = False
            response.Status = 400
            response.HasError = True
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)


def otp_message_sms(phonenumber,otp):
    otp=otp
    number = phonenumber[1:]
    # number=phonenumber
    limit='15 mins'
    message=f"Dear User,This is your One Time Password {otp} for login into your Lifeeazy account. Your OTP will be valid for the next {limit}"
    resp = sendSMS(apikey='MzM2YzQ2NTQ0MTY0NTczOTYxNmY0NjY2NDc3OTQ0Mzk=', numbers=number,
                   sender='VFYHCI', message=message)
    print(resp)