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
        print(f"Namespace Index for '{self.namespace}': {self.nsidx}")

    async def disconnect(self):
        await self.client.disconnect()
    
    async def getTemperature(self) -> float:
        temperature = await self.client.nodes.root.get_child(
            ["0:Objects", f"{self.nsidx}:Box", f"{self.nsidx}:Temperature"]
        )

        return await temperature.read_value()