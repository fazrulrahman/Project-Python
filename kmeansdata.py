import random
n = 100
num = 1
file = open("train.csv",'w')
file.write("x,y\n")
for i in range (1,51):
	x = 5 + random.randint(1,10)
	y = 15 + random.randint(1,5)

	file.write(str(x)+","+str(y)+'\n')

for j in xrange(1,41):
	x = 20 + random.randint(1,5)
	y = 5 + random.randint(1,10)

	file.write(str(x)+","+str(y)+'\n')


file.close()

file = open("test.csv",'w')
file.write("x,y\n")
for i in range (1,11):
	x = 5 + random.randint(1,10)
	y = 15 + random.randint(1,5)

	file.write(str(x)+","+str(y)+'\n')

for j in xrange(1,10):
	x = 20 + random.randint(1,5)
	y = 5 + random.randint(1,10)

	file.write(str(x)+","+str(y)+'\n')
file.close()