import numpy as np
from clientpy3 import run
from parseStatus import parseStatus
from checkMine import checkMine
from traceMap import traceMap
from decideDirection import decideDirection
from bombsAway import bombsAway
import globals
from checkGotWormholed import checkGotWormholed
import time

def moveToPoint(xCur,yCur,xDest,yDest, mineFinding=False,mineTaking=False,foundFromScanning=False):

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
#     check, angleChange = checkWormHoleCollision(xCur,yCur,xDest,yDest)
#     if(check > -1):
#         avoidWormHole(check, angleChange, angle, xDest,yDest)

    #TIME TO ACCELERATE
    Moving = True
    stats = parseStatus()
    oldX = float(stats['x'])
    oldY = float(stats['y'])

    while(Moving):

        stats = parseStatus()
        bombsAway(stats)
        if(checkGotWormholed(oldX,oldY,stats['x'],stats['y']) == 1):
            return -1
        if(mineFinding):
            if len(stats['mines']) > 0:
                chk = checkMine(stats)
                if(chk > -1):
                    print('MINE FOUND')
                    run('ElectricBoogalo','kirtyhurty','BRAKE')
                    time.sleep(5)
                    mineFinding = False
                    xDest = stats['mines'][chk][1]
                    yDest = stats['mines'][chk][2]
                    # while(Moving):
                    #     stats = parseStatus()
                    #     if(float(stats['dx']) < 0.5 and float(stats['dy']) <0.5):
                    #         Moving = False
                    # return 1
        if(mineTaking):
            # run('ElectricBoogalo','kirtyhurty','BRAKE')
            # time.sleep(.0001)
            if(np.sqrt((float(stats['x'])-xDest)**2+(float(stats['y'])-yDest)**2) < float(globals.VISIONRADIUS)):
                chk = checkMine(stats)
                print(chk)
                run('ElectricBoogalo','kirtyhurty','BRAKE')
                time.sleep(.004)
                speed = 0.5
                if(chk == -2):
                    return 3
        xDest,yDest = decideDirection(stats,xDest,yDest)
        angle = np.arctan((yDest-float(stats['y']))/(xDest-float(stats['x'])))
        if(xDest < float(stats['x'])):
            angle += np.pi
        print(angle)
        oldX = stats['x']
        oldY = stats['y']
        #CHECK FOR UNKNOWN WORMHOLES. IF DETECTED, BRAKE IMMEDIATELY.
#         if(len(stats['wormholes']) > 0):
# #             run('ElectricBoogalo','kirtyhurty','ACCELERATE ' + str(angle+np.pi) + ' 1')
# #             time.sleep(2)
# #             run('ElectricBoogalo','kirtyhurty','BRAKE')
#             KNOWN_WORMHOLE_LOC.append(stats['wormholes'][0])
#             print(KNOWN_WORMHOLE_LOC)
#             #We know there's a wormhole in the way, probably, let's just do our best to avoid it
#             check, angleChange = checkWormHoleCollision(float(stats['x']),float(stats['y']),xDest,yDest)
#             avoidWormHole(check, angleChange, angle, xDest,yDest)

        run('ElectricBoogalo','kirtyhurty','ACCELERATE ' + str(angle) + ' ' + str(speed))

        if(not mineTaking):
            if(np.sqrt((float(stats['x'])-xDest)**2 + (float(stats['y'])-yDest)**2) < float(globals.VISIONRADIUS) * 2):
                # run('ElectricBoogalo','kirtyhurty','BRAKE')
                # while(Moving):
                #     stats = parseStatus()
                #     if(float(stats['dx']) < 0.5 and float(stats['dy']) <0.5):
                #         Moving = False
                Moving = False
#         else:
#             if(np.sqrt((float(stats['x'])-xDest)**2 + (float(stats['y'])-yDest)**2) < float(CAPTURERADIUS) * 2)
#                 a = 0

    if(mineFinding):
        2
    else:
        return 1

#Shortest Path Math
def checkWormHoleCollision(xCur,yCur,xDest,yDest):
    print('thats this')
    for i in range(len(globals.KNOWN_WORMHOLE_LOC)-1):
        wormX = float(globals.KNOWN_WORMHOLE_LOC[i][0])
        wormY = float(globals.KNOWN_WORMHOLE_LOC[i][1])
        rad = float(globals.KNOWN_WORMHOLE_LOC[i][2])

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
