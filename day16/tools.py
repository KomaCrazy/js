import time
import serial

path = './convert.txt'
port_1 = serial.Serial(port="COM11",baudrate=9600)




def s1():
    time.sleep(1)

def result(data,crc):
    print(bytes(data))
    crc = hex(int(crc,16))  
    return crc


