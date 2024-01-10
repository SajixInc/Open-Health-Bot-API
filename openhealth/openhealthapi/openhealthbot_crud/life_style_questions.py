from rest_framework import generics
from rest_framework.response import Response
from rest_framework.utils import json
from genericresponse import GenericResponse
from ..serializers import GetQuestionLifestyleSerializer
from errormessage import Errormessage
from rest_framework.permissions import IsAuthenticated
from ..models import *
import logging, traceback


logger = logging.getLogger('django')


class GetAllQuestionsLifeStyleScoringV2(generics.GenericAPIView):
    serializer_class = GetQuestionLifestyleSerializer
    # permission_classes = (IsAuthenticated,)

    def get(self, request):
       
        try:
            result = QuestionLifestyleScoresTableV2.objects.all()
            prodata = GetQuestionLifestyleSerializer(result, many=True)
            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = "Successful"
            response.Result = prodata.data
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