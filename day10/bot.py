import discord
from discord.ext import commands
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

bot = commands.Bot(command_prefix='?>')

box1 = 0
box2 = ""
box3 = ""


@bot.event
async def on_ready() : #เมื่อระบบพร้อมใช้งาน
    print("Bot Started!") #แสดงผลใน CMD
# message.content
@bot.event
async def on_message(message) :
    msg = str(message.content)
    i = 0
    if msg == "KomaCrazy" :
        await message.channel.send("user : " + str(id) +\
            "\n" + "Wins : " +str(win) +\
            "\n" + "Kills : " +str(kills)+\
            "\n" + "Kills : " +str(kills)+\
            "\n" + "Winrate : " +str(Winrate)+\
            "\n" + "Web : "+ url)    
bot.run('OTc2MDA5MjQyNTY3OTA1MzEw.GD8sW6.E043lTDQ2O9LF0M10XPNHBuu1176qXhUZtGvVE')
