from gpiozero import LED # importing the LED module from the gpiozero library

# The next 3 lines are telling the raspberry pi that we are using pin 18,23 and 24 as outputs.
# This means that we can turn the pins on and off.

red = LED(18) 
yellow = LED(23)
green = LED(24)

# The next 3 lines turn the GPIO pins off.
# Which means that the three pins are made to provide no power and turn our LED's off.

red.off()
yellow.off()
green.off()
