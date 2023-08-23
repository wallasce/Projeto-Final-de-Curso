from django.shortcuts import render
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from ClientOPC.OPCClientUA import OPCClientUA
from .form import ControlerForm

# Create your views here.
async def Supervisory(request):    
    client = OPCClientUA()
    await client.connect()

    temperature = await client.getTemperature()
    mode = await client.getMode()
    voltage = await client.getVoltage()
    setPoint = await client.getSetPoint()
    ki = await client.getKi()
    kp = await client.getKp()

    await client.disconnect()

    controlerForm = ControlerForm()
    
    parameters = {
        'controlerForm' : controlerForm,
        'temperature' : temperature,
        'mode' : mode,
        'voltage' : voltage,
        'setPoint' : setPoint,
        'ki' : ki,
        'kp' : kp,
    }

    return render(request, "ihm/supervisory.html", parameters)
