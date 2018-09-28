m = 20
n = 4

sol = 0

for x in range(1,max(m,n)):
	if m % x == 0 and n % x == 0:
		sol = x

print sol

def gcd(a,b):
	if b == 0:
		return a
	else:
		return gcd(b, a % b)
print gcd(5,6)
pass