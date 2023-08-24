# This is a server only to test the client. Should be delete before end the project
import asyncio

from OPCServer import OPCServer

async def main():
    OPCServerUA = OPCServer()
    await OPCServerUA.startServer()
    await OPCServerUA.createVariables()
    temperature = 0
    mode = 'M'
    setPoint = 5

    async with OPCServerUA.server:
        while (temperature < 100):
            await asyncio.sleep(1)

            if (temperature % 10 == 0):
                mode = 'A' if mode == 'M' else 'M'
                setPoint += 5

            print(temperature)
            temperature += 1
            await OPCServerUA.setSetPoint(float(setPoint))
            await OPCServerUA.setVoltage(float(temperature*0.1))
            await OPCServerUA.setMode(mode)
            await OPCServerUA.setTemperature(float(temperature))
            print(await OPCServerUA.setPoint.read_value())

asyncio.run(main())