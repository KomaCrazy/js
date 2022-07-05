
from tools import *
from crc16_c import *
data = ([0x01,0x02,0x03])

crc = crc16_f(data)
print(crc)
hex_int = int(crc, 16)
new_int = hex_int + 0x200
data.append(new_int)

while True:
        print(bytes(data))
        s1()