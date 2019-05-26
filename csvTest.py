import csv as csv
import random as random

file = open("RaffleWinners.csv", "w+")
file.close()

file = open("RaffleWinners.csv", mode='a', newline='')
entries = {}
prizeNumbers = []
prizeNames = []
prizeWinners = {}
maxWins = 1

print("OPEN")

def readFile():
    global prizeNumbers
    global prizeNames
    f = open("RaffleData.csv", mode='r', newline="")

    for row in csv.reader(f):
        if(row[0] == "# of Prizes"):
            global.prizeNumbers = row[1:]
        
        elif(row[0] == "Name"):
            global.prizeNames = row[1:]

        else:
            if(len(row) > 0):
                entries[row[0]] = row[1:]


def getWinners():
    readFile()

    for prize in range(len(prizeNumbers)):
        winners = 0
        while winners < int(prizeNumbers[prize]):
            weight = []
            for i in list(entries.values()):
                weight.append(int(i[prize]))
            randomVal = random.choices(list(entries), weights=weight, k=1)
            if randomVal[0] not in prizeWinners:
                prizeWinners[randomVal[0]] = [prizeNames[prize]]
                #entries.pop(randomVal[0])
                winners = winners + 1
            elif len(prizeWinners[randomVal[0]]) < maxWins:
                if prizeNames[prize] not in prizeWinners[randomVal[0]]:
                    prizeWinners[randomVal[0]].append(prizeNames[prize])
                    winners = winners + 1
                    if len(prizeWinners[randomVal[0]]) >= maxWins:
                        entries.pop(randomVal[0])
    

getWinners()
for name, prizeList in prizeWinners.items():
    writer = csv.writer(file)
    writer.writerow((name, prizeList))
for prize in prizeNames:
    print()
    print(prize)
    for name, prizeList in prizeWinners.items():
        if prize in prizeList:
            print(name)

file.close()

print("Done")

