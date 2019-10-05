import csv as csv
import random as random

file_name = input("What is the file name?") + ".csv"
print(file_name)

file = open("RaffleWinners.csv", "w+")
file.close()

file = open("RaffleWinners.csv", mode='a', newline='')
entries = {}
prize_numbers = []
prize_names = []
prize_winners = {}
max_wins = 1

print("OPEN")

def read_file():
    global prize_numbers
    global prize_names
    global entries
    f = open(file_name, mode='r', newline="")

    for row in csv.reader(f):
        if(row[3] == "# of Prizes"):
            prize_numbers = row[4:-1]
            #print(prize_numbers)
        
        elif(row[0] == "Complete Name"):
            prize_names = row[4:-1]
            #print(prize_names)

        else:
            if(row[0][0] != " "):
                entries[row[0]] = row[4:-1]

    for key, value in entries.items():
        print(key + " " + str(value) + " \n")



def get_winners():
    read_file()
    for prize in range(len(prize_numbers)):
        winners = 0
        while winners < int(prize_numbers[prize]):
            #print(int(prize_numbers[prize]))
            weight = []
            for i in list(entries.values()):
                weight.append(int(i[prize]))
            random_val = random.choices(list(entries), weights=weight, k=1)
            if random_val[0] not in prize_winners:
                prize_winners[random_val[0]] = [prize_names[prize]]
                #entries.pop(random_val[0])
                winners = winners + 1
            elif len(prize_winners[random_val[0]]) < max_wins:
                if prize_names[prize] not in prize_winners[random_val[0]]:
                    prize_winners[random_val[0]].append(prize_names[prize])
                    winners = winners + 1
                    if len(prize_winners[random_val[0]]) >= max_wins:
                        entries.pop(random_val[0])
    

get_winners()
for name, prize_list in prize_winners.items():
    writer = csv.writer(file)
    writer.writerow((name, prize_list))

    
for prize in prize_names:
    print()
    print(prize)
    for name, prize_list in prize_winners.items():
        if prize in prize_list:
            print(name)

file.close()

print("Done")

