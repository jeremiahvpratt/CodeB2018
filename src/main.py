# retrieve config GLOBALS
from moveDiag import moveDiag
from moveToPoint import moveToPoint
from parseStatus import runRet, parseStatus

config = runRet('ElectricBoogalo', 'kirtyhurty', 'CONFIGURATIONS')
config_rets = config.split(" ")
MAPWIDTH = config_rets[config_rets.index('MAPWIDTH') + 1]
MAPHEIGHT = config_rets[config_rets.index('MAPHEIGHT') + 1]
CAPTURERADIUS = config_rets[config_rets.index('CAPTURERADIUS') + 1]
VISIONRADIUS = config_rets[config_rets.index('VISIONRADIUS') + 1]
FRICTION = config_rets[config_rets.index('FRICTION') + 1]
BRAKEFRICTION = config_rets[config_rets.index('BRAKEFRICTION') + 1]
BOMBPLACERADIUS = config_rets[config_rets.index('BOMBPLACERADIUS') + 1]
BOMBEFFECTRADIUS = config_rets[config_rets.index('BOMBEFFECTRADIUS') + 1]
BOMBDELAY = config_rets[config_rets.index('BOMBDELAY') + 1]
BOMBPOWER = config_rets[config_rets.index('BOMBPOWER') + 1]
SCANRADIUS = config_rets[config_rets.index('SCANRADIUS') + 1]
SCANDELAY = config_rets[config_rets.index('SCANDELAY') + 1]

KNOWN_MINE_LOC = []
KNOWN_WORMHOLE_LOC = []
KNOWN_MINE_LOC_UNLAB = []
curInfo=parseStatus()
# moveToPoint(curInfo['x'],curInfo['y'],5000,5000,VISIONRADIUS)
while(True):
    curInfo = parseStatus()
    moveDiag(curInfo,VISIONRADIUS,MAPWIDTH,KNOWN_WORMHOLE_LOC,KNOWN_MINE_LOC,KNOWN_MINE_LOC)
