from django.shortcuts import render
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from ClientOPC.OPCClientUA import OPCClientUA

# Create your views here.
async def Supervisory(request):
    client = OPCClientUA()
    await client.connect()
    temperature = await client.getTemperature()
    await client.disconnect()

    return render(request, "ihm/supervisory.html", {"temperature" : temperature})
