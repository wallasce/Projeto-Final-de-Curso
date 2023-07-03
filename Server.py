import asyncio
import threading

from dataAcquisitionFinal import dataAcquisition
from OPCServer import OPCServer

# Global variables.
global flag

async def thOPCServer():
    OPCServerUA = OPCServer()
    OPCServerUA.createVariables()
    
    while (flag):
        await asyncio.sleep(1)
        await OPCServerUA.setMode(dataManager.getLastMode)
        await OPCServerUA.setSetPoint(dataManager.getLastSetPoint)
        await OPCServerUA.setTemperature(dataManager.getLastTemperature)
        await OPCServerUA.setVoltage(dataManager.getLastVoltage)

async def thDataAcquisition():
    global dataManager
    dataManager = dataAcquisition()
    
    while (flag):
        await asyncio.sleep(1)
        dataManager.readData()

    dataManager.close()

flag = 1

threadDataAquisition = threading.Thread(target = thDataAcquisition, args = ())
threadOPCServer = threading.Thread(target = thOPCServer, args = ())

threadDataAquisition.start()
threadOPCServer.start()

keyboardInput = ''
while (keyboardInput != 'exit'):
    keyboardInput = input('To stop the program, type exit')
# Break thread's loap
flag = 0