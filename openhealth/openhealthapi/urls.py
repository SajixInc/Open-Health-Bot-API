from django.urls import path, include

from .views import *
from django.conf import settings



urlpatterns =[
    path('otp_generation/',otp_genaration.as_view(),name = 'otp genration'),
    path('otpvalidate/<int:id>/',otp_validation.as_view(),name = 'otp validation'),
    path('vaccineSlotsbycenterid/<int:center_id>/<str:Date>/', vaccineSlotsbycenterid.as_view(), name="vaccineSlotsbycenterid"),
    path('vaccineSlotsbydistrictanddate/<str:state_name>/<str:district_name>/<str:Date>/', vaccineSlotsbydistrictanddate.as_view(), name="vaccineSlotsbydistrictanddate"),
    path('vaccineSlotsbypincodeanddate/<int:pincode>/<str:Date>/', vaccineSlotsbypincodeanddate.as_view(), name="vaccineSlotsbypincodeanddate"),
    path('CertificateDownload/<int:mobilenumber>/', CertificateDownload.as_view(), name="CertificateDownload"),
    path('vaccineSlotsbydistrict/<str:state_name>/<str:district_name>/', vaccineSlotsbydistrict.as_view(), name="vaccineSlotsbydistrict"),
    path('vaccineSlotsbypincode/<int:pincode>/', vaccineSlotsbypincode.as_view(), name="vaccineSlotsbypincode"),
    path('demographic_generation/',demographic_genaration.as_view(),name = 'demographic generation'),
    path('OpenHealthRegister/',OpenhealthbotRegView.as_view(), name ='Open Health Register API'),  
    path('OpenHealthIntractionPostApi/',OpenHealthInteractionView.as_view(), name ='Open Health Interaction post api'), 
    path('OpenHealthLifestyleScorePostAPI/',OpenHealthLifestyleScorePostAPI.as_view(), name ='Open Health Lifestyle Score Post API'),
    path('OpenHealthDepressionPostAPI/',OpenHealthDepressionPostAPI.as_view(), name ='Open Health Depression Post API'),
    path('OpenHealthDiabetesPost/',OpenHealthDiabetesPostAPI.as_view(), name ='Open Health Diabetes Post API'),
    path('OpenHealthLifestyleByUserId/<int:UserId>/',OpenHealthLifestyleScoringByUserId.as_view(), name = 'OpenHealth Lifestyle Scoring By using UserId'),
    path('OpenHealthBotUserByMobile/<str:Mobile>/',GetOpenhealthUser.as_view(), name = 'Get Open health Bot User'),
    path('OpenHealthDepressionByUserId/<int:UserId>/',OpenHealthDepressionByUserId.as_view(), name = 'Open health Depression By UserId'),
    path('GetOpenhealthIntractionUserId/<int:UserId>/',OpenHealthIntractionByUserId.as_view(), name = 'Get Open health intraction by UserId'),
    path('OpenHealthDiabetesByUserId/<int:UserId>/',OpenHealthDiabetesByUserId.as_view(), name='Get Open Health Diabete by User id'),
    path('OpenHealthAssessmentByUserId/<int:UserId>/',GetOpenhealthBotAssessmentView.as_view(), name='Get Open Health bot assessment by user id'),
    path('GetAllQuestionsLifeStyleScoringV2/',GetAllQuestionsLifeStyleScoringV2.as_view(), name='GetAllQuestionsLifeStyleScoringV2'),
    path('GetAllQuestionsDepressionV2/',GetAllQuestionsDepressionV2.as_view(), name='GetAllQuestionsDepressionV2'),
    path('GetAllQuestionsDiabetesV2/',GetAllQuestionsDiabetesV2.as_view(), name='GetAllQuestionsDiabetesV2'),
]