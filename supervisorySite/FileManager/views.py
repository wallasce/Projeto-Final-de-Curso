from django.shortcuts import render
from django.http import HttpResponse

from ClientOPC.OPCClientUA import OPCClientUA

# Create your views here.
async def getHistoryData(variable : str) -> dict:
    client = OPCClientUA()
    await client.connect()
    historyData = await client.getHistoryDataFrom(variable)    
    await client.disconnect()

    return historyData

async def getHistoryTemperature(request):
    fileData = await getHistoryData('temperature')

    response = HttpResponse(fileData, content_type='application/text charset=utf-8')
    response['Content-Disposition'] = 'attachment; filename="HistoryTemperature.txt"'
    return response

async def getHistorySetPoint(request):
    fileData = await getHistoryData('setPoint')

    response = HttpResponse(fileData, content_type='application/text charset=utf-8')
    response['Content-Disposition'] = 'attachment; filename="HistorySetPoint.txt"'
    return response

async def getHistoryVoltage(request):
    fileData = await getHistoryData('voltage')

    response = HttpResponse(fileData, content_type='application/text charset=utf-8')
    response['Content-Disposition'] = 'attachment; filename="HistoryVoltage.txt"'
    return response