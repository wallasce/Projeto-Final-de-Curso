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
            await OPCServerUA.setVoltage(float(temperature*0.1))
            
            cls()
            print("setPoint: " + str(await OPCServerUA.setPoint.read_value()))
            print("Ki: " + str(await OPCServerUA.ki.read_value()))
            print("Kp: " + str(await OPCServerUA.kp.read_value()))
            print("Mode: " + str(await OPCServerUA.mode.read_value()))
            print("Voltage: " + str(await OPCServerUA.voltage.read_value()))
            print("Temperature: " + str(await OPCServerUA.temperature.read_value()))
            
            count += 1
            
            temperature = temperature + 1 if (temperatureUp) else temperature - 1

            if temperature == 100:
                temperatureUp = False
            elif temperature == 0:
                temperatureUp = True

            if (count == 601):
                return 0

asyncio.run(main())