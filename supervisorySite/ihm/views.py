from django.shortcuts import render, redirect
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from ClientOPC.OPCClientUA import OPCClientUA
from asyncua import ua
from Controller.form import ControllerForm
from .forms.ihm.ModeForm import ModeForm
from .forms.ihm.VoltageForm import VoltageForm
from Settings.getEndPoint import getEndPoint

# Create your views here.
async def Supervisory(request):   
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

        await client.disconnect()  # Throws a exception if connection is lost
    except (ConnectionError, ua.UaError):
        return redirect("/error")
             
    controllerForm = ControllerForm()
    modeForm = ModeForm()
    voltageForm = VoltageForm()
    
    parameters = {
        'controllerForm' : controllerForm,
        'modeForm' : modeForm,
        'voltageForm' : voltageForm,
        'temperature' : temperature,
        'mode' : mode,
        'voltage' : voltage,
        'setPoint' : setPoint,
        'ki' : ki,
        'kp' : kp,
    }

    return render(request, "ihm/supervisory.html", parameters)
