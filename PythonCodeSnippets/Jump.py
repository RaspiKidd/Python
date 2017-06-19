# Jump.py

import mcpi.minecraft as minecraft

mc = minecraft.Minecraft.create()

mc.postToChat("Jump")
x, y, z = mc.player.getPos() # Get players position
mc.player.setPos(x, y+50, z)

