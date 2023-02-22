from django.apps import apps
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.utils import json
from genericresponse import GenericResponse
from ..serializers import OpenHealthLisestyleScoringSerializer,GetOpenHealthLifestyleScoringSerializer
from errormessage import Errormessage

from ..models import OpenhealthInteractionModel, OpenhealthLifestyleAssessment
# from user_assessment.models import QuestionLifestyleScoresTableV2
import logging, traceback

# from ..serializers import dobb

logger = logging.getLogger('django')

class OpenHealthLifestyleScorePostAPI(generics.GenericAPIView):
    serializer_class = OpenHealthLisestyleScoringSerializer
    

    def post(self, request):
        """Here We Post The Open health bot LifeStyle Assessment And We Get Score Of Each Question User
        (Table_Name:'Openhealth_Lifestyle_Assessment_table')"""
        try:
            question = request.data.get('QuestionId')
            QuestionLifestyleScoresTable = apps.get_model('user_assessment', 'QuestionLifestyleScoresTableV2')
            Interactionid = request.data.get('InteractionId')
            Sub_category=request.data.get('Sub_category')
            Category=request.data.get('Category')
            data = QuestionLifestyleScoresTable.objects.get(id=question)
            sub_category=data.Sub_category
            if Sub_category == sub_category:
                user = request.data.get('UserId')
                # try:
                    # a = 
                if OpenhealthInteractionModel.objects.get(UserId_id=user, InteractionId=Interactionid,
                                                    Category=Category):
                    if OpenhealthLifestyleAssessment.objects.filter(UserId = user, QuestionId = question,InteractionId=Interactionid):
                        response = GenericResponse("message", "result", "status", "has_error")
                        response.Message = "User answer for this question already upload lifestyle assessment"
                        response.Result = False
                        response.Status = 400
                        response.HasError = True
                        jsonStr = json.dumps(response.__dict__)
                        return Response(json.loads(jsonStr), status=400)
                    else:
                        serializer = self.get_serializer(data=request.data)
                        if serializer.is_valid(raise_exception=True):
                            user = serializer.save()
                            response = GenericResponse("Message", "Result", "Status", "HasError")
                            response.Message = "Successful"
                            response.Result = GetOpenHealthLifestyleScoringSerializer(user).data
                            response.Status = 200
                            response.HasError = False
                            jsonStr = json.dumps(response.__dict__)
                            return Response(json.loads(jsonStr), status=200)
                else:
                    response = GenericResponse("Message", "Result", "Status", "HasError")
                    response.Message = "This User Don't Have The InteractionId"
                    response.Result = False
                    response.Status = 400
                    response.HasError = True
                    jsonStr = json.dumps(response.__dict__)
                    return Response(json.loads(jsonStr), status=400)

                # except Exception as e:
                #     response = GenericResponse("message", "result", "status", "has_error")
                #     response.Message = e
                #     response.Result = False
                #     response.Status = 400
                #     response.HasError = True
                #     jsonStr = json.dumps(response.__dict__)
                #     return Response(json.loads(jsonStr), status=400)

            else:
                response = GenericResponse("message", "result", "status", "has_error")
                response.Message ="Please provide the correct category"
                response.Result = False
                response.Status = 400
                response.HasError = True
                jsonStr = json.dumps(response.__dict__)
                return Response(json.loads(jsonStr), status=400)
        except Exception as e:
            response = GenericResponse("message", "result", "status", "has_error")
            response.Message = Errormessage(e)
            response.Result = False
            response.Status = 400
            response.HasError = True
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)