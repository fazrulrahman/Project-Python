LookAndSayList = ['1','11']
nextnum = ''
count = 1
NthTerm = int(input())
for j in range(1,NthTerm-1):
	for i in range(1,len(LookAndSayList[j])):
		if(LookAndSayList[j][i] == LookAndSayList[j][i-1]):
			count += 1
		else:
			nextnum += (str(count)+LookAndSayList[j][i-1])
			count = 1
	nextnum += (str(count)+LookAndSayList[j][i])
	LookAndSayList.append(nextnum)
	nextnum = ''
	count = 1
print(LookAndSayList[NthTerm-1])

#312211