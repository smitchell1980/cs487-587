import csv
import random

def convert(unique):
    result = list("AAAAAAAxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    i = 6
    cnt = 0
    while unique > 0:
        rem = unique % 26
        result[i]=chr(ord('A')+rem)
        unique = int(unique/26)
        i = i-1
        cnt = cnt +1
    return "".join(result)

def str4Select(index):
    switcher = {
        0: "AAAAxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        1: "HHHHxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        2: "OOOOxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        3: "VVVVxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
        }
    return switcher.get(index%4)

with open('test.csv', mode='w' newline='') as employee_file:
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
        #line = '"'+str(unique1)+'","'+str(unique2)+'","'+str(two)+'","'+str(four)+'","'+str(ten)
        #line += '","' +str(twenty)+'","'+str(onePercent)+'","'+str(tenPercent)+'","'+str(twentyPercent)
        #line += '","'+str(fiftyPercent)+'","'+str(unique3)+'","'+str(evenOnePercent)+'","'+str(oddOnePercent)+'"'
        #print(line)
        employee_writer.writerow([unique1, unique2, two, four, ten, twenty, onePercent, tenPercent, twentyPercent, fiftyPercent, unique3, evenOnePercent, oddOnePercent, stringu1, stringu2, string4])
