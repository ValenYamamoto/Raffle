import csv as csv
import random as random

file = open("hypo.csv", "w+")
file.close()

file = open("hypo.csv", mode='a', newline='')
entries = {}
numbers = {}
prizeWinners = []

print("OPEN")

for i in range(1, 101):
    numbers[i] = 0

def readFile():
    f = open("test.csv", mode='r', newline="")
    
    for row in csv.reader(f):
        #self.entries[row[0]] = row[1]
        if(len(row) > 0):
            entries[row[0]] = row[1:]

def getWinners():
    readFile()

    for prize in range(len(entries["1"])-1):
        winners = 0

        while winners < 10:
            weight = []
            for i in list(entries.values()):
                weight.append(int(i[prize]))
            randomVal = random.choices(list(entries), weights=weight, k=1)
            if randomVal[0] not in prizeWinners:
                prizeWinners.append(randomVal[0])
                entries.pop(randomVal[0])
                winners = winners + 1

    



getWinners()
for key in prizeWinners:
    #print(str(key))
    writer = csv.writer(file)
    writer.writerow((key, 0))
file.close()
print("Done")

