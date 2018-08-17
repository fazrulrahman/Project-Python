n = 1000000
cache = [-1 for i in range(1,n)]
cache[1] = 1
cache[2] = 2
count = 0



def collatz(num):
	global cache
	if cache[num] != -1:
		return cache[num]
	elif num % 2 == 0:
		cache[num] = (1 + collatz(num/2))
		return cache[num] 
	else:
		cache[num] = (1 + collatz((3*num)+1))
		return cache[num]

for i in range(3,n+1):
	num = collatz(i)
	print i,num
	pass
# for j in range (2,n):
# 	i = j
# 	while i != 1:
# 		if i%2 == 0:
# 			i = i/2
# 		elif:
# 			i = 3*i + 1
# 		count = count + 1
# 	if i==1:
# 		cache[j] = count
# 	count = 0