import http.client
import json
import surrogates
import telebot
import socket
from telebot.apihelper import ApiTelegramException
from json.decoder import JSONDecodeError

TOKEN = "PUT HERE YOUR TOKEN FROM BOTFATHER"
bot = telebot.TeleBot(TOKEN)
userdata = 'users.data'
responcefile = 'responce.data'
emojigreen = (surrogates.decode('\uD83D\uDFE2'))
emojired = (surrogates.decode('\uD83D\uDD34'))

@bot.message_handler(commands=['start'])
def start_message(msg):
    with open(userdata, 'r') as fl:
        users = json.load(fl)
    bot.send_message(msg.chat.id, 'Привіт! Цей бот сповіщає про повітряну тривогу у м. Київ')
    if msg.chat.id not in users: # if the id isn't already in the users list
        users.append(msg.chat.id)
        with open(userdata, 'w') as fl:
            json.dump(users, fl)

@bot.message_handler(commands=['renew'])
def alarm(msg):
    try:
        with open(userdata, 'r') as fl2:
            users = json.load(fl2)
        conn = http.client.HTTPConnection("ubilling.net.ua")
        conn.request("GET", "/aerialalerts/")
        res = conn.getresponse()        
        if res.status == 200:
            data = res.read()
            responce = json.loads(data)
            newresponce = (responce['states']['м. Київ']['alertnow'])
            print(newresponce)
            with open(responcefile, 'r') as fl:
                oldresponce = json.load(fl)
            users_changed = False
            if (newresponce != oldresponce and newresponce == False):
                with open(responcefile, 'w') as fl:
                    json.dump(newresponce, fl)
                for id in list(users): 
                    try:
                        bot.send_message(id, "{} Відбій повітряної тривоги Київ".format(emojigreen))
                    except ApiTelegramException as f:
                        if f.description == "Forbidden: bot was blocked by the user":
                            print("Увага! Користувач {} заблокував бот. Видаляю з бази...".format(id))
                            users.remove(id)
                            users_changed = True
            elif (newresponce != oldresponce and newresponce == True):
                  with open(responcefile, 'w') as fl:
                      json.dump(newresponce, fl)
                  for id in list(users): 
                      try:
                          bot.send_message(id, "{} Повітряна тривога Київ".format(emojired))
                      except ApiTelegramException as f:
                          if f.description == "Forbidden: bot was blocked by the user":
                              print("Увага! Користувач {} заблокував бот. Видаляю з бази...".format(id))
                              users.remove(id)
                              users_changed = True
            if users_changed:
                with open(userdata, 'w') as fl2:
                    json.dump(users, fl2)
        else:
            bot.send_message(msg.chat.id, "На сервері сталася помилка HTTP: {}".format(res.status))            
    except http.client.HTTPException as e:
        bot.send_message(msg.chat.id, "На сервері сталася помилка {}".format(e))
    except socket.timeout as t:
        bot.send_message(msg.chat.id, "На сервері сталася помилка {}".format(t))
    except JSONDecodeError as g:
        bot.send_message(msg.chat.id, "На сервері сталася помилка {}".format(g))   

@bot.message_handler(commands=['check'])
def check(msg):
    conn = http.client.HTTPConnection("ubilling.net.ua")
    conn.request("GET", "/aerialalerts/")
    res = conn.getresponse()
    data = res.read()
    responce = json.loads(data)
    newresponce = (responce['states']['м. Київ']['alertnow'])
    if newresponce == False:
        bot.send_message(msg.chat.id, "{} Зараз немає повітряної тривоги Київ".format(emojigreen))
    elif newresponce == True:
        bot.send_message(msg.chat.id, "{} Зараз повітряна тривога Київ".format(emojired))

@bot.message_handler(commands=['unsub'])
def unsub(msg):
    try:
        with open(userdata, 'r') as fl:
            users = json.load(fl)
        users.remove(msg.chat.id)
        bot.send_message(msg.chat.id, "Ви успішно відписалися від сповіщень бота")
        with open(userdata, 'w') as fl:
            json.dump(users, fl)
    except ValueError:
        bot.send_message(msg.chat.id, "Ви вже відписалися від бота")

bot.polling()
