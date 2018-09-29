# retrieve config GLOBALS
from moveDiag import moveDiag
from moveToPoint import moveToPoint
from parseStatus import runRet, parseStatus
from findCircles import findCircles
import globals

globals.init()

config = runRet('ElectricBoogalo', 'kirtyhurty', 'CONFIGURATIONS')
config_rets = config.split(" ")

globals.MAPWIDTH = config_rets[config_rets.index('MAPWIDTH') + 1]
globals.MAPHEIGHT = config_rets[config_rets.index('MAPHEIGHT') + 1]
globals.CAPTURERADIUS = config_rets[config_rets.index('CAPTURERADIUS') + 1]
globals.VISIONRADIUS = config_rets[config_rets.index('VISIONRADIUS') + 1]
globals.FRICTION = config_rets[config_rets.index('FRICTION') + 1]
globals.BRAKEFRICTION = config_rets[config_rets.index('BRAKEFRICTION') + 1]
globals.BOMBPLACERADIUS = config_rets[config_rets.index('BOMBPLACERADIUS') + 1]
globals.BOMBEFFECTRADIUS = config_rets[config_rets.index('BOMBEFFECTRADIUS') + 1]
globals.BOMBDELAY = config_rets[config_rets.index('BOMBDELAY') + 1]
globals.BOMBPOWER = config_rets[config_rets.index('BOMBPOWER') + 1]
globals.SCANRADIUS = config_rets[config_rets.index('SCANRADIUS') + 1]
globals.SCANDELAY = config_rets[config_rets.index('SCANDELAY') + 1]

circles = findCircles('canvas.png')
path = bestPathAlg(circles.T)
for point in path:
    curInfo = parseStatus()
    
    moveToPoint(curInfo['x'],curInfo['y'],point[0],point[1])
# print(circles)
# while(True):
#     curInfo = parseStatus()
#     moveDiag(curInfo,globals.VISIONRADIUS,globals.MAPWIDTH)
#     print (globals.KNOWN_MINE_LOC)
#     print (globals.KNOWN_MINE_LOC_UNLAB)
