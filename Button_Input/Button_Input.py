from gpiozero import LED, Button
from signal import pause
import os

red = LED(18) # this is saying the red LED is connected to pin 18 on the raspberry pi
yellow = LED(23) # this is saying the yellow LED is connected to pin 23 on the raspberry pi
green = LED(24) # this is saying the green LED is connected to pin 24 on the raspberry pi
button = Button(25) # this is saying the button is connected to pin 25 on the raspberry pi

os.system('clear') # Clears the screen

print ("Press the Button to turn the LED on and off")

button.when_pressed = red.on
button.when_released = red.off
