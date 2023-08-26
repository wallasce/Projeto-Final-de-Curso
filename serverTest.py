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

            print("Temperature: " + str(temperature))
            temperature += 1
            await OPCServerUA.setSetPoint(float(setPoint))
            #await OPCServerUA.setVoltage(float(temperature*0.1))
            await OPCServerUA.setMode(mode)
            await OPCServerUA.setTemperature(float(temperature))
            print("setPoint: " + str(await OPCServerUA.setPoint.read_value()))
            print("Ki: " + str(await OPCServerUA.ki.read_value()))
            print("Kp: " + str(await OPCServerUA.kp.read_value()))
            print("Mode: " + str(await OPCServerUA.mode.read_value()))
            print("Voltage: " + str(await OPCServerUA.voltage.read_value()))

asyncio.run(main())