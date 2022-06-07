import discord
from discord.ext import commands
from matplotlib.style import use
import requests
from bs4 import BeautifulSoup
id = 'KomaCrazy'

url = 'https://apex.tracker.gg/apex/profile/origin/'+id+'/overview'
web = requests.get(url)
soup = BeautifulSoup(web.text, 'html.parser')
word1 = soup.find_all("span",{"trn-ign__username"})
user = str(word1).split('<span class="trn-ign__username" data-v-47e2d440="">')
user = str(user[1]).split("\n")
user = str(user[1]).split(" ")
user = user[6]




word2 = soup.find_all("div",{"value"})
rank = str(word2).split('<div class="value" data-v-3d7a1831=""><!-- --> <span class="mmr" data-v-3d7a1831="">')
rank = str(rank).split("<")
rank = str(rank[0]).split(" ")
rank = rank[15]
print(" Apex gmae")
print("user : ",user)
print("rank : ",rank,"RP")