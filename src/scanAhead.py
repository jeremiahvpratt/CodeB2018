from parseStatus import runRet, parseStatus
from clientpy3 import run
from traceMap import traceMap
import math
import globals

def searchAhead(x, y):

    status = runRet('ElectricBoogalo', 'kirtyhurty', 'SCAN '+ str(x) + ' ' + str(y))
    status_rets = status.split(" ")
    status_rets = list(filter(None, status_rets))

    if (status_rets[0] == 'ERROR'):
        return -1

    numMines = status_rets[status_rets.index('MINES') + 1]
    mineList= []
    if numMines != 0:
        for ii in range(int(numMines)):
            mine = [status_rets[status_rets.index('MINES') + ((ii*3)+2)], float(status_rets[status_rets.index('MINES') + ((ii*3)+3)]), float(status_rets[status_rets.index('MINES') + ((ii*3)+4)])]
            mineList.append(mine)

    distList = []
    for ii in range(len(mineList)):
        dist = math.hypot(x - mineList[ii][1], y - mineList[ii][2])
        distList.append(dist)

    correct = mineList.index(min(distList))

    return correct[1], correct[2]
