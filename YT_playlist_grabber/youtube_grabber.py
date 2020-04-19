import requests
from bs4 import BeautifulSoup

url = 'https://www.youtube.com/channel/UCzCWehBejA23yEz3zp7jlcg/videos'
response = requests.get(url)
page = response.text
soup = BeautifulSoup(page, 'html.parser')
links = soup.find_all('div', id='content')




for each in links:
    print(each.text)
    with open("list.txt", "a+") as file:
        file.write(each.text)
