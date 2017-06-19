# BuriedTreasure.py

import mcpi.minecraft as minecraft
from time import sleep

mc = minecraft.Minecraft.create()

treasure = 16 # coal
#treasure = int(input("What treasure do ye seek matey:"))

while True:
	x, y, z = mc.player.getPos()
	z -=1
	for i in range (1,60): # look 50 blocks down
		if mc.getBlock(x, y, z) == treasure:
			mc.postToChat("There be treasure " + str(i) + "space below you!")
			break
		else:
			y -=1
			mc.postToChat("Sorry matey, nothing here!")
	sleep (0.2)
