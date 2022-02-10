"""kakaoWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
# For Swagger
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
#from django.conf.urls import url


# 기본 url 경로
urlpatterns = [
    path('admin/', admin.site.urls),
]

schema_view = get_schema_view(
    openapi.Info(
        title="Open API",
        default_version='v1',
        description='챗봇 API Docs',
        terms_of_service = "https://www.google.com/policies/terms/",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    patterns= urlpatterns,
)

urlpatterns += [
    path('', include('stt.urls')),
    path('user', include('user.urls')),
    path('community', include('community.urls')),
    path('swagger<str:format>', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('docs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
