import socket
import sys

def runRet(user, password, * commands):
    HOST, PORT = "codebb.cloudapp.net", 17429
    data = user + " " + password + "\n" + "\n".join(commands) + "\nCLOSE_CONNECTION\n"
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:

        sock.connect((HOST, PORT))
        sock.sendall(bytes(data, "utf-8"))
        sfile = sock.makefile()
        rline = sfile.readline()
        rets = ""
        while rline:
            rets = rets + rline.strip()
            rline = sfile.readline()

    return rets

def parseStatus():

    status = runRet('ElectricBoogalo', 'kirtyhurty', 'STATUS')
    status_rets = status.split(" ")
    status_rets = list(filter(None, status_rets))

    # mines
    numMines = status_rets[status_rets.index('MINES') + 1]
    mineList= []
    if numMines != 0:
        for ii in range(int(numMines)):
            mine = [status_rets[status_rets.index('MINES') + ((ii*3)+2)], float(status_rets[status_rets.index('MINES') + ((ii*3)+3)]), float(status_rets[status_rets.index('MINES') + ((ii*3)+4)])]
            mineList.append(mine)
    # players
    numPlayers = status_rets[status_rets.index('PLAYERS') + 1]
    playerList= []
    if numPlayers != 0:
        for ii in range(int(numPlayers)):
            player = [float(status_rets[status_rets.index('PLAYERS') + ((ii*4)+2)]), float(status_rets[status_rets.index('PLAYERS') + ((ii*4)+3)]), float(status_rets[status_rets.index('PLAYERS') + ((ii*4)+4)]), float(status_rets[status_rets.index('PLAYERS') + ((ii*3)+5)])]
            playerList.append(player)

    # bombs
    numBombs = status_rets[status_rets.index('BOMBS') + 1]
    bombList= []
    if numBombs != 0:
        for ii in range(int(numBombs)):
            bomb = [float(status_rets[status_rets.index('BOMBS') + ((ii*2)+2)]), float(status_rets[status_rets.index('BOMBS') + ((ii*2)+3)])]
            bombList.append(bomb)

    # wormholes
    numWormholes = status_rets[status_rets.index('WORMHOLES') + 1]
    wormholeList= []
    if numWormholes != 0:
        for ii in range(int(numWormholes)):
            wormhole = [float(status_rets[status_rets.index('WORMHOLES') + ((ii*5)+2)]), float(status_rets[status_rets.index('WORMHOLES') + ((ii*5)+3)]), float(status_rets[status_rets.index('WORMHOLES') + ((ii*5)+4)]), float(status_rets[status_rets.index('WORMHOLES') + ((ii*5)+5)]), float(status_rets[status_rets.index('WORMHOLES') + ((ii*5)+6)])]
            wormholeList.append(wormhole)

    out = {
        'x': float(status_rets[1]),
        'y': float(status_rets[2]),
        'dx': float(status_rets[3]),
        'dy': float(status_rets[4]),
        'mines': mineList,
        'players': playerList,
        'bombs': bombList,
        'wormholes': wormholeList
    }

    return out
