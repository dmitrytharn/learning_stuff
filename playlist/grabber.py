from bs4 import BeautifulSoup as bs
import requests

def grabbing(url):
    r = requests.get(url)
    page = r.text
    soup = bs(page,'html.parser')
    res = soup.find_all('h4')

    for i in res:
        # tit = soup.find_all('.yt-ui-ellipsis yt-ui-ellipsis-2')
        print(f"{i.text}\n")
        with open ("generated.txt", "a+") as file:
            file.write(i.text)

grabbing('https://www.youtube.com/watch?v=ACQFByE4f0E&list=PLykNNMVjCDfXxVouOUh_GZjLJP9_Esgig')
