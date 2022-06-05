import requests
from bs4 import BeautifulSoup
id = 'KomaCrazy'
url = 'https://r6.tracker.network/profile/pc/' + id 
web = requests.get(url)
soup = BeautifulSoup(web.text, 'html.parser')
find_word = soup.find_all("div",{"trn-defstat__value"})

win = str(find_word[13]).split('<div class="trn-defstat__value" data-stat="PVPMatchesWon">')
win = str(win[1]).split('\n')
win = win[1]

kills = str(find_word[3]).split('<div class="trn-defstat__value" data-stat="PVPKills">')
kills = str(kills[1]).split('\n')
kills = kills[1]

Winrate = str(find_word[47]).split('<div class="trn-defstat__value" data-stat="CasualWLRatio">')
Winrate = str(Winrate[1]).split('\n')
Winrate = Winrate[1]

print("__________________")
print("user : ",id)
print("Wins : ",win) # Win
print("Kills : ",kills) # Kills
print("Winrate : ",Winrate) # Kills
print("__________________")


#print(find_word[10])#