FROM python:3.9-alpine

RUN pip install python_http_client pyTelegramBotAPI surrogates

WORKDIR /opt/alarmbot/

COPY alarm.py responce.data users.data /opt/alarmbot/

CMD ["python", "alarm.py"]
