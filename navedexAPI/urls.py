"""navedexAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include

#from criador_navedex.api.urls import router

from rest_framework_jwt.views import obtain_jwt_token


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include('criador_navedex.api.urls')),
    #path('api/', include(router.urls)),

    path('api-auth/', include('rest_framework.urls')),

    path('token/', obtain_jwt_token, name='obtain_jwt_token'),
]

# CONFIGURAÇÃO PARA O AMBIENTE DE DESENVOLVIMENTO
# FORNECER OS ARQUIVOS ESTÁTICOS PARA A APLICAÇÃO
from django.conf.urls.static import static
from django.conf import settings

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
