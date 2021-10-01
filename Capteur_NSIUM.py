#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import ColorSensor
from pybricks.parameters import Port, Color

ev3 = EV3Brick()
capteur = ColorSensor(Port.S3)

def detection(x):
    while not False:
        if capteur.color() == x:
            ev3.speaker.beep()