import requests
from bs4 import BeautifulSoup

url = 'https://r6.tracker.network/profile/pc/KomaCrazy'
web = requests.get(url)
soup = BeautifulSoup(web.text, 'html.parser')
find_word = soup.find_all("div",{"trn-defstat__value"})
print(find_word)

for i in find_word :
    print(i)
