from crc import CrcCalculator, Configuration
def crc16_f(data):
    width = 8
    poly=0x07
    init_value=0x00
    final_xor_value=0x00
    reverse_input=False
    reverse_output=False
    configuration = Configuration(width, poly, init_value, final_xor_value, reverse_input, reverse_output)
    use_table = True
    crc_calculator = CrcCalculator(configuration, use_table)

    checksum = crc_calculator.calculate_checksum(data)

    return hex(checksum)


