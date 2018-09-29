import numpy as np

def checkGotWormholed(xOld,yOld,xNew,yNew):
    if np.sqrt((xNew-xOld)**2 + (yNew-yOld)**2) > 100:
        return 1
    else:
        return 0
