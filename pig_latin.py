'''get a word from input. if the first letter in the word is consonant -> more it to the end of the word and add "ay" to it
   if the word beging with vowel  = just add "way to the end of it."
'''
def pig_latin_game():
    print("Welcome to the silly application called 'Pig Latin'. It messes up the words you input in some manner. \n")
    print(" Give it a try by inputing a word.\n")
    print("Say 'EXIT' to quit. \n")
    while True:
    #Determine user input
        words = []
        entries = input("Say the word! ")
        words = entries.split()
        new_words = []
        for word in words:
            if word[0] in ("a", "e", "o", 'u', 'i',):
                new_word = word + "way"
                new_words.append(new_word)
                #most probably you want to use REGEX here :)
            elif word[0] in ("q", "w", 'r', 't', 'y', 'p', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm'):
                new_word = word[1:]+word[0]+"ay"
                new_words.append(new_word)
        if entries == "EXIT":
                break

        else:
            print("This doesn't actually look like a word to me. Try again. ")



        print("\n")
        print(" ".join(new_words))
        print("\n")

pig_latin_game()
print("See you later")

'''this can be improved by accepting cap letters as well, also REGEX. + this is not getting inputs in format like
"Hello! This is me, Mario!"'''
