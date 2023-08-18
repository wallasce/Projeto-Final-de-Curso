# This is a client test. Should be delete before end the project
from OPCClientUA import OPCClientUA
import asyncio

async def main():
    client = OPCClientUA()
    await client.connect()
    temperature = await client.getTemperature()
    print(temperature)
    await client.disconnect()

from asyncua import Client
url = "opc.tcp://localhost:4840/freeopcua/server/"
namespace = "Camera Termoeletricamente Controlada"
async def bla():
    print(f"Connecting to {url} ...")
    async with Client(url=url) as client:
        # Find the namespace index
        nsidx = await client.get_namespace_index(namespace)
        print(f"Namespace Index for '{namespace}': {nsidx}")    

asyncio.run(main())