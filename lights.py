#!/usr/bin/python3
from RPi.GPIO import *

class Lineup:
    def __init__(self, pins):
        self.pins = pins
        setmode(BOARD)
        setwarnings(False)
        for pin in self.pins:
            setup(pin, OUT)
                    
    def luminate(self, pin):
        pin -= 1
        if input(self.pins[pin]) == 0:
            output(self.pins[pin],HIGH)

    def darken(self, pin):
        pin -= 1
        if input(self.pins[pin]) == 1:
            output(self.pins[pin],LOW)


