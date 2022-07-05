bin_d = '0001'
dec_d = '1'

def bin2dec(val):
    return int(val,2)

def dec2bin(val):
    return bin(val).replace("0b", "")

print(dec2bin(dec_d))
print(bin2dec(bin_d))
