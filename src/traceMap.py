import random


#keep track of all mines and wormholes
def traceMap(mines, wormholes): #input bomb mine and wormhole locations from our scan
    i=0
    j=0
    for i in range(len(mines)): #check if already in list with proper name 
        if mines[i] in KNOWN_MINE_LOC:
            #the mine is in the global list
            pass
        elif mines[i][1:3] in KNOWN_MINE_LOC_UNLAB:
        	#the mine is known but the owner changed
            ind = KNOWN_MINE_LOC_UNLAB.index(mines[i][1:3])
            #print(ind)
            KNOWN_MINE_LOC[ind] = mines[i]
        else:
        	#the mine is unknown
            KNOWN_MINE_LOC.append(mines[i])
            KNOWN_MINE_LOC_UNLAB.append(mines[i][1:3])
    for j in range(len(wormholes)):
        if wormholes[j] not in KNOWN_WORMHOLE_LOC:
        	#the wormhole is unknown so we add it
            KNOWN_WORMHOLE_LOC.append(wormholes[j])  
    return


