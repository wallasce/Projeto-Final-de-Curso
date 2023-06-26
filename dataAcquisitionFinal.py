import serial
from threading import Lock

class dataAcquisition:
    port = "/dev/ttyUSB0"
    temperature = []
    mode = ''
    setPoint = []
    voltage = []

    # Constructor
    def __init__(self) -> None:
        self.serialConection = serial.Serial(self.port, 9600)
        self.mutex = Lock()

    def close(self) -> None:
        self.serialConection.close()

    # Read and Decode Data from Serial
    def readData(self) -> None:
        data = self.serialConection.readline()
        data = data.decode().split( )
        
        self.mutex.acquire()
        self.temperature.append(data[4])
        self.setPoint.append(data[5])
        self.voltage.append(data[6])

        if (mode != data[7]) :
            mode = data[7]
        self.mutex.release()

    # Getters.
    def getLastTemperature(self) -> float:
        self.mutex.acquire()
        value = self.temperature[-1]
        self.mutex.release()
        return value

    
    def getLastMode(self) -> float:
        self.mutex.acquire()
        value = self.mode[-1]
        self.mutex.release()
        return value
    
    def getLastSetPoint(self) -> float:
        self.mutex.acquire()
        value = self.setPoint[-1]
        self.mutex.release()
        return value
    
    def getLastVoltage(self) -> float:
        self.mutex.acquire()
        value = self.voltage[-1]
        self.mutex.release()
        return value