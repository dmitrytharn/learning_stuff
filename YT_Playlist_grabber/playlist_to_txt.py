'''This script project was made because I was not really happy with the need of
copying manually titles of new released albums from Black Metal Promotions page
on YouTube and pasting them into Spotify.

So, basically this script asks you to input a url to video playlist page from YT.
For example: https://www.youtube.com/watch?v=6XW0rDX6nhc&list=PLykNNMVjCDfXjYUvYqzvQLVPFMSFTUabS
Then it asks you to choose the name for the file where the data will be saved.
For example: my_playlist.txt
Later on it scans the file for any "Full Album" match (as the channel also includes
track premiers and Official Videos to those lists) and creates a "clean version"
of it stripping whitespaces and sorting out all the full albums entries.

Example: Khora - Timaeus (Full Album) ==> Khora - Timaeus

I could make it output only the clean file itself without the need to created
both, but sometimes you want the full initial file without the cleaning.
'''

from bs4 import BeautifulSoup as bs
import requests

def grabbing(url):
    r = requests.get(url)
    page = r.text
    soup = bs(page,'html.parser')
    res = soup.find_all('h4')
    file_name = input("Please input the name of the desired output file in *.txt format: \n")

    for i in res:
        print(f"{i.text}\n")
        with open (file_name, "a+") as file:
            file.write(i.text)

    print(file_name)
    return file_name

# grabbing('https://www.youtube.com/watch?v=sRr21ya1tBo&list=PLykNNMVjCDfUONxfFCEGKCi4Uq676skR7')

def cleaning(input, output):
    with open(input) as file:
        content = file.readlines()

    new_conten = []
    for i in content:
        if ("(Full Album)") in i:
            j = i.replace("(Full Album)", '')
            new_conten.append(j)
        if ("Full Album Premier" in i):
            j = i.replace("(Full Album Premiere)", "")
            new_conten.append(j)

    for i in new_conten:
        print(i)

    with open(output, "a+") as f:
        for i in new_conten:
            f.write(i.lstrip() + "\n")


if __name__ == "__main__":
    print("This script exports all video titles from YouTube channel. Enter quit/exit to terminate: \n")
    while True:
        url = input("Enter the link to Youtube Playlist here: ")
        if url in ["quit", "exit"]:
            print("See you later!")
            break
        if url[:23] != "https://www.youtube.com":
            print("Are you sure this is a correct link? \n")
        elif len(url) < 30:
            print("Are you sure this is a correct link? \n")
        else:
            input_file = grabbing(url)
            output_file = "Cleaned_" + input_file
            print("Grabbing of the playlist complete!\n")
            cleaning(input_file, output_file)
            print("New Playlist created and cleaned\n")
