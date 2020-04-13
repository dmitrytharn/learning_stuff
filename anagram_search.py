from palindrome_search import load

word_list = load("2of12inf.txt") #Your text file path goes here

def anagram_search():
    given_word = input("Input any word: ")
    given_word_listed = sorted(list(given_word.lower()))
    anagram_list = []
    for i in word_list:
        j = sorted(list(i))
        if j == given_word_listed and given_word != i:
            anagram_list.append(i)



    print(f'The search resulted in {len(anagram_list)} matches.')
    if len(anagram_list) > 0:
        print(f"Here are your anagrams for {given_word} ")
        for i in anagram_list:
            print(i)
    else:
        print("You should try another word next time")

if __name__ == "__main__":
    anagram_search()
