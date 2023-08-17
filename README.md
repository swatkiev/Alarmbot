# Alarmbot - бот, що сповіщає про повітряну тривогу

Виконайте послідовно команди, знаходячись в директорії з Dockerfile: "docker build -t alarmbot ." і "docker run --name alarmbot --restart="always" -d alarmbot"

Також замість копіювання файлів у образ можна запустити докер контейнер з підтримкою volumes: 

в такому випадку у "Dockerfile" треба прибрати рядок з командою "COPY", а файли "alarm.py" "responce.data" "users.data" перенести в каталог "data" і виконати команду:

docker run --name alarmbot -v ./data:/opt/alarmbot --restart="always" -d alarmbot

Це дасть можливість вносити нових користувачів до "users.data" або змінювати код у "alarm.py" одразу з гостьової ОС

В якості джерела даних було використано -> http://ubilling.net.ua/aerialalerts/

Для оновлення даних (кожні 10 сек) використовується модуль Telethon у файлі client.py -> https://github.com/LonamiWebs/Telethon

Файл client.py необхідно додати на виконання у crontab з такими параметрами -> * * * * * /path/to/client.py

Для роботи з запитами до телеграму використовуються модулі http.client та telebot

Змінна TOKEN відповідає унікальному id Вашого телеграм бота, який можна згенерувати тут -> @BotFather

Змінні api_id та api_hash у client.py можна згенерувати тут -> https://my.telegram.org

Файл responce.data використовується для запису поточного стану тривоги (true/false)

Файл users.data використовується для зберігання усіх chat_id користувачів, що підключать собі бота
