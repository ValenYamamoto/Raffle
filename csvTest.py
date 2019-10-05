import csv as csv
import random as random

fileName = input("What is the file name?") + ".csv"
print(fileName)

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
    global entries
    f = open(fileName, mode='r', newline="")

    for row in csv.reader(f):
        if(row[3] == "# of Prizes"):
            prizeNumbers = row[4:-1]
            #print(prizeNumbers)
        
        elif(row[0] == "Complete Name"):
            prizeNames = row[4:-1]
            print(prizeNames)

        else:
            if(row[0][0] != " "):
                entries[row[0]] = row[4:-1]

    for key, value in entries.items():
        print(key + " " + str(value) + " \n")



def getWinners():
    readFile()
    for prize in range(len(prizeNumbers)):
        winners = 0
        while winners < int(prizeNumbers[prize]):
            #print(int(prizeNumbers[prize]))
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

