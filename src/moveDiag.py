def moveDiag(curInfo):

    chk = checkMine(curInfo)
    if chk > -1:
        minex = curInfo['mines'][chk][1]
        miney = curInfo['mines'][chk][2]
        foundMine = True
    else:
        foundMine = False

    x = curInfo['x']
    y = curInfo['y']

    run('ElectricBoogalo', 'kirtyhurty', 'ACCELERATE ' + str(np.arctan(2*float(VISIONRADIUS)/float(MAPWIDTH))) + ' 1')
    while foundMine == False:
        curInfo = parseStatus()
        if len(curInfo['mines']) > 0 or len(curInfo['wormholes']) > 0:
            traceMap(curInfo['mines'], curInfo['wormholes'])
        chk = checkMine(curInfo)
        if chk > -1:
            runRet('ElectricBoogalo', 'kirtyhurty', 'BRAKE')
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
    moveToPoint(x, y, minex, miney,mineTaking=True)
#     run('ElectricBoogalo', 'kirtyhurty', 'BRAKE')
    
