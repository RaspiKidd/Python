# BlockFighter.py

import mcpi.minecraft as minecraft
from time import sleep

mc = minecraft.Minecraft.create()

mc.postToChat("Use the right button to hit blocks and score")
score = 0
sleep (60)

hits = mc.events.pollBlockHits()

for hit in hits:
	# score +=1 and 1 point per hit
	x = hit.pos.x
	y = hit.pos.y
	z = hit.pos.z
	score = score + mc.getBlock(x, y, z)
	print (mc.getBlock(x, y, z))
mc.postToChat("You got " + str(score) + " points!")
