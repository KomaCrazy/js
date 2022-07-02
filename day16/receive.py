import serial 
port_1 = serial.Serial(port="COM13",baudrate=9600)
while True:
    data = port_1.read()
    print(data)
