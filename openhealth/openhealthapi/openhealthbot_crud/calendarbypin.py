

from django.shortcuts import render

# Create your views here.

import datetime
import json
from ..serializers import BotcowinSerializers

from errormessage import Errormessage
import requests
import time
from genericresponse import GenericResponse
from rest_framework import generics
from rest_framework.views import Response

class vaccineSlotsbypincodeanddate(generics.GenericAPIView):
    serializer_class = BotcowinSerializers
    
    def get(self,request,pincode,Date):
        """Here  We're  getting  The  available vaccine slots  Based  On  pincode and Date
        (example: pincode= 530016 ,Date= 29-11-2022 )"""
        # datee = str(Date)
        # datem = datetime.datetime.strptime(datee, '%Y-%m-%d')
        # date = datem.strftime('%d-%m-%Y')
        try:
            b = datetime.datetime.strptime(Date, '%d-%m-%Y')
            if b:
                print(f"Showing you vaccination slots for pincode: {pincode} and {Date} for next 7 days")
                url = f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={pincode}&date={Date}"
                response = requests.request("GET", url)
                vaccineCenters = json.loads(response.text)
                print(vaccineCenters)
                a = vaccineCenters['centers']
                if len(a)==0:
                    response = GenericResponse("Message", "Result", "Status", "HasError")
                    response.Message = "There is no vaccination centers available"
                    response.Result = False
                    response.Status = 400
                    response.HasError = True
                    jsonStr = json.dumps(response.__dict__)
                    return Response(json.loads(jsonStr), status=400)
                else:
                    response = GenericResponse("Message", "Result", "Status", "HasError")
                    response.Message = "Successful"
                    response.Result = a
                    response.Status = 200
                    response.HasError = False
                    jsonStr = json.dumps(response.__dict__)
                    return Response(json.loads(jsonStr), status=200)
            else:
                response = GenericResponse("Message", "Result", "Status", "HasError")
                response.Message = "Please enter the valid date"
                response.Result = False
                response.Status = 400
                response.HasError = True
                jsonStr = json.dumps(response.__dict__)
                return Response(json.loads(jsonStr), status=400)
        except ValueError as e:
            response = GenericResponse("message", "result", "status", "has_error")
            response.Message = 'API not working properly. Please check given Date input(dd-mm-yyyy)'
            response.Result = False
            response.Status = 500
            response.HasError = True
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=500)
        except Exception as e:
            response = GenericResponse("message", "result", "status", "has_error")
            response.Message = 'API not working properly. Please check given inputs(Pincode must be 6 charecters)'
            response.Result = False
            response.Status = 500
            response.HasError = True
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=500)
        

