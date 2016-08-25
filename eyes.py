from gpiozero import DistanceSensor
from time import sleep
eyes = DistanceSensor(24,23) # create distance sensor connected to pins 23 & 24

print('start')

while True: # forever...
    if eyes.distance*100 <4:
        print('distance/in:-)='+ str(eyes.distance*100))
    else:
        print('distance/out:-(='+ str(eyes.distance*100))
    sleep(0.3)
