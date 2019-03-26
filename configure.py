#!/usr/bin/python3
# Five and Zak

from smbus import *

da = 0x48
configr= 0x01
conversionr= 0x00
cb = [0xC0, 0x83]
rg = 6.144


def configure_adc(my_bus, device_address, 
 config_register, conversion_register, config_bytes):
    my_bus.write_i2c_block_data(device_address,\
     config_register, config_bytes)
    
def get_raw_adc_reading(my_bus):
    raw_reading = my_bus.read_i2c_block_data(\
     da, conversionr)
    msb = raw_reading[0] << 8
    return msb + raw_reading[1]

def convert_raw_reading(raw_reading, rang):
    return raw_reading * (rang/32767)
    
def convert_voltage_to_temp(vout, r2, vin):
    r1 = ((vin*r2)/vout)-r2
    m, b = (-0.001565, 51.11)
    return r1 * m + b

# Delete the following later
"""
if __name__ == '__main__':
    #Necessary Variables
    da = 0x48
    configr= 0x01
    conversionr= 0x00
    cb = [0xC0, 0x83]
    rg = 6.144

    bus = SMBus(1)
    configure_adc(bus, da, configr, conversionr, cb)
    q = get_raw_adc_reading(bus)
    print(hex(q))
    print(convert_raw_reading(q, rg))
"""
