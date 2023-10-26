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
    async with OPCServerUA.server:
        while (count < 600):
            await asyncio.sleep(1)
            cls()
            print("setPoint: " + str(await OPCServerUA.setPoint.read_value()))
            print("Ki: " + str(await OPCServerUA.ki.read_value()))
            print("Kp: " + str(await OPCServerUA.kp.read_value()))
            print("Mode: " + str(await OPCServerUA.mode.read_value()))
            print("Voltage: " + str(await OPCServerUA.voltage.read_value()))

asyncio.run(main())