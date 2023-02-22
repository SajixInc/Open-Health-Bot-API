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

class vaccineSlotsbycenterid(generics.GenericAPIView):
    serializer_class = BotcowinSerializers
    
    def get(self,request,center_id,Date):
        """Here  We're  getting  The  available vaccine slots  Based  On  center Id and Date
        (Here center Id is nothing but Vaccination center id(example: center id= 818143,Date= 29-11-2022 )"""
        print(center_id)
        
        
        try:
            b = datetime.datetime.strptime(Date, '%d-%m-%Y')
            if b:
                # datee = str(Date)
                # datem = datetime.datetime.strptime(datee, '%Y-%m-%d')
                # date = datem.strftime('%d-%m-%Y')
                print(f"Showing you vaccination slots for pincode: {center_id} and {Date} for next 7 days")
                url = f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByCenter?center_id={center_id}&date={Date}"
                response = requests.request("GET", url)
                vaccineCenters = json.loads(response.text)
                print(vaccineCenters)
                if len(vaccineCenters)==0:
                    response = GenericResponse("Message", "Result", "Status", "HasError")
                    response.Message = "There is no vaccination centers available"
                    response.Result = False
                    response.Status = 400
                    response.HasError = True
                    jsonStr = json.dumps(response.__dict__)
                    return Response(json.loads(jsonStr), status=400)
                else:
                    a = vaccineCenters['centers']
                    response = GenericResponse("Message", "Result", "Status", "HasError")
                    response.Message = "Successful"
                    response.Result = a
                    response.Status = 200
                    response.HasError = False
                    jsonStr = json.dumps(response.__dict__)
                    return Response(json.loads(jsonStr), status=200)
        except Exception as e:
            response = GenericResponse("message", "result", "status", "has_error")
            response.Message = Errormessage(e)
            response.Result = False
            response.Status = 500
            response.HasError = True
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=500)

        

        

    



    # print(vaccineSlots(818143,'16-11-2022'))