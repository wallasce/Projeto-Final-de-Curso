from opcua import ua, Server
import time

class OPCServer:
    #hostname -I
    endpoint = "opc.tcp://192.168.0.3:4840/freeopcua/server/"
    uri = "Camera Termoeletricamente Controlada"

    def __init__(self) -> None:
        # Setup server.
        self.server = Server()
        self.server.set_endpoint(self.endpoint)
        self.previousMode = 'A'
        self.previousSetPoint = 0

        # Setup Namespace
        self.idx = self.server.register_namespace(self.uri)

    def createVariables(self) -> None:
        # Get Objects Node.
        objects = self.server.get_objects_node()

        # Populate space.
        self.box = objects.add_object(self.idx, "Box")

        self.mode = self.box.add_variable(self.idx, "Mode", 0)
        self.setPoint = self.box.add_variable(self.idx, "SetPoint", 0)
        self.temperature = self.box.add_variable(self.idx, "Temperature", 0)
        self.voltage = self.box.add_variable(self.idx, "Voltage", 0)

        # Set some variables to be writable by clients.
        self.mode.set_writable() 
        self.setPoint.set_writable()

    def serverRun(self) -> None:
        self.server.start()

    def serverStop(self) -> None:
        self.server.stop()

    # Only update the value if the client did't update this value.
    # Case don't update returns false
    def setMode(self, mode) -> bool:
        if (self.previousMode == self.mode.get_value()):
            self.mode.set_value(mode)
            return True
        else:
            return False
    
    def setTemperature(self, temperature) -> None:
        self.temperature.set_value(temperature)

    # Only update the value if the client did't update this value.
    # Case don't update returns false
    def setSetPoint(self, setPoint) -> bool:
        if (self.previousSetPoint == self.setPoint.get_value()):
            self.setPoint.set_value(setPoint)
            return True
        else:
            return False
        
    def setVoltage(self, voltage) -> None:
        self.voltage.set_value(voltage)
