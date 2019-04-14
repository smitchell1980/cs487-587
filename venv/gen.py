import csv
import random

with open('test.csv', mode='w') as employee_file:
    tupleCount = 1000000
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    numList = random.sample(range(0,tupleCount),tupleCount)
    for i in range(tupleCount):
        unique1 = numList[i]
        unique2 = i
        two= unique1 % 2
        four = unique1 % 4
        ten = unique1 % 10
        twenty = unique1 % 20
        onePercent = unique1 % 100
        tenPercent = unique1 % 10
        twentyPercent = unique1 % 5
        fiftyPercent = unique1 % 2
        unique3 = unique1
        evenOnePercent = onePercent *2
        oddOnePercent = onePercent * 2 + 1
        line = '"'+str(unique1)+'","'+str(unique2)+'","'+str(two)+'","'+str(four)+'","'+str(ten)
        line += '","' +str(twenty)+'","'+str(onePercent)+'","'+str(tenPercent)+'","'+str(twentyPercent)
        line += '","'+str(fiftyPercent)+'","'+str(unique3)+'","'+str(evenOnePercent)+'","'+str(oddOnePercent)+'"'
        #print(line)
        employee_writer.writerow([unique1])
