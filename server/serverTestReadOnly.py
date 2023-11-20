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
        while (True):
            await asyncio.sleep(1)
            
            cls()
            await OPCServerUA.print()
            
            count += 1
            if (count == 601):
                return 0

asyncio.run(main())