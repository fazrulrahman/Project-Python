inputdata = [10, 5, 2, 7, 8, 7]

window = []
output = []
window.append(inputdata[0])
window.append(inputdata[1])
window.append(inputdata[2])
for i in range(2,len(inputdata)):
	window[i%3] = inputdata[i]
	output.append(max(window))
print output
