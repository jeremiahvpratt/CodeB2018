# keep track of all mines and wormholes
import globals

def traceMap(mines, wormholes): #input bomb mine and wormhole locations from our scan
    for i in range(len(mines)): #check if already in list with proper name
        if mines[i] in globals.KNOWN_MINE_LOC:
            #the mine is in the global list
            pass
        elif mines[i][1:3] in globals.KNOWN_MINE_LOC_UNLAB:
            print ('in elif')
            #the mine is known but the owner changed
            ind = globals.KNOWN_MINE_LOC_UNLAB.index(mines[i][1:3])
            print (ind)
            #print(ind)
            globals.KNOWN_MINE_LOC[ind] = mines[i]
        else:
            print ('in else')
            #the mine is unknown
            globals.KNOWN_MINE_LOC.append(mines[i])
            globals.KNOWN_MINE_LOC_UNLAB.append(mines[i][1:3])
    for j in range(len(wormholes)):
        if wormholes[j] not in globals.KNOWN_WORMHOLE_LOC:
            #the wormhole is unknown so we add it
            globals.KNOWN_WORMHOLE_LOC.append(wormholes[j])
