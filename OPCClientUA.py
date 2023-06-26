from opcua import Client
import sys
import time

sys.path.insert(0, "..")

# Get Server End Point.
client = Client("opc.tcp://admin@192.168.0.3:4840/freeopcua/server/")

try:
    client.connect()
    root = client.get_root_node()

    mode = root.get_child(["0:Objects", "2:Box", "2:Mode"])
    setPoint = root.get_child(["0:Objects", "2:Box", "2:SetPoint"])
    temperature = root.get_child(["0:Objects", "2:Box", "2:Temperature"])
    voltage = root.get_child(["0:Objects", "2:Box", "2:Voltage"])

    time.sleep(5)
    print("Mode: " + str(mode.get_value()))
    mode.set_value(1)
    time.sleep(5)
    print("Mode: " + str(mode.get_value()))
    mode.set_value(0)
    while (True):
        time.sleep(2)
        print("Temperature: " + str(temperature.get_value()))
finally:
    client.disconnect()