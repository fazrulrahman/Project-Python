n = 100
flag = -1
num = 3
count =0

while count < n:
	# print "5"
	for i in xrange(2,num-1):
		if( num % (i/2)+1 == 0 ):
			flag = 1
	if ( flag == -1):
		print num
		count += 1
	num += 1
	flag = -1