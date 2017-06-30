# FlatLand.py

import mcpi.minecraft as minecraft
import mcpi.block as block
from time import sleep

mc = minecraft.Minecraft.create()

mc.postToChat("Flattening land")
mc.setBlocks(-128, 0, -128, 128, 64, 128, 0)
mc.setBlocks(-128, 0, -128, 128, 64, 128, 24)
