# Alarmbot - бот, що сповіщає про повітряну тривогу

Виконайте послідовно команди, знаходячись в директорії з Dockerfile: "docker build -t alarmbot ." і "docker run --name alarmbot --restart="always" -d alarmbot"

В якості джерела даних було використано -> http://ubilling.net.ua/aerialalerts/

Для оновлення даних використовується модуль Telethon у файлі client.py -> https://github.com/LonamiWebs/Telethon

Для роботи з запитами до телеграму використовуються модулі http.client та telebot

Змінна TOKEN відповідає унікальному id Вашого телеграм бота, який можна згенерувати тут -> @BotFather

Змінні api_id та api_hash у client.py можна згенерувати тут -> https://my.telegram.org

Файл responce.data використовується для запису поточного стану тривоги (true/false)

Змінна users використовується для зберігання усіх chat_id користувачів, що підключать собі бота
