import csv as csv
import random as random

file = open("hypo.csv", "w+")
file.close()

file = open("hypo.csv", mode='a', newline='')
entries = {}
numbers = {}
for i in range(1, 101):
    numbers[i] = 0

def readFile():
    f = open("test.csv", mode='r', newline="")
    
    for row in csv.reader(f):
        #self.entries[row[0]] = row[1]
        if(len(row) > 0):
            if(row[0] not in entries):
                entries[row[0]] = int(row[1])
            else:
                entries[row[0]] = entries[row[0]] + int(row[1])

def getWinners():
    readFile()
    weight = []
    
    for i in list(entries.values()):
        weight.append(int(i))
        
    randomVal = random.choices(list(entries), weights=weight, k=10)

    for num in randomVal:
        num = int(num)
        numbers[num] = numbers[num]+1

    



for i in range(1000):
    getWinners()
    
for key,val in numbers.items():
        writer = csv.writer(file)
        writer.writerow((key, val))
file.close()

