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
    def getLastControler(self) -> tuple:
        self.mutex.acquire()
        ki = 0
        kp = 0
        self.mutex.release()
        return (ki, kp)

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
    
    # Send to Arduino to change the Mode.
    def setMode(self) -> None:
        # Send a mensage with the standards implemented on Arduino.
        self.serialConection.write(b'MMF')

    # Remove first decimal place of absolute value.
    # Returns a String.
    def removeFirstDecimalPlace(value) -> str:
        value = int(abs(value) * 10)
        return str(value)

    def setSetPoint(self, setPoint) -> None:
        mesage = 'R'
        mesage = mesage + ('+' if setPoint > 0 else '-')
        
        mesage = mesage + self.removeFirstDecimalPlace(setPoint) + 'F'

        mesage = mesage.encode()
        self.serialConection.write(mesage)

    def setControler(self, kp, ki) -> None:
        # Initial controler mesage standard.
        mesage = 'C'
        mesage = mesage + self.removeFirstDecimalPlace(kp)
        mesage = mesage + self.removeFirstDecimalPlace(ki)
        # End controler mesage standard.
        mesage = 'F'

        mesage = mesage.encode()
        self.serialConection.write(mesage)
