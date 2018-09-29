def checkMine(curInfo):

    numMines = len(curInfo['mines'])
    if numMines > 0:
        for ii in range(int(numMines)):
            owner = curInfo['mines'][ii][0]

            if owner != 'ElectricBoogalo':
                return int(ii)
            return -2

    return -1
