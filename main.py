#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
ev3 = EV3Brick()
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

def avancer(x) :
    robot.straight(x)

def reculer(x) :
    robot.straight(-x)

def droite(x):
    robot.turn(x)

def gauche(x):
    robot.turn(-x)