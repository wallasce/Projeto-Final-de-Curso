from asyncua import Client, ua

class OPCClientUA:
    namespace = "Camera Termoeletricamente Controlada"

    def __init__(self, endpoint = "localhost:4840"):
        self.url = "opc.tcp://" + endpoint + "/freeopcua/server/"
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

    async def setMode(self, mode : str) -> None:
        modeVar = await self.client.nodes.root.get_child(
            ["0:Objects", f"{self.nsidx}:Box", f"{self.nsidx}:Mode"]
        )
        await modeVar.write_value(mode)

    async def setVoltage(self, voltage : float) -> None:
        voltageVar = await self.client.nodes.root.get_child(
            ["0:Objects", f"{self.nsidx}:Box", f"{self.nsidx}:Voltage"]
        )

        if (voltage > 12):
            voltage = 12.0
        elif (voltage < -12):
            voltage = -12.0
        await voltageVar.write_value(voltage)

    # The table in Server Database follows this standard <namespaceID>_<varID>
    # This functions get these ids and return the table name.
    def OPCVarToTableName(self, OPCVar : list[ua.NodeClass] | ua.NodeClass) -> str:
        namespaceId = str(OPCVar.nodeid.NamespaceIndex)
        varId = str(OPCVar.nodeid.Identifier)
        return namespaceId + "_" + varId 

    async def getHistoryDataFrom(self, variable : str) -> None:
        if variable == "temperature":
            OPCVar = await self.client.nodes.root.get_child(
                ["0:Objects", f"{self.nsidx}:Box", f"{self.nsidx}:Temperature"]
            )
        elif variable == "setPoint":
            OPCVar = await self.client.nodes.root.get_child(
                ["0:Objects", f"{self.nsidx}:Box", f"{self.nsidx}:SetPoint"]
            )
        elif variable == "voltage":
            OPCVar = await self.client.nodes.root.get_child(
                ["0:Objects", f"{self.nsidx}:Box", f"{self.nsidx}:Voltage"]
            )
        else:
            return 
        table = self.OPCVarToTableName(OPCVar) 
        
        box = await self.client.nodes.root.get_child(
            ["0:Objects", f"{self.nsidx}:Box"]
        )
        history = await box.call_method(f"{self.nsidx}:getHistoryData", table)
        return history