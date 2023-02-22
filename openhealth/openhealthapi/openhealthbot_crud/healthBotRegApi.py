from rest_framework import generics
from rest_framework.response import Response
from rest_framework.utils import json
from genericresponse import GenericResponse
from ..serializers import OpenHealthRegSerializers
from errormessage import Errormessage


import logging, traceback
logger = logging.getLogger('django')


class OpenhealthbotRegView(generics.GenericAPIView):
    serializer_class = OpenHealthRegSerializers
    

    def post(self, request, *args, **kwargs):
        """Here We Post register the open health bot
           (Table name: OpenHealth_table)
        """
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = "Successful"
            response.Result = OpenHealthRegSerializers(user).data
            response.Status = 200
            response.HasError = False
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=200)
        except Exception as e:
            response = GenericResponse("message", "result", "status", "has_error")
            response.Message = str(e)
            response.Result = False
            response.Status = 400
            response.HasError = True
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)