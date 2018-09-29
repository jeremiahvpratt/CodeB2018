# retrieve config GLOBALS
from moveDiag import moveDiag
from moveToPoint import moveToPoint
from parseStatus import runRet, parseStatus
from findCircles import findCircles
from bestPathAlg import bestPathAlg
from scanAhead import scanAhead
from clientpy3 import run
import numpy as np
import globals
import time

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
print(circles.T)
curInfo = parseStatus()
path = bestPathAlg(circles.T,[curInfo['x'],curInfo['y']])
print(path)
while(True):
    for i in range(np.shape(path)[0]):
        print(path[i][0])
        print(path[i][1])
        curInfo = parseStatus()
        xTrue, yTrue = scanAhead(path[i][0],path[i][1])
        if (xTrue == -1 and yTrue == -1):
            continue
        moveToPoint(curInfo['x'],curInfo['y'],xTrue,yTrue,mineFinding=False,mineTaking=True)
        run('ElectricBoogalo','kirtyhurty','BRAKE')
        time.sleep(6)

# print(circles)
# while(True):
#     curInfo = parseStatus()
#     moveDiag(curInfo,globals.VISIONRADIUS,globals.MAPWIDTH)
#     print (globals.KNOWN_MINE_LOC)
#     print (globals.KNOWN_MINE_LOC_UNLAB)
