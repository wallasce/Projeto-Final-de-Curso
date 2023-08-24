from asyncua import Client

class OPCClientUA:
    url = "opc.tcp://localhost:4840/freeopcua/server/"
    namespace = "Camera Termoeletricamente Controlada"

    def __init__(self):
        self.client = None
        self.nsidx = None

    async def connect(self):
        self.client = Client(url = self.url)
        await self.client.connect()
        self.nsidx = await self.client.get_namespace_index(self.namespace)

    async def disconnect(self):
        await self.client.disconnect()
    
    # Getters.
    async def getTemperature(self) -> float:
        temperature = await self.client.nodes.root.get_child(
            ["0:Objects", f"{self.nsidx}:Box", f"{self.nsidx}:Temperature"]
        )

        return await temperature.read_value()

    async def getMode(self) -> str:
        mode = await self.client.nodes.root.get_child(
            ["0:Objects", f"{self.nsidx}:Box", f"{self.nsidx}:Mode"]
        )

        return await mode.read_value()
    
    async def getVoltage(self) -> float:
        voltage = await self.client.nodes.root.get_child(
            ["0:Objects", f"{self.nsidx}:Box", f"{self.nsidx}:Voltage"]
        )

        return await voltage.read_value()
    
    async def getSetPoint(self) -> float:
        setPoint = await self.client.nodes.root.get_child(
            ["0:Objects", f"{self.nsidx}:Box", f"{self.nsidx}:SetPoint"]
        )

        return await setPoint.read_value()
    
    async def getKi(self) -> float:
        ki = await self.client.nodes.root.get_child(
            ["0:Objects", f"{self.nsidx}:Box", f"{self.nsidx}:Ki"]
        )

        return await ki.read_value()
    
    async def getKp(self) -> float:
        kp = await self.client.nodes.root.get_child(
            ["0:Objects", f"{self.nsidx}:Box", f"{self.nsidx}:Kp"]
        )

        return await kp.read_value()
    
    # Setters.
    async def setSetPoint(self, setPoint : float) -> None:
        setPointVar = await self.client.nodes.root.get_child(
            ["0:Objects", f"{self.nsidx}:Box", f"{self.nsidx}:SetPoint"]
        )
        await setPointVar.write_value(setPoint)

    async def setKi(self, ki : float) -> None:
        kiVar = await self.client.nodes.root.get_child(
            ["0:Objects", f"{self.nsidx}:Box", f"{self.nsidx}:Ki"]
        )
        await kiVar.write_value(ki)

    async def setKp(self, kp : float) -> None:
        kpVar = await self.client.nodes.root.get_child(
            ["0:Objects", f"{self.nsidx}:Box", f"{self.nsidx}:Kp"]
        )
        await kpVar.write_value(kp)