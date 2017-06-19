# LetItSnow.py

import mcpi.minecraft as minecraft

mc = minecraft.Minecraft.create()

pos = mc.player.getTilePos()
for x in range (pos.x, pos.x+10):
	for z in range (pos.z, pos.z+10):
		y = mc.getHeight(x, z)
		mc.setBlock(x, y, z, 78) # 78 = Snow 
