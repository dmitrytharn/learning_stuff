import sys
import time
start_time = time.time()

def load(file): # this function reads the data from txt file and gets it ready for further usage
    try:
        with open(file) as in_file:
            loaded_txt = in_file.read().strip().split("\n")
            loaded_txt = [x.lower() for x in loaded_txt]
            return loaded_txt
    except IOError as e:
        print("{}\nError opening {}. Terminating program".format(e, file), file=sys.stderr)
        sys.exit(1)

loaded_text = load() #input your sample text file path here

def find_palingrams():
    pali_list = []
    words = set(loaded_text)
    for word in words:
        end = len(word)
        reversed = word[::-1]
        if end > 1:
            for i in range(end):
                if word[i:] == reversed[:end-i] and reversed[end-i: ] in  words: #
                    pali_list.append((word, reversed[end-i:]))
                if word[:i] == reversed[end-i:] and reversed[:end-i] in words:
                    pali_list.append((reversed[:end-i], word))
    return pali_list

palingrams = find_palingrams()
palingrams_sorted = sorted(palingrams)
end_time = time.time()
print(f"\nNumber of palingrams found {len(palingrams_sorted)} ")
for first, second in palingrams_sorted:
    print(f"{first}, {second}")
print(f"The program finished running. \nIt took {end_time - start_time} seconds to execute")
