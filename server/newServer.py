import asyncio
import os

from dataAcquisitionFinal import dataAcquisition
from OPCServer import OPCServer

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

async def main():
    dataManager = dataAcquisition()

    OPCServerUA = OPCServer()
    await OPCServerUA.startServer()
    await OPCServerUA.createVariables()
    await OPCServerUA.createFunctions()

    async with OPCServerUA.server:
        while(True):
            await asyncio.sleep(0.5)

            dataManager.readData()

            await OPCServerUA.setTemperature(dataManager.getTemperature())

            mode = await OPCServerUA.getMode()

            if (dataManager.getMode() != mode):
                    dataManager.setMode()
            
            if (mode == 'A'):
                controller = await OPCServerUA.getController()
                
                dataManager.setSetPoint(await OPCServerUA.getSetPoint())
                dataManager.setController(controller[0], controller[1])

                await OPCServerUA.setVoltage(dataManager.getVoltage())
            elif (mode == 'M'):
                dataManager.setSetPoint(await OPCServerUA.getVoltage())

            cls()
            OPCServerUA.print()
            print("")
            dataManager.print()
            
                