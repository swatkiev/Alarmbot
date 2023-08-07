# Alarmbot - бот, що сповіщає про повітряну тривогу

В якості джерела даних було використано Air Raid Alerts API (Ukraine) -> https://github.com/and3rson/raid

Для оновлення даних використовується модуль Telethon у файлі client.py -> https://github.com/LonamiWebs/Telethon

Змінна ALARM_API = "http://127.0.0.1:10101/api/states/25" - цифра 25 відповідає за м. Київ (для іншого регіону треба вказати іншу цифру)

Змінна TOKEN відповідає унікальному id Вашого телеграм бота, який можна згенерувати тут -> @BotFather

Змінні api_id та api_hash у client.py можна згенерувати тут -> https://my.telegram.org

Файл responce.data використовується для запису поточного стану тривоги (true/false)

Змінна users використовується для зберігання усіх chat_id користувачів, що підключать собі бота
