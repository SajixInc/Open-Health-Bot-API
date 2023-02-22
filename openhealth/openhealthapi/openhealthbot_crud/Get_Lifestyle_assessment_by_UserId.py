import json
from django.apps import apps

from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from genericresponse import GenericResponse
from ..serializers import GetOpenHealthLifestyleScoringSerializer,GetQuestionLifestyleSerializer
from ..models import OpenhealthLifestyleAssessment
from errormessage import Errormessage


class OpenHealthLifestyleScoringByUserId(APIView):
    serializer_class = GetQuestionLifestyleSerializer
    renderer_classes = [JSONRenderer]
    
    def get(self, request, UserId):
        """Here We Get The Lifestyle assessment Data Based On UserId Include All the MasterData
        (Table_Name : 'Lifestyle scoring Questions',
        Table_Name : 'Openhealth_Lifestyle_Assessment_table')"""

        try:
            result = OpenhealthLifestyleAssessment.objects.filter(UserId_id=UserId)
            Question = apps.get_model('user_assessment', 'QuestionLifestyleScoresTableV2')
            if OpenhealthLifestyleAssessment.objects.filter(UserId_id=UserId):
                x = Question.objects.all()
                count = []
                dq = GetQuestionLifestyleSerializer(x, many=True)
                life = GetOpenHealthLifestyleScoringSerializer(result, many=True)
                for j in life.data:
                    count.append(int(j['QuestionId']))
                data = []
                a = 0
                for i in dq.data:
                    a=1
                    for j in life.data:
                        if int(i['id']) == int(j['QuestionId']):
                            if int(i['id']) in count:
                                i['Lifestyle'] = j
                                data.append(i)
                            else:
                                pass
                        else:
                            if int(i['id']) not in count:
                                if a==1:
                                    a+=1
                                    i['Lifestyle'] = "Not Answered"
                                    data.append(i)
                                else:
                                    pass
                response = GenericResponse("Message", "Result", "Status", "HasError")
                response.Message = "Successful"
                response.Result = data
                response.Status = 200
                response.HasError = False
                jsonStr = json.dumps(response.__dict__)
                return Response(json.loads(jsonStr), status=200)

            else:
                x = Question.objects.all()
                dq = GetQuestionLifestyleSerializer(x, many=True)
                data= []
                for i in dq.data:
                    i['Lifestyle'] = "Not Answered"
                    data.append(i)
                response = GenericResponse("Message", "Result", "Status", "HasError")
                response.Message = "Successful"
                response.Result = data
                response.Status = 200
                response.HasError = False
                jsonStr = json.dumps(response.__dict__)
                return Response(json.loads(jsonStr), status=200)
        except Question.DoesNotExist as e:
            response = GenericResponse("Message", "Resul t", "Status", "HasError")
            response.Message = Errormessage(e)
            response.Result = False
            response.Status = 400
            response.HasError = True
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)