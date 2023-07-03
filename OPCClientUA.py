from asyncua import Client
import asyncio
import sys

sys.path.insert(0, "..")

# Get Server End Point.
url = "opc.tcp://192.168.0.3:4840/freeopcua/server/"
namespace = "Camera Termoeletricamente Controlada"

async def main():
    async with Client(url = url) as client:
        nsidx = await client.get_namespace_index(namespace)

        # Get the variable node for read / write
        mode = await client.nodes.root.get_child(
            ["0:Objects", f"{nsidx}:Box", f"{nsidx}:Mode"]
        )
        setPoint = await client.nodes.root.get_child(
            ["0:Objects", f"{nsidx}:Box", f"{nsidx}:SetPoint"]
        )
        temperature = await client.nodes.root.get_child(
            ["0:Objects", f"{nsidx}:Box", f"{nsidx}:Temperature"]
        )
        voltage = await client.nodes.root.get_child(
            ["0:Objects", f"{nsidx}:Box", f"{nsidx}:Voltage"]
        )

        await asyncio.sleep(5)
        print("Mode: " + str(await mode.read_value()))
        await mode.write_value(1)
        await asyncio.sleep(5)
        print("Mode: " + str(await mode.read_value()))
        await mode.write_value(0)
        while (True):
            await asyncio.sleep(2)
            print("Temperature: " + str(await temperature.read_value()))

asyncio.run(main())