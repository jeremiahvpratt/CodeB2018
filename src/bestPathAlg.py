import random, numpy, math, copy #, matplotlib.pyplot as plt

def bestPathAlg(KNOWN_MINE_LOC, KNOWN_MINE_LOC_UNLAB):
	l=[]	#dont go to places we own
	for n in range(len(KNOWN_MINE_LOC)):
		if KNOWN_MINE_LOC[n][0] != 'ElectricBoogalo':
			l.append(KNOWN_MINE_LOC_UNLAB[n])

	nMines=len(l)
	cities = l
	path = random.sample(range(nMines),nMines);#generate random path of indecies [7,1,4,3,5,2,8,6]

	for temp in numpy.logspace(0,5.5,num=100000)[::-1]: # generates a logarithmic spacing of 0->10^5 with 100k points 
		[i,j] = sorted(random.sample(range(nMines),2));
		newpath =  path[:i] + path[j:j+1] +  path[i+1:j] + path[i:i+1] + path[j+1:];
		c=[] #temp array
		for k in [j,j-1,i,i-1]: #only compute the ith and jth dist cuz rest will cancel
			ab=[]
			for d in [0,1]:
				ab.append((cities[path[(k+1)%nMines]][d] - cities[path[k%nMines]][d])**2  )
			c.append( math.sqrt(sum( ab )))
		oldDist =  sum(c)

		c=[] #temp array for all hypotenuse  
		for k in [j,j-1,i,i-1]:
			ab=[] #temp array to store the a^2 and b^2
			for d in [0,1]: #do x and y coor 
				ab.append((cities[newpath[(k+1)%nMines]][d] - cities[newpath[k%nMines]][d])**2  ) #find the next point and subtract dist in x, then y and square it for mr pythagorous
			c.append( math.sqrt(sum(ab)))#append to hypotenuse list
		newDist =  sum(c)

		if math.exp(( oldDist - newDist) / temp) > random.random(): #something to do with gibbs free energy. 
			path = copy.copy(newpath);

	pth = list(zip([cities[path[i % nMines]][0] for i in range(nMines+1)], [cities[path[i % nMines]][1] for i in range(nMines+1)]))
	#print(pth,temp)
	#plt.plot([cities[path[i % nMines]][0] for i in range(nMines+1)], [cities[path[i % nMines]][1] for i in range(nMines+1)], 'xb-');
	#plt.show()

	return(pth)
	
'''
nM = 35
cities = [random.sample(list(numpy.linspace(0,1023,2000)), 2) for x in range(nM)];

e = 1

BestPathAlg(e,cities)

'''