import mcpi.minecraft as minecraft
craft = minecraft.Minecraft.create()
cor = craft.player.getTilePos()
print(cor.x, cor.y, cor.z)
craft.postToChat("PlayerPos="+str(cor.x)+","+str( cor.y)+","+str( cor.z))
