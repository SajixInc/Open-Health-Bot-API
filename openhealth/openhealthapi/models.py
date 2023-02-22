from django.db import models
from datetime import datetime
from django.core.validators import RegexValidator

# Create your models here.

Questions_Category = (
    ('Connectedness', 'Connectedness'),
    ('Movement', 'Movement'),
    ('Nutrition', 'Nutrition'),
    ('Recovery', 'Recovery'),
    ('SubstanceUse', 'SubstanceUse'),
    ('Depression', 'Depression'),
    ('Diabetes', 'Diabetes'),
)

Answers = (
    ('Yes', 'Yes'),
    ('No', 'No'),
    ('less than 1', 'less than 1'),
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10+', '10+'),
    ('less than 30', 'less than 30'),
    ('30', '30'),
    ('45', '45'),
    ('60', '60'),
    ('90', '90'),
    ('120', '120'),
    ('150', '150'),
    ('180', '180'),
    ('210', '210'),
    ('240', '240'),
    ('270', '270'),
    ('300+', '300+'),
)
ethnicity_choices = (
    ('white', 'WHITE'),
    ('Black or African American', 'BLACK OR AFRICAN AMERICAN'),
    ('Asian', 'ASIAN'),
    ('Native Hawaiian or Other Pacific Islander', 'NATIVE HAWAIIAN OR OTHER PACIFIC ISLANDER'),
    ('American Indian or Alaska Native', 'AMERICAN INDIAN OR ALASKA NATIVE'),
    ('Hispanic or Latino', 'HISPANIC OR LATINO')
)

Lifestylescoreing_CategoryV2 = (
    ('Connectedness', 'Connectedness'),
    ('Movement', 'Movement'),
    ('Nutrition', 'Nutrition'),
    ('Recovery', 'Recovery'),
    ('SubstanceUse', 'SubstanceUse'),
)

Depression_CategoryV2 = (
    ('Depression', 'Depression'),
)

Diabetes_CategoryV2 = (
    ('Diabetes', 'Diabetes'),
)

Category = (
    ('Lifestyle', 'Lifestyle'),
    ('Depression', 'Depression'),
    ('Diabetes', 'Diabetes'),
)


# Create your models here.

class otp_model(models.Model):
    otp = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=100, unique=True)
    date_time = models.DateTimeField()
    expiry_on = models.DateTimeField()

    class Meta:
        db_table = 'bot_otp_table'


class otp_loggs(models.Model):
    otp = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=100, unique=True)
    date_time = models.DateTimeField()
    expiry_on = models.DateTimeField()
    status = models.CharField(max_length=10)

    class Meta:
        db_table = 'bot_otp_log'


class demographicModel(models.Model):
    InteractionId = models.ForeignKey(otp_model, related_name='bot_democratic_table', on_delete=models.CASCADE)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    ethnicity = models.CharField(max_length=50, choices=ethnicity_choices, default='')

    class Meta:
        db_table = 'bot_demographic_table'


class OpenHealthModel(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,14}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 14 digits "
                                         "allowed.")
    MobileNumber = models.CharField(validators=[phone_regex], max_length=14, unique=True)
    objects = models.manager

    class Meta:
        db_table = 'OpenHealth_table'


class QuestionLifestyleScoresTableV2(models.Model):
    AssessmentId = models.IntegerField(default=1)
    Question = models.CharField(max_length=500)
    Category = models.CharField(max_length=100,default="lifestyle scoring")
    Sub_category = models.CharField(max_length=30,choices=Lifestylescoreing_CategoryV2)
    class Meta:
        db_table = "Lifestyle scoring Questions"


class QuestionDepressionTableV2(models.Model):
    AssessmentId = models.IntegerField(default=2)
    Question = models.CharField(max_length=500)
    Category = models.CharField(max_length=100,default="Depression")
    Sub_category = models.CharField(max_length=30,choices=Depression_CategoryV2)
    class Meta:
        db_table = "Depression Questions"


class QuestionDiabetesTableV2(models.Model):
    AssessmentId = models.IntegerField(default=3)
    Question = models.CharField(max_length=500)
    Category = models.CharField(max_length=100,default="Diabetes")
    Sub_category = models.CharField(max_length=30,choices=Diabetes_CategoryV2)
    class Meta:
        db_table = "Diabetes Questions"


class OpenhealthLifestyleAssessment(models.Model):
    UserId = models.ForeignKey(OpenHealthModel, related_name='UserOpenhealthLifestyle', on_delete=models.CASCADE)
    FamilyId = models.CharField(max_length=255, default=None)
    Age = models.CharField(max_length=200)
    QuestionId = models.ForeignKey('QuestionLifestyleScoresTableV2', related_name='OpenhealthLifestyle',
                                   on_delete=models.CASCADE)
    Category = models.CharField(max_length=100, choices=Category, default="Lifestyle")
    Sub_category = models.CharField(max_length=100, choices=Lifestylescoreing_CategoryV2)
    AssessmentId = models.IntegerField(default=1)
    InteractionId = models.IntegerField()
    Answer = models.CharField(max_length=20, choices=Answers)
    Score = models.IntegerField()
    CreatedOn = models.DateTimeField(default=datetime.today)
    UpdatedOn = models.DateTimeField(auto_now=True)
    objects = models.Manager

    class Meta:
        db_table = "Openhealth_Lifestyle_Assessment_table"


class OpenhealthDepressionAssessment(models.Model):
    UserId = models.ForeignKey(OpenHealthModel, related_name='UserOpenhealthDepression', on_delete=models.CASCADE)
    FamilyId = models.CharField(max_length=255, default=None)
    Age = models.CharField(max_length=200)
    QuestionId = models.ForeignKey('QuestionDepressionTableV2', related_name='OpenhealthDepression',
                                   on_delete=models.CASCADE)
    Category = models.CharField(max_length=100, choices=Depression_CategoryV2)
    AssessmentId = models.IntegerField(default=2)
    InteractionId = models.IntegerField()
    Answer = models.CharField(max_length=20, choices=Answers)
    Score = models.IntegerField()
    CreatedOn = models.DateTimeField(default=datetime.today)
    UpdatedOn = models.DateTimeField(auto_now=True)
    objects = models.Manager

    class Meta:
        db_table = "Openhealth_Depression_Assessment_table"


class OpenhealthDiabetesAssessment(models.Model):
    UserId = models.ForeignKey(OpenHealthModel, related_name='UserOpenhealthDiabetes', on_delete=models.CASCADE)
    FamilyId = models.CharField(max_length=25, default=None)
    Age = models.CharField(max_length=200)
    QuestionId = models.ForeignKey('QuestionDiabetesTableV2', related_name='OpenhealthDiabetes',
                                   on_delete=models.CASCADE)
    Category = models.CharField(max_length=100, choices=Diabetes_CategoryV2)
    AssessmentId = models.IntegerField(default=3)
    InteractionId = models.IntegerField()
    Answer = models.CharField(max_length=20, choices=Answers)
    Score = models.IntegerField()
    CreatedOn = models.DateTimeField(default=datetime.today)
    UpdatedOn = models.DateTimeField(auto_now=True)
    objects = models.Manager

    class Meta:
        db_table = "Openhealth_Diabetes_Assessment_table"


class OpenhealthInteractionModel(models.Model):
    UserId = models.ForeignKey(OpenHealthModel, related_name='Openhealth_InteractionUser', on_delete=models.CASCADE)
    FamilyId = models.CharField(max_length=255, default=None)
    InteractionId = models.IntegerField()
    Category = models.CharField(max_length=100, choices=Category)
    objects = models.Manager

    class Meta:
        db_table = "Openhealth_InteractionTable"
