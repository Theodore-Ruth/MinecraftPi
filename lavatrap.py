import mcpi.minecraft as minecraft
import mcpi.block as block
from time import sleep

mc = minecraft.Minecraft.create()
mc.postToChat("Welcome to the Lava Trap")

sleep(3)

pos = mc.player.getTilePos()

mc.setBlocks(
    pos.x - 5, pos.y - 2, pos.z - 5,
    pos.x + 5, pos.y - 2, pos.z + 5,
    block.STONE.id)

mc.setBlocks(
    pos.x - 5, pos.y - 1, pos.z - 5,
    pos.x + 5, pos.y - 1, pos.z + 5,
    block.LAVA.id)

mc.setBlocks(
    pos.x - 5, pos.y, pos.z - 5,
    pos.x + 5, pos.y + 5, pos.z + 5,
    block.GLASS.id)

mc.setBlocks(
    pos.x - 4, pos.y, pos.z - 4,
    pos.x + 4, pos.y + 4, pos.z + 4,
    block.AIR.id)


mc.setBlock(pos.x, pos.y -1, pos.z, block.DIAMOND_BLOCK.id)

sleep(1)

mc.postToChat("Get Ready")
mc.postToChat("Blocks under you will keep disappearing")
sleep(2)
mc.postToChat("Go")

gameover = False

curGameLoop = 0
curPoints = 0
while gameover == False:
    p = mc.player.getTilePos()
    mc.setBlock(p.x, p.y - 1, p.z, block.OBSIDIAN.id)
    
    if curGameLoop < 1.7:
        sleep(2 -  curGameLoop)
    else:
        sleep(2 - 1.7)
    
    mc.setBlock(p.x, p.y - 1, p.z, block.AIR.id)
    sleep(0.5)
    curGameLoop += 0.1

    if p.y != pos.y:
        gameover = True
        mc.postToChat("Game over.")
        
    curPoints += 1

mc.postToChat("You got " + str(curPoints) + " points!")
mc.player.setPos(0, 10, 0)
