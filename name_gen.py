import sys
import random

# Set the tuples with first name & last name to pick with
first_name = ("Ficadon","Fickfylo","Fildon","Firedorn","Firiro","Floran","Folmard",'Fraderk','Fronar','Fydar','Fyn')
last_name = ("Dragonborne", "Stormbreaker", "Mountaintop", "Grimmerwald", "Axechop", "Foldings", "Willingfoe")


# Greet the player and explain what this script does!

#chreate a main loop where the player will decide if he wants to generate or quit the program
def get_name():

    print("Welcome to magnificent Fantasy Name generator! \n")
    print("Here you can create a name for your character with a simple press of a button! \n")
    while True:

        chosen_first = random.choice(first_name)
        chosen_last = random.choice(last_name)
        answer = input("Do you want to generate a name for your character now? y/n ")

        if answer == "y":
            print("\n")
            print(f"Random character name: {chosen_first} {chosen_last}")
            print("\n")
            new_name = chosen_first + " " + chosen_last
        elif answer == "n":
            name = "Unnamed character"
            print("Ok. See you again!")
            break
        elif answer == "n" and new_name:
            name = new_name
            print("Ok. See you again!")
            break
        elif answer not in ["y", 'n']:
            print("Just 'y' or 'n' please")
    try:
        return new_name
    except UnboundLocalError:
        return name


    #     if answer == "n":
    #         if len(name) < 3:
    #             name = "Unnamed character"
    #         else:
    #             name =
    #         print("Ok. See you again!")
    #         break
    #     elif answer not in ["y", 'n']:
    #         print("Just 'y' or 'n' please")
    # return name



if __name__ == "__main__":
    get_name()
