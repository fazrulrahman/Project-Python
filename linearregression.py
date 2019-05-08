import sklearn.linear_model as lm
import csv

inputX = []
outputY = []
textInput = []

with open("train.csv",'rb') as csvtrain:
	reader = csv.reader(csvtrain)
	reader.next()
	for row in reader:
		inputX.append([row[0]])
		outputY.append(row[1])

lr = lm.LinearRegression()
lr.fit(inputX,outputY)

with open("test.csv",'rb') as csvtest:
	reader = csv.reader(csvtest)
	reader.next()
	for row in reader:
		textInput.append([float(row[0])])

print(lr.predict(textInput))