import math
import globals

def decideDirection(curInfo, newx, newy):

    x = curInfo['x']
    y = curInfo['y']

    if (math.hypot(x-newx, y-newy)) > (math.hypot(x+(globals.MAPWIDTH-newx), y+(globals.MAPHEIGHT-newy))):
        return -(globals.MAPWIDTH-newx), -(globals.MAPWIDTH-newy)
    else:
        return newx, newy
