
from tools import *
from crc16_c import *
data = ([0x01,0x02,0x03])

crc = crc16_f(data)
print(crc)
while True:
        port_1.write(serial.to_bytes(da))
        s1()