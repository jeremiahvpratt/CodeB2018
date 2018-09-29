from parseStatus import runRet, parseStatus
from clientpy3 import run
from traceMap import traceMap
import time
import math
import globals

def scanAhead(x, y):
    print('proof dude')
    status = runRet('ElectricBoogalo', 'kirtyhurty', 'SCAN '+ str(x) + ' ' + str(y))
    status_rets = status.split(" ")
    status_rets = list(filter(None, status_rets))

    while (status_rets[0] == 'ERROR'):
        status = runRet('ElectricBoogalo', 'kirtyhurty', 'SCAN '+ str(x) + ' ' + str(y))
        status_rets = status.split(" ")
        status_rets = list(filter(None, status_rets))
        time.sleep(0.1)
        
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
    # mineList()
    # print(distList)
    # correct = mineList.index(min(distList))
    if(len(distList) > 0):
        correct = mineList[distList.index(min(distList))]
    else:
        correct = [0,x,y]
    print(correct)
    return correct[1], correct[2]
