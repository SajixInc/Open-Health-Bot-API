from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.conf.urls import *
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions








######## Version #########
schema_view = get_schema_view(
    openapi.Info(
        title="LifeEazy",
        default_version='1.0.0',
        name='openapi-schema',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('OpenHealthBot/', include('openhealthapi.urls')),
    path('swagger/' , schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    
    # path('redoc/',schema_view.with_ui('redoc',cache_timeout=0),name='schema-redoc'),
    

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
