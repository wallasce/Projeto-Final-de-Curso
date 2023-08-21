from django.shortcuts import render, HttpResponse
import json

from .OPCClientUA import OPCClientUA

# Create your views here.
async def getOPCValues(request):
    client = OPCClientUA()
    await client.connect()

    temperature = await client.getTemperature()

    await client.disconnect()
    response = json.dumps({
        'temperature' : temperature,
    })

    return HttpResponse(response)