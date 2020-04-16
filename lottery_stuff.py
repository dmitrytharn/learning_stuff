''' This script allows you to input x amount of digits to form a "ticket" (list of those numbers)
and check how many times you have to generate another list of 4 numbers (won_ticket)
to match yours. Other words = lotteries have pretty bad rates, I'd say.
I left the value extra low, for demo purposes'''

from random import randrange, choice

lottery = list(range(1, 11))

def user_choice_get():
    print("Welcome to lottery! Input digits you think will win")
    user_choice = []
    while len(user_choice) < 2:
        choice = input(f"Enter digits from 1 to {len(lottery)}: ")
        try:
            if choice == "exit":
                break
            choice = int(choice)
            if choice > 0 and choice < 11:
                user_choice.append(choice)
                print(f"{choice} added to your ticket. It contains {user_choice} now")
            else:
                print("That's not a correct number to add")
                print(f"your ticket contains {user_choice} now")

        except ValueError:
            print("Something went wrong!")
            print(f"your ticket contains {user_choice} now")

    if user_choice and len(user_choice) == 2:
        return user_choice
    else:
        print("You didn't provide all 2 numbers for lottery ticket")

my_ticket = user_choice_get()

def run_the_show():
    counter = 0
    won_ticket = None
    for i in range(1, 100000000):
        if won_ticket != my_ticket:
            won_ticket = random_ticket()
            counter += 1
        else:
            break

    if won_ticket == my_ticket:
        print(f"Match of {my_ticket} found!")
        print(f"\nIt took {counter} tries to crack the lottery!")
    else:
        print(f"I ran {counter} attempts but the match was not found")
        print(f"your ticket was{my_ticket}")

def random_ticket():
    won_ticket = []
    while len(won_ticket) < 2:
        x = choice(lottery)
        won_ticket.append(x)
    return won_ticket


run_the_show()
