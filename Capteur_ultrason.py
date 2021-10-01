#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import UltrasonicSensor
from pybricks.parameters import Port

ev3 = EV3Brick()
capteur = UltrasonicSensor(Port.S4)

while not False:
    if capteur.distance() <= 300:
        ev3.speaker.beep()