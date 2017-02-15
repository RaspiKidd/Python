from gpiozero import LED
from time import sleep
import os

red = LED(18) # this is saying the red LED is connected to pin 18 on the raspberry pi
yellow = LED(23) # this is saying the yellow LED is connected to pin 23 on the raspberry pi
green = LED(24) # this is saying the green LED is connected to pin 24 on the raspberry pi

os.system('clear') # Clears the screen

print ("Which LED would you like to blink")
print ("1: Red?")
print ("2: Yellow?")

# Prints prompts to the screen and waits for input from the user
led_choice = input ("Choose your option: ")
count = input ("How many times would you like it to blink? ")

# Convert user input from string (text) to integer (number)
led_choice = int(led_choice)
count = int(count)

# Set the LEDChoice variable depending on the led_choice
if led_choice == 1:
    print ("You picked the Red LED")
    LEDChoice = red
if led_choice == 2:
    print ("You have picked the Yellow LED")
    LEDChoice = yellow

# if we have chosen a valid choice, flash the LED 
if LEDChoice>0:
    while count > 0:
    LEDChoice.on()
    sleep (1)
    LEDChoice.off()
    sleep(1)
    count = count -1