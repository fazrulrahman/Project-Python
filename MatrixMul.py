n = [[1,2,3],[1,2,3],[1,2,3]]
m = [[1,0,0],[0,1,0],[0,0,1]]
o = (2,3,4)
sol = [[0,0,0],[0,0,0],[0,0,0]]
print m[2][2]
for i in xrange(0,2):
	for j in xrange(0,2):
		for k in xrange(0,2):
			sol[i][j] += (n[i][k] * m[k][j] )


print sol

# import numpy as np

# x = np.array([[2,3,4],[3,4,5],[4,5,6]])
# y = np.array([[1,0,0],[0,1,0],[0,0,1]])
# print np.matmul(x,y)