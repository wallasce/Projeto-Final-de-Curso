"""
URL configuration for supervisorySite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from ihm.views import Supervisory
from ClientOPC.views import getOPCValues, setOPCSetPoint, setOPCKi, setOPCKp, setOPCMode, setOPCVoltage
from FileManager.views import getHistoryTemperature

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", Supervisory),
    path("ajax/getOPCValues", getOPCValues, name = 'getOPCValues'),
    path("ajax/setOPCSetPoint", setOPCSetPoint, name = 'setOPCSetPoint'),
    path("ajax/setOPCKi", setOPCKi, name = 'setOPCKi'),
    path("ajax/setOPCKp", setOPCKp, name = 'setOPCKp'),
    path("ajax/setOPCMode", setOPCMode, name = 'setOPCMode'),
    path("ajax/setOPCVoltage", setOPCVoltage, name = 'setOPCVoltage'),
    path("file/temperature", getHistoryTemperature, name = 'getHistoryTemperature'),
]
