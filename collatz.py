n = 100
temp = 0
count = 0
solution = 0
solutioncount = 0
for x in xrange(2,n):
	temp = x
	while temp != 1:
		if temp % 2 == 0:
			temp = temp/2
		else:
			temp = (3 * temp) +1
		count = count + 1

	if( count > solutioncount):
		solution = x
		solutioncount = count
	count = 0
	
print solution, solutioncount