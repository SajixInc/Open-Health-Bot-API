import json
import requests
from genericresponse import GenericResponse
from rest_framework import generics
from rest_framework.views import Response
from ..serializers import BotcowinSerializers

class CertificateDownload(generics.GenericAPIView):
    serializer_class = BotcowinSerializers
    def get(self,mobilenumber):
        """Here We Downloading Certificate through Mobile Number"""
        a = '503 Service Unavailable server error'
        response = GenericResponse("Message", "Result", "Status", "HasError")
        response.Message = "Successful"
        response.Result = a
        response.Status = 200
        response.HasError = False
        jsonStr = json.dumps(response.__dict__)
        return Response(json.loads(jsonStr), status=200)

    