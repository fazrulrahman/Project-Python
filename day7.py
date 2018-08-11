n = []
input = '61261821129'
output = ""
alpha = "abcdefghijklmnopqrstuvwxyz"
possible = ''

for i in range(0,len(input)-1):
	output += (alpha[int(input[i])])
	if int(input[i]) == 1 or (int(input[i]) == 2 and int(input[i+1]) <= 6):
		possible += str(i)

print output
print possible

