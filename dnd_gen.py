from random import randint
# set the main parameters
my_char = {
"Strength" : 0,
"Dexterity" : 0,
"Constitution" : 0,
"Wizdom" : 0,
"Intelligence" : 0,
"Charisma" : 0,
}
#roll 3 dices for a random number
def dice_roll():
    dice_1 = randint(1, 6)
    dice_2 = randint(1, 6)
    dice_3 = randint(1, 6)
    total = dice_1 + dice_2 + dice_3
    return total

# add all values and assign it to parameter

#generate the character - This actually iterates through dictionary of "my_char & rolls dices for each param"
def generating():
    for key, value in my_char.items():
        my_char[key] = dice_roll()
        # print(my_char[key])


    for key, value in my_char.items():
        print(key, "--> ", value )

while True:
    answer = input("Do you want to generate another character? y/n \n")
    if answer == 'y':
        generating()
    elif answer == 'n':
        print("See you later, stranger")
        break
    else:
        print("The input should be 'y' or 'n' ")
