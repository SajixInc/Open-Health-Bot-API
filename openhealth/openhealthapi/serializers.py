from django.apps import apps
from .models import *
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .score import Score


class botdemographicserializer(serializers.ModelSerializer):
    class Meta:
        model = demographicModel
        fields = ['InteractionId', 'age', 'gender', 'ethnicity']


class bototpserializer(serializers.ModelSerializer):
    class Meta:
        model = otp_model
        fields = "phone_number",


class bototpvalidationserializer(serializers.ModelSerializer):
    class Meta:
        model = otp_model
        fields = "id","otp"

class BotcowinSerializers(serializers.Serializer):
    # center_id = serializers.IntegerField()
    Date = serializers.CharField(max_length=25)


class OpenHealthRegSerializers(serializers.ModelSerializer):
    class Meta:
        model = OpenHealthModel
        fields = ['id','MobileNumber']


class OpenHealthIntractionPostSerializers(serializers.ModelSerializer):
    class Meta:
        model = OpenhealthInteractionModel
        fields = ['id','UserId','Category']


    def create(self, validated_data):
        userId = validated_data['UserId']
        catagory = validated_data['Category']
        interaction = OpenhealthInteractionModel.objects.filter(UserId=userId,Category=catagory).order_by('-id')[:1]
        if interaction:
            global interactionid
            for i in interaction:
                print(type(i))
                interactionid=i.InteractionId

            a=OpenhealthInteractionModel.objects.create(UserId=validated_data['UserId'],
                                              Category=validated_data['Category'],
                                              InteractionId=interactionid+1)
            a.save()
            return a
        else:
            a = OpenhealthInteractionModel.objects.create(UserId=validated_data['UserId'],
                                                Category=validated_data['Category'],
                                                InteractionId=1)
            a.save()
            return a


class OpenHealthIntractionserializers(serializers.ModelSerializer):
    class Meta:
        model = OpenhealthInteractionModel
        fields = ['id', 'UserId', 'FamilyId', 'Category', 'InteractionId']


class OpenHealthLisestyleScoringSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpenhealthLifestyleAssessment
        fields = ['UserId','QuestionId','Answer','Age', 'Category','Sub_category','InteractionId']
    def create(self, validated_data):
        questionid = validated_data['QuestionId']
        answer = validated_data['Answer']
        s = Score(questionid,answer)
        user = OpenhealthLifestyleAssessment.objects.create(UserId = validated_data['UserId'],
                                             QuestionId=validated_data['QuestionId'],
                                             Category = validated_data['Category'],
                                             Sub_category = validated_data['Sub_category'],
                                             InteractionId = validated_data['InteractionId'],
                                             Age = validated_data['Age'],
                                             Answer=answer,
                                             Score = s)

        user.save()
        return user


class OpenHealthDepressionSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpenhealthDepressionAssessment
        fields = ['UserId','QuestionId','Answer','Age', 'Category','InteractionId']
    def create(self, validated_data):
        questionid = validated_data['QuestionId']
        answer = validated_data['Answer']
        s = Score(questionid,answer)
        user = OpenhealthDepressionAssessment.objects.create(UserId = validated_data['UserId'],
                                             QuestionId=validated_data['QuestionId'],
                                             Category = validated_data['Category'],
                                             InteractionId = validated_data['InteractionId'],
                                             Age = validated_data['Age'],
                                             Answer=answer,
                                             Score = s)

        user.save()
        return user


class OpenHealthDiabetesSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpenhealthDiabetesAssessment
        fields = ['UserId','QuestionId','Answer','Age', 'Category','InteractionId']
    def create(self, validated_data):
        questionid = validated_data['QuestionId']
        answer = validated_data['Answer']
        s = Score(questionid,answer)
        user = OpenhealthDiabetesAssessment.objects.create(UserId = validated_data['UserId'],
                                             QuestionId=validated_data['QuestionId'],
                                             Category = validated_data['Category'],
                                             InteractionId = validated_data['InteractionId'],
                                             Age = validated_data['Age'],
                                             Answer=answer,
                                             Score = s)

        user.save()
        return user


class GetOpenHealthLifestyleScoringSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpenhealthLifestyleAssessment
        fields = ['id', 'UserId', 'FamilyId', 'QuestionId', 'Age', 'Answer', 'Category','Sub_category', 'InteractionId',
                  'AssessmentId', 'Score']


class GetQuestionLifestyleSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionLifestyleScoresTableV2
        fields = ['id','Question','Sub_category']


class GetOpenhealthDepressionSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpenhealthDepressionAssessment
        fields = ['id', 'UserId', 'FamilyId', 'QuestionId', 'Age', 'Answer', 'Category', 'InteractionId',
                  'AssessmentId', 'Score']

class GetQuestionDepressionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionDepressionTableV2
        fields = ['id','Question','Sub_category']


class GetOpenhealthDiabetesSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpenhealthDepressionAssessment
        fields = ['id', 'UserId', 'FamilyId', 'QuestionId', 'Age', 'Answer', 'Category', 'InteractionId',
                  'AssessmentId', 'Score']

class GetQuestionDiabetesSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionDiabetesTableV2
        fields = ['id','Question','Sub_category']