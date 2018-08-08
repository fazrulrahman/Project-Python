n = input()

# candles = [3,2,1,3]
candles = []
for i in range(0,n):
	candles.append(input())

count = 0
tallCandle = 0

for i in range(0,n):

	if(candles[i] == tallCandle):
		count = count + 1
	elif(candles[i] > tallCandle):
		tallCandle = candles[i]
		count = 1
print count
