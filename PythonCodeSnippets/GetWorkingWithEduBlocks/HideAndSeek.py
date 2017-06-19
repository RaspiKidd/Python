# HideAndSeek.py

import mcpi.minecraft as minecraft
from time import sleep
import math
import random

mc = minecraft.Minecraft.create()

targetBlock = 41 # gold
destX = random.randint(-127, 127)
destZ = random.randint(-127, 127)
destY = mc.getHeight(destX, destZ) # ground level
print (destZ)
mc.setBlock(destX, destY, destZ, targetBlock)

mc.postToChat("Block hidden - go find it!")
print ("x: " + str(destX) + " y: " + str(destY) + " z:" + str(destZ))

while True:
	pos = mc.player.getPos()
	distance = math.sqrt((pos.x-destX)**2 + (pos.z-destZ)**2)
	if distance > 100:
		mc.postToChat("Freezing!")
	elif distance > 50:
		mc.postToChat("Cold!")
	elif distance > 25:
		mc.postToChat("Warm!")
	elif distance > 15:
		mc.postToChat("Hot!")
	elif distance < 2:
		mc.postToChat("Found it!")
	sleep(0.2)
