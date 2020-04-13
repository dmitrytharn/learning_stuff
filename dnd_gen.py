from random import randint
from name_gen import get_name
import random

# set the main parameters
my_char = {
"Str" : 0,
"Dex" : 0,
"Con" : 0,
"Wis" : 0,
"Int" : 0,
"Cha" : 0,
}

# # **************************STRENGTH DESCRIPTIONS *************************************************
stren = (
("You are a winner in genetics lottery. Born as an image of gods for this plane.",
"You were gifted with the incredible power when you were born",
"You are a prodigy. Born with exceptional strength, you were meant to rule this world")
,
("You were brough to this world with a gift of strength. As you grew older - the stronger you became",
"You were given a blessing of unusual strength. You are much stronger than people around you.",
"Your body flows with the energy. You are stronger than most of the folks around you."),

("You are quite powerful individual. Your physical strength is above the average",
"At some days you feel you could crush the mountains. You are quite a strong person",
"You strength was noticed since early days from your birh. People around you say, you could be a great warrior"),

("You seem to be in good shape since the early days of your life. Nothing mystical, just a good source of power within your muscles",
"Your mom always told you that you are the strongest around. You are not sure if this is true, but you can surely feel some strength in your arms",
"You are a well developed individual with a light touch of perfection when it comes to your strenght."),

("You have quite an average strength within you. Nothing special, but nothing wrong with it.",
"You know people who are much stronger than you. But since when it was a problem? You are pleased with your capabilities and know how to use them",
"You have quite a good health. You get tired just like all the normal folks around you. Normal is the new great"),

("You can't say you're strong. You're normal. Maybe even a bit less than normal. You get tired quickly and not fond of lifting heavy things",
"When it comes to rough physical work - you're not the best choice. Lifting weights makes your back hurt a bit.",
"If the King would give a call for strong people in the kingdom - you wouldn't hear about it. You're not strong. You're slightly below average when it comes to strength"),

("You always despited physical activities. Lifting things is for other people. You can barely grab a fullcast iron pan from the stove. Strength is definitely not your talent",
"You were born a weak child. From the very first day everyone around you knew you wouldn't be a great warrior.",
"Truth hurts. You're weak. Probably, one of the weakest folks around. You got mocked in your childhood on this. So you decided to focus on developing other traits."),

("You were born as a catastrophe. Your strength is so low, that holding a mug of ale brings you pain and discofort.",
"Your birth feels like it was a curse rather than a gift. You were born with muscle atrophy. Holding something heavier than a book makes your arms tremble",
"You are the walking example of 'weak'. Poor genetics, gods anger or a curse, probably? Anyway, you are so weak, that just holding your body on your two feet feels like a challenge sometimes"),
)
# # **************************DEXTERITY DESCRIPTIONS *************************************************
dex = (('1', "2"), ('3', "4"), ('5', "6"), ('7', "8"), ('9', '10'), ('11', '12'), ('13', '14'), ('15', '16'),)

# # **************************CONSTITUTION DESCRIPTIONS *************************************************
con = (('one', "2"), ('two', "3"), ('three', "4"), ('four', "6"), ('5', '9'), ('6', '123'), ('7', '321'), ('8', '9'),)

# # **************************WISDOM DESCRIPTIONS *************************************************
wis = (('a', "b"), ('c', "d"), ('e', "f"), ('g', "h"), ('i', 'j'), ('k', 'l'), ('m', 'n'), ('o', 'p'),)

# # **************************ITELLIGENCE DESCRIPTIONS *************************************************
int = (('one', "2"), ('two', "3"), ('three', "4"), ('four', "6"), ('5', '9'), ('6', '123'), ('7', '321'), ('8', '9'),)

# # **************************CHARISMA DESCRIPTIONS *************************************************
cha = (('one', "2"), ('two', "3"), ('three', "4"), ('four', "6"), ('5', '9'), ('6', '123'), ('7', '321'), ('8', '9'),)

#core function that triggers dice_roll() function for all key:values pairs in my_char dictionary
def generating():
    for key, value in my_char.items():
        my_char[key] = dice_roll()
        # print(my_char[key])

# basic print function that prettifies the output by iterating through dictionary
def print_out():
    for key, value in my_char.items():
        print(key, "--> ", value )

# this function allows re-roll of chosen stat by input from player. It rewrites the values for keys in my_char dictionary
def re_roll():
    counter_for_reroll = 3
    while counter_for_reroll > 0:
        print(f"\nYou have {counter_for_reroll} stat re-rolls left. Do you want to reroll a stat?\n")
        re_roll = input("y/n? ")

        if re_roll in ['y', "Y"]:
            param = input("\nWhich stat do you want to re-roll? (Str/Dex/Con/Wis/Int/Cha) \n").capitalize()
            # print(param)
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

    return my_char


# This function checks if the generated parameter of my_char belongs to a certain category ranked (F - SS)
# Returns a new dict with same keys, but values set to validate the stat by rank
def check_if_stat_is_big(char_to_check):
    char_close_look = {}
    for key, value in my_char.items():
        if value  < 2:
            char_close_look[key] = "F"
        elif value <= 5 and value > 1:
            char_close_look[key] = "E"
        elif value <= 7 and value > 5:
            char_close_look[key] = "D"
        elif value <= 10 and value > 7:
            char_close_look[key] = "C"
        elif value <= 12 and value > 10:
            char_close_look[key] = "B"
        elif value <= 15 and value > 12:
            char_close_look[key] = "A"
        elif value < 18 and value > 15:
            char_close_look[key] = "S"
        elif value == 18:
            char_close_look[key] = "SS"

    return char_close_look


# This function evaluates given dictionary (Here - a result of check_if_stat_is_big function). It looks if key in the param dict is equal to desired("given") key,
# and iterates through certain lists based on value of the key given. E.g. Valuator(result, Stren, "Str") will loop through "char_close_look" (assigned to be "result")
# and if given (key) == "Str" it will loop through Stren list (top of script) and make a random choice from lists in list according to value of the stat.
def valuator(param, list, given):
    for key, value in param.items():
        if key == given:
            if value == "SS":
                summary = random.choice(list[0])
            elif value == "S":
                summary = random.choice(list[1])
            elif value == "A":
                summary = random.choice(list[2])
            elif value == "B":
                summary = random.choice(list[3])
            elif value == "C":
                summary = random.choice(list[4])
            elif value == "D":
                summary = random.choice(list[5])
            elif value == "E":
                summary = random.choice(list[6])
            elif value == "F":
                summary = random.choice(list[7])

            return summary

# This function sets the parameter for valuator above and loops through this dict checking if individual valuator for parameter should be ran.
# returns descriptions for each parameter
def lets_go():
    result = check_if_stat_is_big(my_char)
    for key, value in result.items():
        if key == "Str":
            strn = valuator(result, stren, "Str")
        elif key == "Dex":
            dext = valuator(result, dex, "Dex")
        elif key == "Con":
            cons = valuator(result, con, "Con")
        elif key == "Wis":
            wisd = valuator(result, wis, "Wis")
        elif key == "Int":
            inte = valuator(result, int, "Int")
        elif key == "Cha":
            cha_ism = valuator(result, cha, "Cha")

    return strn, dext, cons, wisd, inte, cha_ism
    # print(str_sum)

#roll 3 dices for a random number
def dice_roll():
    dice_1 = randint(1, 6)
    dice_2 = randint(1, 6)
    dice_3 = randint(1, 6)
    total = dice_1 + dice_2 + dice_3
    return total

def main():
    while True:
        answer = input("Do you want to generate another character? y/n \n")
        if answer == 'y':
            generating()
            print_out()
            re_roll()
            print(my_char)
            name = get_name()
            print(name)
            print(str(my_char) + "\n")
            strn, dext, cons, wisd, inte, cha_ism = lets_go()
            print(f"{strn} \n\n")
            with open ("char.txt", "a+") as file:
                file.write(name + "\n")
                file.write(str(my_char)+"\n")
                file.write(str() + "\n\n")
        elif answer == 'n':
            print("See you later, stranger")
            break
        else:
            print("The input should be 'y' or 'n' \n")


if __name__ == "__main__":
    print("Welcome to Roleplaying Character Generator v.0.1 \n")
    print("*******************************************************************************")
    print("With the help of this script you can easily create a character in few steps\n")
    main()

#you have 3 re-rolls left.
