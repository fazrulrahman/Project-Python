n = 15

dash = (n * 2) - 2
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
i = 1
for x in range(dash,-2,-2):
	# print (("-"*x) + alphabet[n-1] )
	str1 = ("-")*x
	str2 = ''
	str3 = ''
	for j in xrange(0,i):
		str2 = str2 + alphabet[n-j-1] + '-' 
	if i != 1:
		for k in xrange(1,i):
			str3 = str3 + alphabet[n-k-1] 
			if k != i-1:
				str3 = str3+'-'
	print str1+str2+str3+str1
	i = i+1

dash = 2
for x in range(dash,(n * 2) ,2):

	str1 = ("-")*x
	str2 = ''
	str3 = ''
	for j in xrange(1,i-1):
		str2 = str2 + alphabet[n-j] + '-' 
	if i != 1:
		for k in xrange(1,i-2):
			str3 = str3 + alphabet[n-k-1] 
			if k != i-1:
				str3 = str3+'-'
	print str1+str2+str3+str1
	i = i - 1