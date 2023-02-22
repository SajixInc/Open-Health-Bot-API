

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

class vaccineSlotsbydistrictanddate(generics.GenericAPIView):
    serializer_class = BotcowinSerializers
    
    def get(self,request,state_name,district_name,Date):
        print(f"Showing you vaccination slots for DistricName: {district_name} and {Date} for next 7 days")
        try:
            b = datetime.datetime.strptime(Date, '%d-%m-%Y')
            if b:
                url1 = f"https://cdndemo-api.co-vin.in/api/v2/admin/location/states"
                response = requests.request("GET", url1)
                states = json.loads(response.text)
                a = states['states']
                

                for i in a:


                    if i['state_name'] == state_name:


                        state_id = i['state_id']

                        url = f"https://cdn-api.co-vin.in/api/v2/admin/location/districts/{state_id}"

                        response = requests.request("GET", url)
                        vaccineCenters = json.loads(response.text)
                        c = vaccineCenters['districts']
                        for j in c:
                            if j['district_name'] == district_name:
                                district_id = j['district_id']
                                
            
                                # datee = str(Date)
                                # datem = datetime.datetime.strptime(datee, '%Y-%m-%d')
                                # date = datem.strftime('%d-%m-%Y')
                                print(f"Showing you vaccination slots for district_id: {district_id} and {Date} for next 7 days")
                                url = f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={district_id}&date={Date}"
                                response = requests.request("GET", url)
                                vaccineCenters = json.loads(response.text)
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
                            response.Message = "District name should be camel case"
                            response.Result = False
                            response.Status = 400
                            response.HasError = True
                            jsonStr = json.dumps(response.__dict__)
                            return Response(json.loads(jsonStr), status=400)
                else:
                    response = GenericResponse("Message", "Result", "Status", "HasError")
                    response.Message = "State name should be camel case"
                    response.Result = False
                    response.Status = 400
                    response.HasError = True
                    jsonStr = json.dumps(response.__dict__)
                    return Response(json.loads(jsonStr), status=400)

        except Exception as e:
            response = GenericResponse("message", "result", "status", "has_error")
            response.Message = Errormessage(e)
            response.Result = False
            response.Status = 500
            response.HasError = True
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=500)
        

        