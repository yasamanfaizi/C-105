import csv
import math

f = open("class2.csv")
file = csv.reader(f)
data = list(file)
data.pop(0)
StudentNumber = []
for i in range(0,len(data)):
    num = data[i][0]
    StudentNumber.append(int(num))

sum = 0
for i in StudentNumber:
    sum = sum+i

mean = sum/len(StudentNumber)
print(mean)

square = []
for i in StudentNumber: 
    a = int(i)-mean
    a = a**2
    square.append(a)

sum = 0
for i in square:
    sum = sum+i

result = sum/(len(StudentNumber)-1)

div = math.sqrt(result)
print(div)

import statistics
div = statistics.stdev(StudentNumber)
print(div)
