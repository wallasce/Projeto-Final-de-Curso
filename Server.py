import time
import threading

from dataAcquisitionFinal import dataAcquisition
from OPCServer import OPCServer

# Global variables.
global flag

def thOPCServer():
    OPCServerUA = OPCServer()
    OPCServerUA.createVariables()
    OPCServerUA.serverRun()
    
    while (flag):
        time.sleep(1)
        OPCServerUA.setMode(dataManager.getLastMode)
        OPCServerUA.setSetPoint(dataManager.getLastSetPoint)
        OPCServerUA.setTemperature(dataManager.getLastTemperature)
        OPCServerUA.setVoltage(dataManager.getLastVoltage)

    OPCServerUA.serverStop()

def thDataAcquisition():
    global dataManager
    dataManager = dataAcquisition()
    
    while (flag):
        time.sleep(1)
        dataManager.readData()

    dataManager.close()

flag = 1

threadDataAquisition = threading.Thread(target = thDataAcquisition, args = ())
threadOPCServer = threading.Thread(target = thOPCServer, args = ())

threadDataAquisition.start()
threadOPCServer.start()

keyboardInput = ''
while (keyboardInput != 'exit'):
    keyboardInput = input('To stop the program, type exit')
# Break thread's loap
flag = 0