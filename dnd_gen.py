from random import randint
# set the main parameters
my_char = {
"Str" : 0,
"Dex" : 0,
"Con" : 0,
"Wis" : 0,
"Int" : 0,
"Cha" : 0,
}
#roll 3 dices for a random number
def dice_roll():
    dice_1 = randint(1, 6)
    dice_2 = randint(1, 6)
    dice_3 = randint(1, 6)
    total = dice_1 + dice_2 + dice_3
    return total

# add all values and assign it to parameter
def re_roll():
    counter_for_reroll = 3
    while counter_for_reroll > 0:
        print(f"\nYou have {counter_for_reroll} re-rolls left. Do you want to reroll \n")
        re_roll = input("y/n? ")

        if re_roll in ['y', "Y"]:
            param = input("\nWhich param do you want to re-roll? (Str/Dex/Con/Wis/Int/Cha) \n").capitalize()
            print(param)
            for key,value in my_char.items():
                if key != param:
                    # print("Checking parameters. Fail")
                    continue
                elif key == param:
                    my_char[key] = dice_roll()
                    print(f"\nNew value for {param} is {my_char[key]} \n")
                    print_out()
                    counter_for_reroll -=1

        elif re_roll in ['n', "N"]:
            break


#generate the character - This actually iterates through dictionary of "my_char & rolls dices for each param"
def generating():
    for key, value in my_char.items():
        my_char[key] = dice_roll()
        # print(my_char[key])

def print_out():
    for key, value in my_char.items():
        print(key, "--> ", value )

def main():
    while True:
        answer = input("Do you want to generate another character? y/n \n")
        if answer == 'y':
            generating()
            print_out()
            re_roll()
            print(my_char)
        elif answer == 'n':
            print("See you later, stranger")
            break
        else:
            print("The input should be 'y' or 'n' ")

main()

#you have 3 re-rolls left.
