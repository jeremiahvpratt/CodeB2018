import math
import globals

def decideDirection(curInfo, newx, newy):

    x = float(curInfo['x'])
    y = float(curInfo['y'])

    if (math.hypot(x-newx, y-newy)) > (math.hypot(x+(float(globals.MAPWIDTH)-newx), y+(float(globals.MAPHEIGHT)-newy))):
        return -(float(globals.MAPWIDTH)-newx), -(float(globals.MAPWIDTH)-newy)
    else:
        return newx, newy
