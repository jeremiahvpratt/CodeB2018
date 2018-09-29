from clientpy3 import run
from parseStatus import parseStatus
from moveToPoint import moveToPoint
from checkMine import checkMine
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
        chk = checkMine(curInfo)
        if chk > -1:
            run('ElectricBoogalo', 'kirtyhurty', 'BRAKE')
            minex = curInfo['mines'][chk][1]
            miney = curInfo['mines'][chk][2]
            break
        else:
            foundMine = False

    print ('mine found!')
    print ('moving to: ' + str(minex) +" "+ str(miney))
    curInfo = parseStatus()
    x = curInfo['x']
    y = curInfo['y']
    moveToPoint(x, y, minex, miney, mineTaking=True)
