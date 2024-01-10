from rest_framework import generics
from rest_framework.response import Response
from rest_framework.utils import json
from django.apps import apps
from genericresponse import GenericResponse
from ..serializers import *
from errormessage import Errormessage

from ..models import *
import logging

from ..validation import validation, category_validation,answer_validation_depression,answer_validation_diabetes

logger = logging.getLogger('django')


class GetOpenhealthBotAssessmentView(generics.GenericAPIView):
    serializer_class = GetOpenHealthLifestyleScoringSerializer
    
    def get(self, request, UserId):
        """Here We Get the Session Scoring The User Have Fill All The Questions For Every Session Then We Get The Scoring For All Sessions
        Or Else He/She Fill Only One Session Questions Then They Will  Only Get That One Session Scoring  Which They Are Filled By Using UserId
        (Here We Get Scoring From Different Tables
        1.Table_Name:'User_Diabetes_Assessment_table'
        2.Table_Name: 'User_Depression_Assessment_table'
        3.Table_Name: 'User_Lifestyle_Assessment_table')"""
        try:
            # lifeQ = QuestionLifestyleScoresTableV2()
            # depreQ = QuestionDepressionTableV2()
            # DiaQ = QuestionDiabetesTableV2()
            diab=0
            depres=0
            lifeee=0
            Diintration = OpenhealthInteractionModel.objects.filter(UserId=UserId,FamilyId=None,Category="Diabetes").order_by('-id')[:1]
            deintration = OpenhealthInteractionModel.objects.filter(UserId=UserId,FamilyId=None,Category="Depression").order_by('-id')[:1]
            lifeintration = OpenhealthInteractionModel.objects.filter(UserId=UserId,FamilyId=None,Category="Lifestyle").order_by('-id')[:1]
            for i in deintration:
                depres=i.InteractionId
                print(depres)
            for j in Diintration:
                diab = j.InteractionId
                print(diab,"diab")
            for k in lifeintration:
                lifeee = k.InteractionId
                print(lifeee,"lifeee")
            print(lifeee,depres,diab)
            result1 = OpenhealthDiabetesAssessment.objects.filter(UserId_id=UserId,Category="Diabetes",FamilyId=None,InteractionId=diab)
            # print(result1,"result1")
            result2 = QuestionDiabetesTableV2.objects.filter(Category="Diabetes")
            Diabetes = GetOpenhealthDiabetesSerializer(result1,many=True)
            # print(Diabetes,"diaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
            Diabetes1=GetQuestionDiabetesSerializer(result2,many=True)
            result3 = OpenhealthDepressionAssessment.objects.filter(UserId_id=UserId,Category="Depression",FamilyId=None,InteractionId=depres)
            result4 = QuestionDepressionTableV2.objects.filter(Category="Depression")
            Depression = GetOpenhealthDepressionSerializer(result3, many=True)
            Depression1 = GetQuestionDepressionSerializer(result4, many=True)
            result5 = OpenhealthLifestyleAssessment.objects.filter(UserId=UserId,Category="Lifestyle",FamilyId=None,InteractionId=lifeee)
            result6 = QuestionLifestyleScoresTableV2.objects.filter(Category="lifestyle scoring")
            Lifestyle = GetOpenHealthLifestyleScoringSerializer(result5, many=True)
            Lifestyle1 = GetQuestionLifestyleSerializer(result6, many=True)
            ss=int(len(Diabetes1.data))
            print(ss,"sssssssssssssssssssss")
            ss1=int(len(Depression1.data))
            lifestylelen=len(Lifestyle1.data)
            rr = len(Diabetes.data)
            print(rr,"rrrrrrrrrrrrrrrrrrrr")
            rr1 = len(Depression.data)
            lifestyleQn=len(Lifestyle.data)
            life = {}
            totalscore_result9=[]
            totalscore_result7=[]
            totalscore_result1 = []
            totalscore_result2 = []
            a={}
        
            if rr == ss:
                decount=0
                for m in Diabetes.data:
                    if m['Answer'] == "Yes":
                        # print('rr')
                        totalscore_result9.append(m)
                        decount += 1
                    else:
                        totalscore_result9.append(m)
                if decount == rr:
                    validate = answer_validation_diabetes("Yes")
                    totalscore_result7.append(validate)
                else:
                    validate = answer_validation_diabetes("No")
                    totalscore_result7.append(validate)
                a['Diabities'] = totalscore_result9
                a['Risk to Diabities'] = totalscore_result7
            print(rr1,ss1)
            if rr1==ss1:
                # print(Depression.data)
                dicount = 0
                for m in Depression.data:
                    if m['Answer'] == "Yes":
                        print(rr)
                        totalscore_result1.append(m)
                        dicount += 1
                    else:
                        totalscore_result1.append(m)
                if dicount == rr1:
                    validate = answer_validation_depression("Yes")
                    totalscore_result2.append(validate)
                else:
                    validate = answer_validation_depression("No")
                    totalscore_result2.append(validate)
                if totalscore_result1:
                    a['Depression'] = totalscore_result1
                    print(a["Depression"])
                    a['Risk to Depression'] = totalscore_result2
            if lifestylelen == lifestyleQn:
                print("aa")
                result51 = OpenhealthLifestyleAssessment.objects.filter(UserId_id=UserId,Category="Lifestyle",
                                                                  Sub_category="Connectedness",FamilyId=None,InteractionId=lifeee)
                result52 = OpenhealthLifestyleAssessment.objects.filter(UserId_id=UserId, Category="Lifestyle",
                                                                  Sub_category="Movement",FamilyId=None,InteractionId=lifeee)
                result53 = OpenhealthLifestyleAssessment.objects.filter(UserId_id=UserId, Category="Lifestyle",
                                                                  Sub_category="Nutrition",FamilyId=None,InteractionId=lifeee)
                result54 = OpenhealthLifestyleAssessment.objects.filter(UserId_id=UserId, Category="Lifestyle",
                                                                  Sub_category="Recovery",FamilyId=None,InteractionId=lifeee)
                result55 = OpenhealthLifestyleAssessment.objects.filter(UserId_id=UserId, Category="Lifestyle",
                                                                  Sub_category="SubstanceUse",FamilyId=None,InteractionId=lifeee)
                totalscore_result11 = []
                # print(totalscore_result11,'jhjh')
                totalscore_result22 = []
                totalscore_result33 = []
                totalscore_result4 = []
                totalscore_result5 = []
                for i in result51:
                    # print(i.Score)
                    totalscore_result11.append(i.Score)
                for j in result52:
                    totalscore_result22.append(j.Score)
                for k in result53:
                    totalscore_result33.append(k.Score)
                for l in result54:
                    totalscore_result4.append(l.Score)
                for m in result55:
                    totalscore_result5.append(m.Score)
                Connectedness = GetOpenHealthLifestyleScoringSerializer(result51, many=True)
                Movement = GetOpenHealthLifestyleScoringSerializer(result52, many=True)
                Nutrition = GetOpenHealthLifestyleScoringSerializer(result53, many=True)
                Recovery = GetOpenHealthLifestyleScoringSerializer(result54, many=True)
                SubstanceUse = GetOpenHealthLifestyleScoringSerializer(result55, many=True)
                # connectedness = prodata.data
                score1 = sum(totalscore_result11)
                score2 = sum(totalscore_result22)
                score3 = sum(totalscore_result33)
                score4 = sum(totalscore_result4)
                score5 = sum(totalscore_result5)
                c = (score1 + score2 + score3 + score4 + score5)
                life['Connectedness']= Connectedness.data
                life['ConnectednessDomainTotal'] = score1, category_validation(score1)
                life['Movement'] = Movement.data
                life['MovementDomainTotal'] = score2, category_validation(score2)
                life['Nutrition'] = Nutrition.data
                life['NutritionDomainTotal'] = score3, category_validation(score3)
                life['Recovery'] = Recovery.data
                life['RecoveryDomainTotal'] = score4, category_validation(score4)
                life['SubstanceUse'] = SubstanceUse.data
                life['SubstanceUseDomainTotal'] = score5, category_validation(score5)
                life['Overall_Lifestyle'] = c, validation(c)
                a['Life Style Scoring'] = life
            if totalscore_result9 or totalscore_result1 or life:
                response = GenericResponse("Message", "Result", "Status", "HasError")
                response.Message = "Successful"
                response.Result = a
                response.Status = 200
                response.HasError = False
                jsonStr = json.dumps(response.__dict__)
                return Response(json.loads(jsonStr), status=200)
            else:
                response = GenericResponse("message", "result", "status", "has_error")
                response.Message = "This User Don't Have Assessment"
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
