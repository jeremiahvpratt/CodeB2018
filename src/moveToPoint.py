import numpy as np
from main import run

def moveToPoint(xCur,yCur,xDest,yDest,mineFinding=False):

    speed = 1
    #STOP SHIP FIRST
    Moving = True
    run('ElectricBoogalo','kirtyhurty','BRAKE')
    while(Moving):
        stats = parseStatus()
        if(float(stats['dx']) < 2 and float(stats['dy']) <2):
            Moving = False

    #SET FIRST MOVE ANGLE
    angle = np.arctan((yDest-float(stats['y']))/(xDest-float(stats['x'])))
    if(xDest < float(stats['x'])):
        angle += np.pi
    print(angle)
    #CHECK FOR POSSIBLE WORMHOLES IN PATH
    check, angleChange = checkWormHoleCollision(xCur,yCur,xDest,yDest)
    if(check > -1):
        avoidWormHole(check, angleChange, angle, xDest,yDest)

    #TIME TO ACCELERATE
    Moving = True
    while(Moving):
        stats = parseStatus()
        if(mineFinding):
            if len(stats['mines']) > 0:
            chk = checkMine(stats)
            if(chk > -1):
                print('MINE FOUND')
                run('ElectricBoogalo','kirtyhurty','BRAKE')
                while(Moving):
                    stats = parseStatus()
                    if(float(stats['dx']) < 0.5 and float(stats['dy']) <0.5):
                        Moving = False
                return 1
        angle = np.arctan((yDest-float(stats['y']))/(xDest-float(stats['x'])))
        if(xDest < float(stats['x'])):
            angle += np.pi
        print(angle)
        #CHECK FOR UNKNOWN WORMHOLES. IF DETECTED, BRAKE IMMEDIATELY.
        if(len(stats['wormholes']) > 0):
#             run('ElectricBoogalo','kirtyhurty','ACCELERATE ' + str(angle+np.pi) + ' 1')
#             time.sleep(2)
#             run('ElectricBoogalo','kirtyhurty','BRAKE')
            KNOWN_WORMHOLE_LOC.append(stats['wormholes'][0])
            print(KNOWN_WORMHOLE_LOC)
            #We know there's a wormhole in the way, probably, let's just do our best to avoid it
            check, angleChange = checkWormHoleCollision(float(stats['x']),float(stats['y']),xDest,yDest)
            avoidWormHole(check, angleChange, angle, xDest,yDest)

        run('ElectricBoogalo','kirtyhurty','ACCELERATE ' + str(angle) + ' ' + str(speed))

        if(np.sqrt((float(stats['x'])-xDest)**2 + (float(stats['y'])-yDest)**2) < float(VISIONRADIUS) * 2):
            # run('ElectricBoogalo','kirtyhurty','BRAKE')
            # while(Moving):
            #     stats = parseStatus()
            #     if(float(stats['dx']) < 0.5 and float(stats['dy']) <0.5):
            #         Moving = False
            Moving = False

    if(mineFinding):
        2
    else:
        return 1

#Shortest Path Math
def checkWormHoleCollision(xCur,yCur,xDest,yDest):
    print('thats this')
    for i in range(len(KNOWN_WORMHOLE_LOC)-1):
        wormX = float(KNOWN_WORMHOLE_LOC[i][0])
        wormY = float(KNOWN_WORMHOLE_LOC[i][1])
        rad = float(KNOWN_WORMHOLE_LOC[i][2])

        #shortest distance to line calculation
        distToLine = (np.abs((xDest-xCur)*wormX + (yCur-yDest)*wormY +
                            (xCur - xDest)*yCur + (yDest-yCur)*xCur)/
                      np.sqrt((xDest-xCur)**2 + (yCur-yDest)**2))

        #check if inside circle
        if(distToLine < rad):
            angleChange = np.arcsin((2*rad)/np.sqrt((wormX-xCur)**2+(wormY-yCur)**2))
            return i, angleChange

    return -1, 0

#Moving Around Wormhole
def avoidWormHole(check, angleChange, angle, xDest,yDest):
    run('ElectricBoogalo','kirtyhurty','BRAKE')
    time.sleep(1)
    while(check > -1):
        run('ElectricBoogalo','kirtyhurty','ACCELERATE ' + str(angle+angleChange) + ' 1')
        stats = parseStatus()
        check, differentAngle = checkWormHoleCollision(float(stats['x']),float(stats['y']),xDest,yDest)

    run('ElectricBoogalo','kirtyhurty','BRAKE')
    time.sleep(.2)

    return 0

def checkMine(curInfo):

    numMines = len(curInfo['mines'])
    # flatMines = [x for sub in KNOWN_MINE_LOC for x in sub]
    for ii in range(int(numMines)):
        # minex = curInfo['mines'][ii][1]
        # miney = curInfo['mines'][ii][2]
        owner = curInfo['mines'][ii][0]
        print (owner)
        if owner != 'ElectricBoogalo':
            return int(ii)

    return -1
