from django.shortcuts import render, HttpResponse
import json

from .OPCClientUA import OPCClientUA

# Create your views here.
async def getOPCValues(request):
    client = OPCClientUA()
    await client.connect()

    temperature = await client.getTemperature()
    mode = await client.getMode()
    voltage = await client.getVoltage()
    setPoint = await client.getSetPoint()
    ki = await client.getKi()
    kp = await client.getKp()

    await client.disconnect()
    response = json.dumps({
        'temperature' : temperature,
        'mode' : mode,
        'voltage' : voltage,
        'setPoint' : setPoint,
        'ki' : ki,
        'kp' : kp,
    })

    return HttpResponse(response)

async def setOPCSetPoint(request):
    client = OPCClientUA()
    await client.connect()

    newSetPoint = float(request.body)
    await client.setSetPoint(newSetPoint)

    await client.disconnect()
    
    return HttpResponse(request)