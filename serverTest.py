# This is a server only to test the client. Should be delete before end the project
import asyncio

from OPCServer import OPCServer

async def main():
    OPCServerUA = OPCServer()
    await OPCServerUA.startServer()
    await OPCServerUA.createVariables()
    temperature = 0

    async with OPCServerUA.server:
        while (temperature < 100):
            await asyncio.sleep(1)
            print(temperature)
            temperature += 1
            await OPCServerUA.setTemperature(temperature)

asyncio.run(main())