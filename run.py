#!/usr/bin/python3
from configure import *
import lights, sys, time

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
print(convert_voltage_to_temp(convert_raw_reading(q, rg), 9800,5))

display = lights.Lineup((11, 13, 15, 16, 18))
if sys.argv[1] == 'meter':
    min, max = (4600, 17050)
    
    while True:
        
elif sys.arg[1] == 'dark':
    for i in range(6):
        display.darken(i)   
     for i in range(6):
        display.luminate(i)
        time.sleep(.23)
        display.darken(i)   
    
else:
    while True:
