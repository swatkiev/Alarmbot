import requests
import json
import surrogates
import telebot

TOKEN = "PUT HERE YOUR TOKEN FROM BOTFATHER"
bot = telebot.TeleBot(TOKEN)

users = []

headers = {
    'X-API-Key': 'foo',
}

ALARM_API = "http://app:10101/api/states/25"

response = requests.get(ALARM_API, headers=headers)

response1 = response.json()

response2 = response1['state']

newresponce = response2['alert']

responcefile = 'responce.data'

emojigreen = (surrogates.decode('\uD83D\uDFE2'))
emojired = (surrogates.decode('\uD83D\uDD34'))

@bot.message_handler(commands=['start'])
def start_message(msg):
    bot.send_message(msg.chat.id, 'Привіт! Цей бот сповіщає про повітряну тривогу у м. Київ')
    if msg.chat.id not in users: # if the id isn't already in the users list
        users.append(msg.chat.id)

@bot.message_handler(commands=['renew'])
def alarm(msg):
    with open(responcefile, 'r') as fl:
        oldresponce = json.load(fl)
    if (newresponce != oldresponce and newresponce == False):
        oldresponce = newresponce
        with open(responcefile, 'w') as fl:
            json.dump(oldresponce, fl)
        for id in users: # for every user that has start the bot
            bot.send_message(id, "{} Відбій повітряної тривоги Київ".format(emojigreen))
    elif (newresponce != oldresponce and newresponce == True):
          oldresponce = newresponce
          with open(responcefile, 'w') as fl:
              json.dump(oldresponce, fl)
          for id in users: # for every user that has start the bot
              bot.send_message(id, "{} Повітряна тривога Київ".format(emojired))

bot.polling()
