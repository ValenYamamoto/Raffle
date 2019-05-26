import csv as csv
import random as random

file = open("RaffleWinners.csv", "w+")
file.close()

file = open("RaffleWinners.csv", mode='a', newline='')
entries = {}
numbers = {}
prizeNumbers = []
prizeNames = []
prizeWinners = {}
maxWins = 1

print("OPEN")

def readFile():
    f = open("RaffleData.csv", mode='r', newline="")
    
    for row in csv.reader(f):
        if(row[0] == "# of Prizes"):
            prizeNumbers.append(row[1:])
        
        elif(row[0] == "Name"):
             prizeNames.append(row[1:])

        else:
            if(len(row) > 0):
                entries[row[0]] = row[1:]


def getWinners():
    readFile()

    for prize in range(len(prizeNumbers[0])):
        winners = 0
        
        while winners < int(prizeNumbers[0][prize]):
            weight = []
            for i in list(entries.values()):
                weight.append(int(i[prize]))
            randomVal = random.choices(list(entries), weights=weight, k=1)
            if randomVal[0] not in prizeWinners:
                prizeWinners[randomVal[0]] = [prizeNames[0][prize]]
                #entries.pop(randomVal[0])
                winners = winners + 1
            elif len(prizeWinners[randomVal[0]]) < maxWins:
                if prizeNames[0][prize] not in prizeWinners[randomVal[0]]:
                    prizeWinners[randomVal[0]].append(prizeNames[0][prize])
                    winners = winners + 1
                    if len(prizeWinners[randomVal[0]]) >= maxWins:
                        entries.pop(randomVal[0])
    



getWinners()
for key, val in prizeWinners.items():
    #print(str(key))
    writer = csv.writer(file)
    writer.writerow((key, val))
file.close()
print(pri
print("Done")

