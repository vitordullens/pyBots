import telepot
import requests
from bs4 import BeautifulSoup

bot = telepot.Bot('681198688:AAE-GrSWuSorq2Gsu6ho_uU-FfXYzDFT5jY')

def getImg(id):
    url = 'http://www.funcage.com'
    r = requests.get(url, stream=True)

    soup = BeautifulSoup(r.text, 'html.parser')
    tag = soup.find_all("div", {"class":"cimg"})

    img = str(tag)
    img = img.split('src="')
    img = str(img[1])
    img = img.split('"')
    print('http://www.funcage.com' + img[0])
    bot.sendPhoto(id, 'http://www.funcage.com' + img[0])


def receivedMsg(msg):
    message = msg['text']
    id = msg['chat']['id']

    if(message.startswith('/kleber')):
        getImg(id)


bot.message_loop(receivedMsg)

while True:
    pass
