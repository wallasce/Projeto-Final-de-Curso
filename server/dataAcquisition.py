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

    def close(self) -> None:
        self.serialConection.close()

    # Read and Decode Data from Serial
    def readData(self) -> None:
        data = self.serialConection.readline()

        if b'endereco do sensor' in data:
            raise Exception('Error to find some of the sensors')

        data = data.decode().split( )
        
        self.temperature = float(data[4])
        self.setPoint = float(data[5])
        self.voltage = float(data[6])

        if (self.mode != data[7]) :
            self.mode = data[7]

    # Getters.
    def getTemperature(self) -> float:
        return self.temperature

    def getMode(self) -> float:
        return self.mode
    
    def getSetPoint(self) -> float:
        return self.setPoint
    
    def getVoltage(self) -> float:
        return self.voltage
    
    # Send to Arduino to change the Mode.
    def setMode(self) -> None:
        # Send a mensage with the standards implemented on Arduino.
        self.serialConection.write(b'MMF')

    # Remove first decimal place of absolute value.
    # Returns a String.
    def removeFirstDecimalPlace(self, value) -> str:
        value = int(abs(value) * 10)
        return str(value)

    def setSetPoint(self, setPoint) -> None:
        mesage = 'R'
        mesage = mesage + ('+' if setPoint > 0 else '-')
        
        mesage = mesage + self.removeFirstDecimalPlace(setPoint) + 'F'

        mesage = mesage.encode()
        self.serialConection.write(mesage)

    def setController(self, ki, kp) -> None:
        # Initial controller mesage standard.
        mesage = 'C'
        mesage = mesage + self.removeFirstDecimalPlace(kp)
        mesage = mesage + self.removeFirstDecimalPlace(ki)
        # End controller mesage standard.
        mesage = 'F'

        mesage = mesage.encode()
        self.serialConection.write(mesage)

    def print(self) -> None:
        print("Arduino Values: ")
        print("setPoint: " + str(self.setPoint))
        print("Mode: " + str(self.mode))
        print("Temperature: " + str(self.temperature))
        print("Voltage: " + str(self.voltage))