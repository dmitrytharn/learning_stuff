'''get a word from input. if the first letter in the word is consonant -> more it to the end of the word and add "ay" to it
   if the word beging with vowel  = just add "way to the end of it."
'''
def pig_latin_game():
    print("Welcome to the silly application called 'Pig Latin'. It messes up the words you input in some manner. \n")
    print(" Give it a try by inputing a word.\n")
    print("Say 'EXIT' to quit. \n")
    while True:
    #Determine user input

        the_word = input("Say the word! ")
        if the_word[0] in ("a", "e", "o", 'u', 'i',):
            new_word = the_word + "way"
            print("\n" +new_word+ "\n")
            #most probably you want to use REGEX here :)
        elif the_word[0] in ("q", "w", 'r', 't', 'y', 'p', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm'):
            new_word = the_word[1:]+the_word[0]+"ay"
            print("\n" +new_word+ "\n")
        elif the_word == "EXIT":
            print("goodbye!")
            break
        else:
            print("This doesn't actually look like a word to me. Try again. ")

pig_latin_game()
print("See you later")

'''this can be improved by accepting cap letters as well, also - multiple words/sentences and REGEX'''
