from gpiozero import LED, Button
from signal import pause
import os

red = LED(18)
yellow = LED(23)
green = LED(24)
button = Button(25)

print ("What LED would you like to turn on? ")
print ("1: red?")
print ("2: yellow?")

choice = input("What LED would you like to turn on?")

choice = int(choice)

if choice == 1:
    print ("You picked the red LED")
    LEDChoice = red

if choice == 2:
    print ("You picked the Yellow LED")
    LEDChoice = yellow


button.when_pressed = LEDChoice.on
button.when_released = LEDChoice.off

pause()
