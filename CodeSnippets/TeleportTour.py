# TeleportTour.py

import mcpi.minecraft as minecraft
import time

mc = minecraft.Minecraft.create()

mc.postToChat("Boing")
x, y, z = mc.player.getPos() # Get the players position
mc.player.setPos(x, y+10, z+10)
time.sleep (1)

mc.postToChat("Boing")
x, y, z = mc.player.getPos() # Get the players position
mc.player.setPos(x, y+10, z+10)
time.sleep (1)

mc.postToChat("Boing")
x, y, z = mc.player.getPos() # Get the players position
mc.player.setPos(x, y+10, z+10)
time.sleep (1)
