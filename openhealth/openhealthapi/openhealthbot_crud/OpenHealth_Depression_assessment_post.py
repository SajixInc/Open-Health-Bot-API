from django.apps import apps
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.utils import json
from genericresponse import GenericResponse
from ..serializers import OpenHealthDepressionSerializer, GetOpenhealthDepressionSerializer
from errormessage import Errormessage

from ..models import OpenhealthInteractionModel, OpenhealthDepressionAssessment, QuestionDepressionTableV2
# from user_assessment.models import QuestionLifestyleScoresTableV2
import logging, traceback

# from ..serializers import dobb

logger = logging.getLogger('django')

class OpenHealthDepressionPostAPI(generics.GenericAPIView):
    serializer_class = OpenHealthDepressionSerializer
    

    def post(self, request):
        """Here We Post The Open health bot Depression Assessment And We Get Score Of Each Question User
        (Table_Name:'Openhealth_Depression_Assessment_table')"""
        try:
            question = request.data.get('QuestionId')
            # QuestionDepressionTable = apps.get_model('user_assessment', 'QuestionDepressionTableV2')
            Interactionid = request.data.get('InteractionId')
            Category=request.data.get('Category')
            data = QuestionDepressionTableV2.objects.get(id=question)
            sub_category=data.Sub_category
            if Category == sub_category:
                user = request.data.get('UserId')
                # try:
                #     a = OpenhealthInteractionModel.objects.get(UserId_id=user, InteractionId=Interactionid,
                #                                      Category=Category)
                if OpenhealthInteractionModel.objects.get(UserId_id=user, InteractionId=Interactionid,
                                                    Category=Category):
                    if OpenhealthDepressionAssessment.objects.filter(UserId = user, QuestionId = question,InteractionId=Interactionid):
                        response = GenericResponse("message", "result", "status", "has_error")
                        response.Message = "User answer for this question already upload Depression assessment"
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
                            response.Result = GetOpenhealthDepressionSerializer(user).data
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

                # except:
                #     response = GenericResponse("message", "result", "status", "has_error")
                #     response.Message = "Please enter the valid intractionId"
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