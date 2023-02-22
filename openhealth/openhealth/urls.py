from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include, re_path
from django.conf.urls import *
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
# from rest_framework.schemas import get_schema_view, openapi
from django.views.generic import TemplateView
import subprocess
from rest_framework import generics, permissions
from rest_framework.response import Response


# class LoginAPI(generics.GenericAPIView):
#     serializer_class = UserSerializer

#     def token():
#         unique_id = get_random_string(length=32)
#         return unique_id
#     global x
#     x=token()
#     def post(self, request, token = x):
#         serializer = AuthTokenSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         print(token)
#         return redirect('/schema/'+x)





##### home login ###############
global version
# branch_name = subprocess.check_output('git branch --show-current', shell=True)
branch_name = subprocess.check_output('hostname', shell=True)
print(branch_name)
# host = [b'main\n', b'prod\n']
if branch_name == b'vivify-dev-api\n':
    version = 'v6.3.0-Staging'
    print(version)
elif branch_name == b'vivify-prod-api\n':
    print(version)
    version = 'v1.9.6-Prod'
else:
    version = 'v6.3.0-Staging'
    print(version)


######## Version #########
schema_view = get_schema_view(
    openapi.Info(
        title="LifeEazy",
        default_version=version,
        name='openapi-schema',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('OpenHealthAPI/', include('openhealthapi.urls')),
    path('swagger/' , schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    
    # path('redoc/',schema_view.with_ui('redoc',cache_timeout=0),name='schema-redoc'),
    

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
