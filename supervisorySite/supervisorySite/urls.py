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

from Charts.views import lineChartJson
from ClientOPC.views import getOPCValues, setOPCSetPoint, setOPCKi, setOPCKp, setOPCMode, setOPCVoltage
from ContentPage.views import homePage, helpPage
from FileManager.views import getHistoryTemperature, getHistorySetPoint, getHistoryVoltage, downloadPage
from ihm.views import Supervisory
from Settings.views import ChangeEndPoint

urlpatterns = [
    path("", homePage, name = 'homePage'),
    path("admin/", admin.site.urls),
    path("download", downloadPage, name = 'downloadPage'),
    path("help", helpPage, name = 'helpPage'),
    path("hmi", Supervisory, name = 'Supervisory'),
    path("settings", ChangeEndPoint, name = 'ChangeEndPoint'),
    path('chartJSON', lineChartJson, name='line_chart_json'),
    path("ajax/getOPCValues", getOPCValues, name = 'getOPCValues'),
    path("ajax/setOPCKi", setOPCKi, name = 'setOPCKi'),
    path("ajax/setOPCKp", setOPCKp, name = 'setOPCKp'),
    path("ajax/setOPCMode", setOPCMode, name = 'setOPCMode'),
    path("ajax/setOPCSetPoint", setOPCSetPoint, name = 'setOPCSetPoint'),
    path("ajax/setOPCVoltage", setOPCVoltage, name = 'setOPCVoltage'),
    path("file/setPoint", getHistorySetPoint, name = 'getHistorySetPoint'),
    path("file/temperature", getHistoryTemperature, name = 'getHistoryTemperature'),
    path("file/voltage", getHistoryVoltage, name = 'getHistoryVoltage'),
]
