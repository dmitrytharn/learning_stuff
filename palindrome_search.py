''' Looks through a text file in search of palindromes (E.g.: stats, bob, anna, etc)
Prints out the number of palindromes found in a file and prints them out. 60.000 word dictionary returns ~60 palindromes.'''

import sys

def load(file):
    try:
        with open(file) as in_file:
            loaded_txt = in_file.read().strip().split("\n")
            loaded_txt = [x.lower() for x in loaded_txt]
            return loaded_txt
    except IOError as e:
        print("{}\nError opening {}. Terminating program".format(e, file), file=sys.stderr)
        sys.exit(1)


def check_for_palindromes(value):
    pali_list = []
    for i in value:
        if (len(i)> 1) and i[::-1] == i[::]:
            pali_list.append(i)
    print(f"Number of palindromes found = {len(pali_list)}")
    print(*pali_list, sep="\n")
    return pali_list

if __name__ == "__main__":
    check_for_palindromes(load("sample_text_file.txt"))
