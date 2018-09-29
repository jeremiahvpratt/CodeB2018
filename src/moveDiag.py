from clientpy3 import run
from parseStatus import parseStatus
from moveToPoint import moveToPoint
from checkMine import checkMine
from searchAndFind import searchAndFind
import numpy as np
import globals

def moveDiag(curInfo,VISIONRADIUS,MAPWIDTH):

    chk = checkMine(curInfo)
    if chk > -1:
        minex = curInfo['mines'][chk][1]
        miney = curInfo['mines'][chk][2]
        foundMine = True
    else:
        foundMine = False

    x = curInfo['x']
    y = curInfo['y']
    angle = np.random.uniform(0,2*np.pi)
    run('ElectricBoogalo', 'kirtyhurty', 'ACCELERATE ' + str(angle) + ' 1')
    # run('ElectricBoogalo', 'kirtyhurty', 'ACCELERATE ' + str(np.arctan(2*float(VISIONRADIUS)/float(MAPWIDTH))) + ' 1')
    while foundMine == False:
        curInfo = parseStatus()
        search_chk = searchAndFind(curInfo, VISIONRADIUS)
        chk = checkMine(curInfo)
        if chk > -1:
            print ('mine found by vision!')
            run('ElectricBoogalo', 'kirtyhurty', 'BRAKE')
            minex = curInfo['mines'][chk][1]
            miney = curInfo['mines'][chk][2]
            break
        elif search_chk > -1:
            print ('mine found by scanning!')
            minex = globals.KNOWN_MINE_LOC[search_chk][1]
            miney = globals.KNOWN_MINE_LOC[search_chk][2]
            break
        else:
            foundMine = False

    print ('moving to: ' + str(minex) +" "+ str(miney))
    curInfo = parseStatus()
    x = curInfo['x']
    y = curInfo['y']
    moveToPoint(x, y, minex, miney, mineTaking=True)
