from gpiozero import DistanceSensor
from threading import Thread
from gpiozero import Motor
from time import sleep
sleep(20)
eyes = DistanceSensor(24,23)
m1=Motor(20,21)
m2=Motor(3,4)
print('start')

def ouch(): # function to detect obstacles
    while moving:
        if eyes.distance*100 <8:
            print('distance/in:-)='+ str(eyes.distance*100))
            s()
        else:
            print('distance/out:-(='+ str(eyes.distance*100))
        sleep(0.3)

def f(speed): # Move the robot forwards
    print('foward')
    m1.forward(speed)
    m2.forward(speed)

def b(speed): # Move the robot backwards
    m1.backward(speed)
    m2.backward(speed)

def l(speed): # Move the robot left
    m1.backward(speed)
    m2.forward(speed)

def r(speed): # Move the robot right
    print('right')
    m1.forward(speed)
    m2.backward(speed)

def s():
    print('stop')
    m1.stop()
    m2.stop()

moving=True
eye=Thread(target=ouch) # create thread for ouch function
eye.start() # start thread
for i in range(5): # move in a square 5 times
    f(0.5)
    sleep(3)
    r(0.5)
    sleep(0.84)

moving=False
