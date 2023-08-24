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

async def setValue(varOPC : str, value : float) -> None:
    client = OPCClientUA()
    await client.connect()

    if (varOPC == 'setPoint'):
        await client.setSetPoint(value)

    await client.disconnect()

async def setOPCSetPoint(request):
    await setValue('setPoint', float(request.body))
    
    return HttpResponse(request)