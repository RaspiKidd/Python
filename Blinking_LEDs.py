from gpiozero import LED
from time import sleep

# Configuring LEDs to pin numbers
red = LED(18)
yellow = LED(23)
green = LED(24)

# LEDs on
red.on()
yellow.on()
green.on()

sleep(1)

# LEDs off
red.off()
yellow.off()
green.off()

sleep(1)

# LEDs on
red.on()
yellow.on()
green.on()

sleep(1)

# LEDs off
red.off()
yellow.off()
green.off()
