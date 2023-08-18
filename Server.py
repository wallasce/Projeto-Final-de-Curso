import asyncio
import threading

from dataAcquisitionFinal import dataAcquisition
from OPCServer import OPCServer

# Global variables.
global flag

async def thOPCServer():
    OPCServerUA = OPCServer()
    await OPCServerUA.startServer()
    await OPCServerUA.createVariables()
    
    async with OPCServerUA.server:
        while (flag):
            await asyncio.sleep(1)

            # Try update mode value in OPC server, else update the value in Arduino
            if not (await OPCServerUA.setMode(dataManager.getLastMode)):
                dataManager.setMode()
                await OPCServerUA.updatePreviousModeValue()

            # Try update SetPoint value in OPC server, else update the value in Arduino
            if not (await OPCServerUA.setSetPoint(dataManager.getLastSetPoint)):
                dataManager.setSetPoint(await OPCServerUA.getSetPoint())
                await OPCServerUA.updatePreviousSetPointValue()

            await OPCServerUA.setTemperature(dataManager.getLastTemperature)
            await OPCServerUA.setVoltage(dataManager.getLastVoltage)

            # Checks if client update controler values.
            if (await OPCServerUA.controlerChange()):
                controler = await OPCServerUA.getControler()
                dataManager.setControler(controler[0], controler[1])
                await OPCServerUA.updatePreviousControler()

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