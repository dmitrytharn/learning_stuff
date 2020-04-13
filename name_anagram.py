import sys
from palindrome_search import load
from collections import Counter

word_list = load("2of12inf.txt")
word_list.append('a')
word_list.append('i')
word_list = sorted(word_list)

the_name = input("Enter the name: ")

def find_anagrams(name, word_list):
    name_letter_map = Counter(name)
    anagrams = []
    for word in word_list:
        test = ''
        word_letter_map = Counter(word.lower())
        for letter in word:
            if word_letter_map[letter] <= name_letter_map[letter]:
                test+=letter
        if Counter(test) == word_letter_map:
            anagrams.append(word)

    print(*anagrams, sep="\n")
    print()
    print(f"Remaining letters = {name}")
    print(f"Number of remaining letters = {len(name)}")
    print(f"Number of remaining (real word) anagrams = {len(anagrams)}")

def process_choice(name):
    while True:
        choice = input("\nMake a choice else Enter to start over or # to end: ")
        if choice == "":
            main()
        elif choice == "#":
            sys.exit()
        else:
            candidate = ''.join(choice.lower().split())

        left_over_list = list(name)
        for letter in candidate:
            if letter in left_over_list:
                left_over_list.remove(letter)
        if len(name) - len(left_over_list) == len(candidate):
            break
        else:
            print("Won't work! Make another choice!")
    name = ''.join(left_over_list)
    return choice, name

def main():
    name = ''.join(the_name.lower().split())
    name = name.replace('-', '')
    limit = len(name)
    phrase = ''
    running = True

    while running:
        temp_phrase = phrase.replace(" ", '')
        if len(temp_phrase) < limit:
            print(f"Length of anagram phrase = {len(temp_phrase)}")

            find_anagrams(name, word_list)
            print("Current anagram phrase = ", end = " ")
            print(phrase)

            choice, name = process_choice(name)
            phrase += choice + " "

        elif len(temp_phrase) == limit:
            print("\n*****FINISHED*****\n")
            print("Anagram of the name = ", end=" ")
            print(phrase)
            print()

            try_again = input("\n\nTry again? (Press Enter else \"n\" to quit)\n")
            if try_again.lower() == "n":
                running = False
                sys.exit()
            else:
                main()

if __name__ == "__main__":
    main()
