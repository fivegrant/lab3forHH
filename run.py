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
temp = int(convert_voltage_to_temp(convert_raw_reading(q, rg), 9800,5))

display = lights.Lineup((11, 13, 15, 16, 18))

if sys.argv[1] == 'meter':
    min, max = (20,35)
    limits = (min,(min + ((min+max)/2))/2,(min+max)/2, 
     (max + ((min+max)/2))/2, max)
    while True:
        temp = int(convert_voltage_to_temp(convert_raw_reading(\
         get_raw_adc_reading(bus), rg), 9800,5))
        for i in range(1,6):
            display.darken(i)
        generator = 1
        catch = True
        for bar in limits:
            if temp <= bar:
                for i in range(1, generator):
                    display.luminate(i)   
                catch = False
                break
            generator += 1
        if catch:
            for i in range(1,6):
                display.luminate(i)
        
elif sys.argv[1] == 'dark':
    for i in range(1,6):
        display.darken(i)   
    for i in range(1,6):
        display.luminate(i)
        time.sleep(.3)
        display.darken(i)   

elif sys.argv[1] == 'bulb':
        which = int(sys.argv[2])
        display.luminate(which)
        time.sleep(1.5)
        display.darken(which)   
    
else:
    while True:
        temp = int(convert_voltage_to_temp(convert_raw_reading(\
         get_raw_adc_reading(bus), rg), 9800,5))
        show = bin(temp)[2:]
        print(show)
        for i in range(1,6):
            display.luminate(i)
            time.sleep(.1)
            display.darken(i)   
        print('-')
        for value in show:
            print(value)
            if int(value) == 1: 
                display.luminate(1)
                time.sleep(1)
                display.darken(1)
                time.sleep(1)
            else:
                display.luminate(2)
                time.sleep(1)
                display.darken(2)
                time.sleep(1)
        for i in range(1,6):
            display.luminate(i)
            time.sleep(.1)
            display.darken(i)   


