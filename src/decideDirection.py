import math
import globals

def decideDirection(curInfo, newx, newy):

    x = float(curInfo['x'])
    y = float(curInfo['y'])

    if x >= 5000 and y >= 5000:
        if (math.hypot(x-newx, y-newy)) > (math.hypot(x-(newx+float(globals.MAPWIDTH)), y-(newy+float(globals.MAPHEIGHT)))):
            return (newx+float(globals.MAPWIDTH)), (newy+float(globals.MAPHEIGHT))
        else:
            return newx, newy

    if x >= 5000 and y <= 5000:
        if (math.hypot(x-newx, y-newy)) > (math.hypot(x-(newx+float(globals.MAPWIDTH)), y-(newy-float(globals.MAPHEIGHT)))):
            return (newx+float(globals.MAPWIDTH)), (newy-float(globals.MAPHEIGHT))
        else:
            return newx, newy

    if x <= 5000 and y >= 5000:
        if (math.hypot(x-newx, y-newy)) > (math.hypot(x-(newx-float(globals.MAPWIDTH)), y-(newy+float(globals.MAPHEIGHT)))):
            return (newx+float(globals.MAPWIDTH)), (newy+float(globals.MAPHEIGHT))
        else:
            return newx, newy

    if x <= 5000 and y<= 5000:
        if (math.hypot(x-newx, y-newy)) > (math.hypot(x-(newx-float(globals.MAPWIDTH)), y-(newy-float(globals.MAPHEIGHT)))):
            return (newx-float(globals.MAPWIDTH)), (newy-float(globals.MAPHEIGHT))
        else:
            return newx, newy
