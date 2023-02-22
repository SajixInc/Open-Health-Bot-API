import datetime
import json
import requests
import time
from genericresponse import GenericResponse
from rest_framework import generics
from rest_framework.views import Response
from ..serializers import BotcowinSerializers

from errormessage import Errormessage

class vaccineSlotsbypincode(generics.GenericAPIView):
    serializer_class = BotcowinSerializers
    

    # def vaccineSlots(pincode, age):
    #     print(f"Showing you vaccination slots for pincode: {pincode} and age: {age} for next 10 days")
    #     # headers = {
    #     #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
    #     # }
    #
    #     for i in range(10):
    #         day = (datetime.date.today() + datetime.timedelta(i)).day
    #         month = (datetime.date.today() + datetime.timedelta(i)).month
    #         year = (datetime.date.today() + datetime.timedelta(i)).year
    #         slot = 0
    #         url = f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={pincode}&date={day:02}-{month:02}-{year}"
    #         response = requests.request("GET", url)
    #         vaccineCenters = json.loads(response.text)
    #         print(f"Date:{day:02}-{month:02}-{year}\n")
    #         for vaccineCenter in vaccineCenters['sessions']:
    #             if vaccineCenter['min_age_limit'] <= int(age) and vaccineCenter['available_capacity'] > 0:
    #                 slot += 1
    #                 print(
    #                     f"```Name:{vaccineCenter['name']}\nAddress:{vaccineCenter['address']}\nState:{vaccineCenter['state_name']}\nDistrict:{vaccineCenter['district_name']}\nVaccine:{vaccineCenter['vaccine']}\nSlots:{vaccineCenter['slots']}\nAge Limit : {vaccineCenter['min_age_limit']}\n\n```")
    #
    #         time.sleep(2)
    #         if slot == 0:
    #             print("```No Slots Available for the Day```")

    def get(self,request,pincode):
        """Here  We're  getting  The  available vaccine slots  Based  On  pincode (example: pincode= 530016 )"""

        print(f"Showing you vaccination slots for pincode: {pincode} for next 10 days")
            # headers = {
            #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
            # }
        try:
            for i in range(10):
                day = (datetime.date.today() + datetime.timedelta(i)).day
                month = (datetime.date.today() + datetime.timedelta(i)).month
                year = (datetime.date.today() + datetime.timedelta(i)).year
                slot = 0
                url = f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={pincode}&date={day:02}-{month:02}-{year}"
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
        except Exception as e:
            response = GenericResponse("message", "result", "status", "has_error")
            response.Message = 'API not working properly. Please check given inputs(Pincode must be 6 charecters)'
            response.Result = False
            response.Status = 500
            response.HasError = True
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=500)