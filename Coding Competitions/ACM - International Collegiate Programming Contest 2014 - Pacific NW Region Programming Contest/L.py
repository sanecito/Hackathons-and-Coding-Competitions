#team203
import math
def distance(star1,star2):
	result = math.sqrt( (star1[0] - star2[0])**2 +  
			(star1[1] - star2[1])**2 +
			(star1[2] - star2[2])**2 )
	if result - int(result) > 0.5:
		result = int(result) + 1
	else:
		result = int(result)
	return result


T = input()
kase = 1
while T:
	T -= 1
	NAME = {}
	POS = []
	star = input()
	for i in range(0,star):
		Line = raw_input().split()
		pos = map(int,Line[1:])
		NAME[Line[0]] = i
		POS.append(pos)
	dis = []
	for i in range(0,star):
		row = []
		for j in range(0,star):
			row.append(0.0)
		dis.append(row)

	for i in range(0,star):
		for j in range(0,star):	
			if i == j:
				dis[i][j] = 0.0
			else:
				dis[i][j] = dis[j][i] = distance(POS[i],POS[j])
	#	
	#for i in range(0,star):
	#	for j in range(0,star):	
	#		print dis[i][j],
	#	print ""
	#
	#

	worm = input()
	for i in range(0,worm):
		F,S = raw_input().split()
		dis[NAME[F]][NAME[S]] = 0.0
	for i in range(0,star):
		for j in range(0,star):
			for k in range(0,star):
				dis[i][j] = min(dis[i][j],(dis[i][k] + dis[k][j]))
	
	print "Case %d:" % kase
	kase += 1
	query = input()
	for i in range(0,query):
		F,S = raw_input().split()
		result = dis[NAME[F]][NAME[S]]
		
		print "The distance from "+ F + " to " + S + " is",
		print int(result),
		print "parsecs."






