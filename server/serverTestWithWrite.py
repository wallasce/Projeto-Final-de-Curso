# This is a server only to test the client.
# This server don't write any variable.
# Works for 10 minutes.
import asyncio
import os

from OPCServer import OPCServer

def cls():
    os.system('cls' if os.name=='nt' else 'clear')


async def main():
    OPCServerUA = OPCServer()
    await OPCServerUA.startServer()
    await OPCServerUA.createVariables()
    await OPCServerUA.createFunctions()

    count = 0
    temperature = 0
    temperatureUp = True

    async with OPCServerUA.server:
        while (True):
            await asyncio.sleep(1)
            await OPCServerUA.setTemperature(float(temperature))
            if (await OPCServerUA.getMode() == 'A'):
                await OPCServerUA.setVoltage(float(temperature*0.1))
            
            cls()
            await OPCServerUA.print()
            
            temperature = temperature + 1 if (temperatureUp) else temperature - 1
            if temperature == 100:
                temperatureUp = False
            elif temperature == 0:
                temperatureUp = True

            count += 1
            if (count == 601):
                return 0

asyncio.run(main())