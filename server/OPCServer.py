from asyncua import Server, uamethod, ua
from asyncua.server.history_sql import HistorySQLite

from SQLiteManager import SQLiteManager
from FormaterData import formaterData

# Method to do a query in a dump with history data.
@uamethod
def getHistoryData(parent, table : str) -> dict:
    sqlConnection = SQLiteManager('history_data.sql')
    answer = sqlConnection.selectDataFrom(table)
    sqlConnection.stopConnection()

    formater = formaterData()
    answer = formater.getFormatedData(answer)
    
    return answer

class OPCServer:
    #hostname -I
    #endpoint = "opc.tcp://192.168.0.2:4840/freeopcua/server/"
    endpoint = "opc.tcp://0.0.0.0:4840/freeopcua/server/"
    uri = "Camera Termoeletricamente Controlada"

    def __init__(self) -> None:
        self.server = Server()
        self.server.iserver.history_manager.set_storage(HistorySQLite("history_data.sql"))
        
        # Default value from Arduino
        self.previousKi = 4.5
        self.previousKp = 1.8
        self.previousMode = 'A'
        self.previousSetPoint = 20

    async def startServer(self) -> None :
        # Setup server.
        await self.server.init()
        self.server.set_endpoint(self.endpoint)
        
        sqlConnection = SQLiteManager('history_data.sql')
        sqlConnection.clearData()

        # Setup Namespace
        self.idx = await self.server.register_namespace(self.uri)

    async def createVariables(self) -> None:
        # Populate space.
        self.box = await self.server.nodes.objects.add_object(self.idx, "Box")

        self.ki = await self.box.add_variable(self.idx, "Ki", 4.5)
        self.kp = await self.box.add_variable(self.idx, "Kp", 1.8)
        self.mode = await self.box.add_variable(self.idx, "Mode", 'A')
        self.setPoint = await self.box.add_variable(self.idx, "SetPoint", 20.0)
        self.temperature = await self.box.add_variable(self.idx, "Temperature", 0.0)
        self.voltage = await self.box.add_variable(self.idx, "Voltage", 0.0)

        # Set some variables to be writable by clients.
        await self.ki.set_writable()
        await self.kp.set_writable()
        await self.mode.set_writable() 
        await self.setPoint.set_writable()
        await self.voltage.set_writable()

        # Add temperature to historic.
        varToHistorize = [self.temperature, self.voltage, self.setPoint]
        await self.server.historize_node_data_change(varToHistorize, period=None, count=1200)

    async def createFunctions(self) -> None:
        await self.box.add_method(self.idx, "getHistoryData", getHistoryData, [], [])

    async def getSetPoint(self) -> float:
        return await self.setPoint.read_value()
    
    async def getMode(self) -> str:
        return (await self.mode.read_value())
    
    async def getVoltage(self) -> float:
        return (await self.voltage.read_value())
    
    # Return a tuple with (ki, kp).
    async def getController(self) -> tuple:
        return (await self.ki.read_value(), await self.kp.read_value())

    # Only update the value if the client did't update this value.
    # Case don't update returns false
    async def setMode(self, mode) -> None:
        await self.mode.write_value(mode)
    
    async def setTemperature(self, temperature) -> None:
        await self.temperature.write_value(temperature)

    # Only update the value if the client did't update this value.
    # Case don't update returns false
    async def setSetPoint(self, setPoint) -> None:
        await self.setPoint.write_value(setPoint)
        
    async def setVoltage(self, voltage) -> None:
        await self.voltage.write_value(voltage)

    async def print(self) -> None:
        print("Server OPC: ")
        print("setPoint: " + str(await self.setPoint.read_value()))
        print("Ki: " + str(await self.ki.read_value()))
        print("Kp: " + str(await self.kp.read_value()))
        print("Mode: " + str(await self.mode.read_value()))
        print("Voltage: " + str(await self.voltage.read_value()))