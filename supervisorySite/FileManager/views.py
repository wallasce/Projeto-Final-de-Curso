from django.shortcuts import render
from django.http import HttpResponse

from ClientOPC.OPCClientUA import OPCClientUA

# Create your views here.
async def getHistoryData(variable : str) -> dict:
    client = OPCClientUA()
    await client.connect()
    
    if (variable == 'temperature'):
        historyData = await client.getHistoryDataFrom('temperature')
        
    await client.disconnect()

    return historyData

async def getHistoryTemperature(request):
    fileData = await getHistoryData('temperature')

    response = HttpResponse(fileData, content_type='application/text charset=utf-8')
    response['Content-Disposition'] = 'attachment; filename="HistoryTemperature.txt"'
    return response