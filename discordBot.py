import discord
import asyncio
import requests
from bs4 import BeautifulSoup

client = discord.Client()

@client.event
async def on_ready():
	print(client.user.name)
	print(client.user.id)

@client.event
async def on_message(message):

    msg = message.content.lower()

    if(msg.startswith("!kleber")):
        url = 'http://www.funcage.com'
        r = requests.get(url, stream=True)

        soup = BeautifulSoup(r.text, 'html.parser')
        tag = soup.find_all("div", {"class":"cimg"})

        img = str(tag)
        img = img.split('src="')
        img = str(img[1])
        img = img.split('"')
        img = 'http://www.funcage.com' + img[0]
        await client.send_message(message.channel, img)



client.run('*** TOKEN HERE ***')