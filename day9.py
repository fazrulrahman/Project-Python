n =[5,3,8,9,16,14,12,6]
# n = [2,4,6,2,5]
# n = [5,1,1,5]
exc = 0
inc = n[0]
newEx = 0
for i in range(2,len(n)+1):
	newEx = max(exc,inc)
	inc = n[i-1] + exc
	exc = newEx

print max(exc,inc)