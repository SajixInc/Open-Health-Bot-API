import datetime
import json
import requests
import time
from genericresponse import GenericResponse
from rest_framework import generics
from rest_framework.views import Response
from ..serializers import BotcowinSerializers

from errormessage import Errormessage

        
class vaccineSlotsbydistrict(generics.GenericAPIView):
    serializer_class = BotcowinSerializers
    
    def get(self,request,state_name,district_name):

        
        """Here  We're  getting  The  available vaccine slots  Based  On  district
        (example: district= Visakhapatnam )"""
        
        try:

            print(f"Showing you vaccination slots for DistricName: {district_name} for next 10 days")
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
                            
                            for i in range(10):
                                day = (datetime.date.today() + datetime.timedelta(i)).day
                                month = (datetime.date.today() + datetime.timedelta(i)).month
                                year = (datetime.date.today() + datetime.timedelta(i)).year
                                slot = 0
                                url = f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={district_id}&date={day:02}-{month:02}-{year}"
                                response = requests.request("GET", url)
                                vaccineCenters = json.loads(response.text)
                                a = vaccineCenters['sessions']
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
                                    

    