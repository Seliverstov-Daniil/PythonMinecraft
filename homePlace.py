#2.3 Место жительства
import  mcpi.minecraft as minecraft
import time
craft = minecraft.Minecraft.create()
home = craft.player.getTilePos()

while True:
    cor = craft.player.getTilePos()
    if cor == home:
        print("walcome")
    else:
        print("GO HOME!!!")
    time.sleep(2)    
 
