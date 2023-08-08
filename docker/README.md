# Alarmbot - бот, що сповіщає про повітряну тривогу

Для запуску бота у докер контейнері було модифіковано docker-compose.yml файл, оригінал якого знаходиться тут ->  Air Raid Alerts API (Ukraine) -> https://github.com/and3rson/raid

Для повноцінної роботи бота спочатку треба склонувати https://github.com/and3rson/raid, а потім замінити файл docker-compose.yml на модифікований, а також додати папку bot, що містить файли Dockerfile, alarm.py, responce.data

Змінна ALARM_API = "http://app:10101/api/states/25" - цифра 25 відповідає за м. Київ (для іншого регіону треба вказати іншу цифру)

Змінна TOKEN відповідає унікальному id Вашого телеграм бота, який можна згенерувати тут -> @BotFather

Змінні api_id та api_hash у client.py можна згенерувати тут -> https://my.telegram.org

Файл responce.data використовується для запису поточного стану тривоги (true/false)

Змінна users використовується для зберігання усіх chat_id користувачів, що підключать собі бота
