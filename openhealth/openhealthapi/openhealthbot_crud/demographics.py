from rest_framework import generics
from genericresponse import GenericResponse
from rest_framework.response import Response
from rest_framework.utils import json
from ..models import demographicModel
from ..serializers import botdemographicserializer
from errormessage import Errormessage

class demographic_genaration(generics.GenericAPIView):
    serializer_class = botdemographicserializer

    def post(self, request):
        """Here  We're  Posting  The  User  Demographic Details  Based  On  InteractionId (Here InteractionId is nothing but user Registration id)"""
        try:
            s=self.get_serializer(data=request.data)
            s.is_valid(raise_exception=True)
            user=s.save()
            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = "Successful"
            response.Result = botdemographicserializer(user).data
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