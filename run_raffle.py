import csv as csv
import random as random


OUTPUT_FILE_NAME = "RaffleWinners.csv"
MAX_WINS = 1


def read_file(file_name: str):
    with open(file_name) as f:
        reader = csv.reader(f)
        prize_numbers = [int(i) for i in next(reader)[4:-1]]
        prize_names = next(reader)[4:-1]
        entries = {row[0] : row[4:-1] for row in reader if row[0][0] != " "}

    return prize_numbers, prize_names, entries


def get_winners(prize_number, prize_name, entries):
    prize_winners = {}
    for prize in range(len(prize_numbers)):
        winners = 0
        while winners < prize_numbers[prize]:
            weight = [int(i[prize]) for i in entries.values()]
            random_val = random.choices(list(entries), weights=weight, k=1)
            if random_val[0] not in prize_winners: # Person is not yet a winner
                prize_winners[random_val[0]] = [prize_names[prize]]
                winners = winners + 1
            elif len(prize_winners[random_val[0]]) < MAX_WINS: # Person has won less than max_wins
                if prize_names[prize] not in prize_winners[random_val[0]]:
                    prize_winners[random_val[0]].append(prize_names[prize])
                    winners = winners + 1
                    if len(prize_winners[random_val[0]]) >= MAX_WINS:
                        del entries[random_val[0]]
    return prize_winners
    



if __name__ == "__main__":
    file_name = input("What is the file name?") + ".csv"
    print("Reading Data from: " + file_name)

    prize_numbers, prize_names, entries = read_file(file_name)
    winners = get_winners(prize_numbers, prize_names, entries)

    with open(OUTPUT_FILE_NAME, mode='w') as file:
        print("Writing to: " + OUTPUT_FILE_NAME)
        for name, prize_list in winners.items():
            writer = csv.writer(file)
            writer.writerow((name, prize_list))

    for prize in prize_names:
        print()
        print(prize)
        for name, prize_list in winners.items():
            if prize in prize_list:
                print(name)

    print("DONE")
