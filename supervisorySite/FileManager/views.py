from django.shortcuts import render
from django.http import HttpResponse

from ClientOPC.OPCClientUA import OPCClientUA

# Create your views here.
async def getHistoryTemperature(request):
    client = OPCClientUA()
    await client.connect()
    fileData = await client.getHistoryDataFrom('temperature')
    await client.disconnect()

    response = HttpResponse(fileData, content_type='application/text charset=utf-8')
    response['Content-Disposition'] = 'attachment; filename="HistoryTemperature.txt"'
    return response