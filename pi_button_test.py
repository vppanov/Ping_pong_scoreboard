# import RPI.GPIO as GPIO  # for raspberry     pip install RPi.GPIO

# import RPI.GPIO as GPIO  # uncomment on raspberry
import gpio
import time
import turtle

gpio.setmode(gpio.BCM)
gpio.setup(26, gpio.IN)  # number of button and setup as input

while 1 == 1:
    turtle.forward(4)
    if gpio.input(26) == 1:
        turtle.right(12)
    time.sleep(0.2)


