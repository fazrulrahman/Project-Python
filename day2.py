n = [1,2,3,4,5]

m = []
totalProduct = 1

def divide(num, divider):
	count = 1
	while num > divider:
		num = num - divider
		count = count + 1

	return count

for i in range(0,len(n)):
	totalProduct *= n[i]
print totalProduct

# print (totalProduct/n[x] for x in range(0,len(n)-1)) 

for i in range(0, len(n)):
	m.append(divide(totalProduct,n[i]))

print m