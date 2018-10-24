n = [10, 5 ,7]
n = [10,5,1]
n = [ 1 , 4 , 4 ,23 ,45, 1, 50]
count = 0
for i in range(1,len(n)):
	if n[i] >= n[i-1]:
		count += 1

if count == len(n) - 2:
	print("yes")

print(count)