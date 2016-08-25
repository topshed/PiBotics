from gpiozero import Motor
from time import sleep
m1=Motor(20,21) # Create our motor, connected to pins GPIO 20 and 21

m1.forward(0.5) # Move forward at half max speed
sleep(3) # wait for 3 seconds
m1.stop() # Stop the motor
