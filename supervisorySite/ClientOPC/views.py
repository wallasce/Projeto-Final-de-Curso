from django.shortcuts import render, HttpResponse
import json

from .OPCClientUA import OPCClientUA
from asyncua import ua
from asyncio import TimeoutError
from Settings.getEndPoint import getEndPoint

# Create your views here.
async def getOPCValues(request):
    try:
        endPoint = await getEndPoint()
        
        client = OPCClientUA(endPoint) if endPoint else OPCClientUA()
        await client.connect()

        temperature = await client.getTemperature()
        mode = await client.getMode()
        voltage = await client.getVoltage()
        setPoint = await client.getSetPoint()
        ki = await client.getKi()
        kp = await client.getKp()

        await client.disconnect()
    except (ConnectionError, ua.UaError, TimeoutError):
        response = HttpResponse()
        response.status_code = 500
        return response
    
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
    try:
        endPoint = await getEndPoint()
        
        client = OPCClientUA(endPoint) if endPoint else OPCClientUA()
        await client.connect()

        if (varOPC == 'setPoint'):
            await client.setSetPoint(value)
        elif (varOPC == 'ki'):
            await client.setKi(value)
        elif (varOPC == 'kp'):
            await client.setKp(value)
        elif (varOPC == 'mode'):
            await client.setMode(value)
        elif (varOPC == 'voltage'):
            await client.setVoltage(value)    

        await client.disconnect()
    except (ConnectionError, ua.UaError, TimeoutError):
        response = HttpResponse()
        response.status_code = 500
        return response

async def setOPCSetPoint(request):
    await setValue('setPoint', float(request.body))
    
    return HttpResponse(request)

async def setOPCKi(request):
    await setValue('ki', float(request.body))
    
    return HttpResponse(request)

async def setOPCKp(request):
    await setValue('kp', float(request.body))
    
    return HttpResponse(request)

async def setOPCMode(request):
    await setValue('mode', request.body.decode('utf-8'))
    
    return HttpResponse(request)

async def setOPCVoltage(request):
    await setValue('voltage', float(request.body))
    
    return HttpResponse(request)