from parseStatus import runRet, parseStatus
from clientpy3 import run
from traceMap import traceMap
import globals

def searchAndFind(curInfo, VISIONRADIUS):

    x = curInfo['x']
    y = curInfo['y']
    status = runRet('ElectricBoogalo', 'kirtyhurty', 'SCAN '+ str(x+(float(VISIONRADIUS)*2)) + ' ' + str(y+(float(VISIONRADIUS)*2)))
    status_rets = status.split(" ")
    status_rets = list(filter(None, status_rets))

    if (status_rets[0] == 'ERROR'):
        return -1
    # mines
    numMines = status_rets[status_rets.index('MINES') + 1]
    mineList= []
    if numMines != 0:
        for ii in range(int(numMines)):
            mine = [status_rets[status_rets.index('MINES') + ((ii*3)+2)], float(status_rets[status_rets.index('MINES') + ((ii*3)+3)]), float(status_rets[status_rets.index('MINES') + ((ii*3)+4)])]
            mineList.append(mine)

    # wormholes
    numWormholes = status_rets[status_rets.index('WORMHOLES') + 1]
    wormholeList= []
    if numWormholes != 0:
        for ii in range(int(numWormholes)):
            wormhole = [float(status_rets[status_rets.index('WORMHOLES') + ((ii*5)+2)]), float(status_rets[status_rets.index('WORMHOLES') + ((ii*5)+3)]), float(status_rets[status_rets.index('WORMHOLES') + ((ii*5)+4)]), float(status_rets[status_rets.index('WORMHOLES') + ((ii*5)+5)]), float(status_rets[status_rets.index('WORMHOLES') + ((ii*5)+6)])]
            wormholeList.append(wormhole)

    if int(numMines) > 0 or int(numWormholes) > 0:
        traceMap(mineList, wormholeList)
        if int(numMines) > 0:
            if mineList[-1][0] != 'ElectricBoogalo':
                return 1
    return -1
