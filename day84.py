# 1 0 0 0 0
# 0 0 1 1 0
# 0 1 1 0 0
# 0 0 0 0 0
# 1 1 0 0 1
# 1 1 0 0 1

n = [[1,0,0,0,0],[0,0,1,1,0],[0,1,1,0,0],[0,0,0,0,0],[1,1,0,0,1],[1,1,0,0,1]]

row = len(n)
col = len(n[0])

# for i in range(0,col):
# 	for j in range(0,row):
# 		if n[i][j] == 1:
# 			if n[i][j+1] == 0:

# 		else:
# 			pass

temp1 = []
temp2 = []
flag = 0

###############  Row List ##############
rowlist = []
for i in range(0,row):
	for j in range(0,col):
		if n[i][j] == 1:
			flag = 1
			temp1.append(j)
			# print(temp)
		if (flag == 1 and n[i][j] == 0) or (flag == 1 and j == col-1) :
			temp2.append(temp1)
			temp1 = []
			# collist.append([temp])
			flag = 0
		# print(temp2)
		if j == col-1:
			rowlist.append(temp2)
			temp2 = []

print(rowlist)
#########################################



################   Column List  #########
collist = []
for i in range(0,col):
	for j in range(0,row):
		if n[j][i] == 1:
			flag = 1
			temp1.append(j)
			# print(temp)
		if (flag == 1 and n[j][i] == 0) or (flag == 1 and j == row-1) :
			temp2.append(temp1)
			temp1 = []
			# collist.append([temp])
			flag = 0
		# print(temp2)
		if j == row-1:
			collist.append(temp2)
			temp2 = []

print(collist)
###########################################

def compare(j):
	for i in rowlist[j[1]]:
		for k in range(1,len(j)):
			for l in k:
				



for i in collist:
	for j in i:
		if len(j) > 1:
			compare(j)


