FROM python:3.9-alpine

RUN pip install python_http_client && pip install pyTelegramBotAPI && pip install surrogates

WORKDIR /opt/alarmbot

COPY alarm.py /opt/alarmbot

COPY responce.data /opt/alarmbot

COPY users.data /opt/alarmbot

CMD ["python", "alarm.py"]
