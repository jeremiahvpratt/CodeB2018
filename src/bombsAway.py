from clientpy3 import run 

def bombsAway(curInfo):

    x = curInfo['x']
    y = curInfo['y']
    run('ElectricBoogalo', 'kirtyhurty', 'BOMB ' + str(x) + ' ' + str(y))
