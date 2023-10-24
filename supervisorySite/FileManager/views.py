from django.shortcuts import render, redirect
from django.http import HttpResponse
from asyncua import ua

from ClientOPC.OPCClientUA import OPCClientUA
from Settings.getEndPoint import getEndPoint

# Create your views here.
async def downloadPage(request):
    try:
        endPoint = await getEndPoint()
        client = OPCClientUA(endPoint) if endPoint else OPCClientUA()
        await client.connect()
        await client.disconnect()
    except (ConnectionError, ua.UaError):
        return redirect("/error")
    
    return render(request, "FileManager/downloads.html")

async def getHistoryData(variable : str) -> dict:
    endPoint = await getEndPoint()
        
    client = OPCClientUA(endPoint) if endPoint else OPCClientUA()
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