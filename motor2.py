from gpiozero import Motor
from time import sleep
m1=Motor(14,15) # Create 1st motor, connected to pins GPIO 20 and 21
m2=Motor(3,4) # Create 2nd motor, connected to pins GPIO 3 and 4

def f(speed): # define function to move forward at speed
    m1.forward(speed)
    m2.forward(speed)

def b(speed):  # define function to move backwards at speed
    m1.backward(speed)
    m2.backward(speed)

def l(speed):  # define function to move left speed
    m1.backward(speed)
    m2.forward(speed)

def r(speed):  # define function to move right at speed
    m1.forward(speed)
    m2.backward(speed)

def s(): # define function stop both motors
    m1.stop()
    m2.stop()

# Main code
f(0.5) # move forward at half max speed
sleep(3) # wait 3 seconds
b(0.5) # move back at half max speed
sleep(3)
l(0.5) 
sleep(3)
r(0.5)
sleep(3)
s()
