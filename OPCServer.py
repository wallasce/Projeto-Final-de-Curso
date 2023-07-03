from asyncua import Server, ua

class OPCServer:
    #hostname -I
    endpoint = "opc.tcp://192.168.0.3:4840/freeopcua/server/"
    uri = "Camera Termoeletricamente Controlada"

    async def __init__(self) -> None:
        # Setup server.
        self.server = Server()
        await self.server.init()
        self.server.set_endpoint(self.endpoint)
        self.previousMode = 'A'
        self.previousSetPoint = 0

        # Setup Namespace
        self.idx = await self.server.register_namespace(self.uri)

    async def createVariables(self) -> None:
        # Populate space.
        self.box = await self.server.nodes.objects.add_object(idx, "Box")

        self.mode = await self.box.add_variable(self.idx, "Mode", 'A')
        self.setPoint = await self.box.add_variable(self.idx, "SetPoint", 0)
        self.temperature = await self.box.add_variable(self.idx, "Temperature", 0)
        self.voltage = await self.box.add_variable(self.idx, "Voltage", 0)

        # Set some variables to be writable by clients.
        await self.mode.set_writable() 
        await self.setPoint.set_writable()

    # Only update the value if the client did't update this value.
    # Case don't update returns false
    async def setMode(self, mode) -> bool:
        if (self.previousMode == await self.mode.get_value()):
            await self.mode.write_value(mode)
            return True
        else:
            return False
    
    async def setTemperature(self, temperature) -> None:
        await self.temperature.write_value(temperature)

    # Only update the value if the client did't update this value.
    # Case don't update returns false
    async def setSetPoint(self, setPoint) -> bool:
        if (self.previousSetPoint == await self.setPoint.get_value()):
            await self.setPoint.write_value(setPoint)
            return True
        else:
            return False
        
    async def setVoltage(self, voltage) -> None:
        await self.voltage.write_value(voltage)
