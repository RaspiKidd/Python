# BuildHouse.py

import mcpi.minecraft as minecraft
from time import sleep

mc = minecraft.Minecraft.create()

length = 6
width = 6
height = 6
blockType = 4
air = 0

mc.postToChat("Build a house")

x, y, z = mc.player.getPos()
mc.setBlocks(x+1, y, z, x+width+1, y+height, z+length, blockType)

# Hollow out the inside
mc.setBlocks(x+2, y, z+1, x+width-1, y+height-1, z+length-1, air)

# Make a door
mc.setBlocks(x+1, y, z+3, x+1, y+2, z+4, air)
