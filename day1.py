n = [12, 5, 6, 2]
k = 11

n.sort()
start = 0
end = len(n) - 1
flag = 0

while start != end:
	if n[start] + n[end] == k:
		flag = 1
		start = end
	elif n[start] + n[end] < k:
		start = start + 1
	elif n[start] + n[end] > k:
		end = end - 1

if flag == 1:
	print "True"
else:
	print "False"
