# MushroomTrail.py

import mcpi.minecraft as minecraft
from time import sleep

mc = minecraft.Minecraft.create()

mc.postToChat ("Let's build!")
blockType = 40 # Mushroom

while True:
	x, y, z = mc.player.getTilePos() # Get player position
	mc.setBlock(x, y, z, blockType)
	sleep(0.1)
