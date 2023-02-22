import json
from django.apps import apps
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from genericresponse import GenericResponse
from ..serializers import OpenHealthIntractionserializers
from ..models import OpenhealthInteractionModel
from errormessage import Errormessage


class OpenHealthIntractionByUserId(APIView):
    serializer_class = OpenHealthIntractionserializers
    renderer_classes = [JSONRenderer]
    

    def get(self, request, UserId):
        """Here We Get The Open health intraction Data Based On UserId
        (Table_Name : 'Openhealth_InteractionTable')"""

        try:
            if OpenhealthInteractionModel.objects.filter(UserId=UserId,FamilyId=None).last():
                result = OpenhealthInteractionModel.objects.filter(UserId=UserId,FamilyId=None).last()
                # .order_by('-id')[:1]
                user = OpenHealthIntractionserializers(result)            
                response = GenericResponse("Message", "Result", "Status", "HasError")
                response.Message = "Successful"
                response.Result = user.data
                response.Status = 200
                response.HasError = False
                jsonStr = json.dumps(response.__dict__)
                return Response(json.loads(jsonStr), status=200)
            else:
                response = GenericResponse("Message", "Resul t", "Status", "HasError")
                response.Message = "No Intraction data in this user"
                response.Result = False
                response.Status = 400
                response.HasError = True
                jsonStr = json.dumps(response.__dict__)
                return Response(json.loads(jsonStr), status=400)
        except Exception as e:
            response = GenericResponse("Message", "Resul t", "Status", "HasError")
            response.Message = Errormessage(e)
            response.Result = False
            response.Status = 400
            response.HasError = True
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)