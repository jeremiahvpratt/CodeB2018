import numpy as np

def checkGotWormholed(xOld,yOld,xNew,yNew):
    # if np.sqrt((xNew-xOld)**2 + (yNew-yOld)**2) > 100:
    if (np.abs(xNew-xOld) > 100) and (np.abs(yNew-yOld) > 100):
        return 1
    else:
        return 0
