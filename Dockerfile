FROM python:3.8-alpine

RUN pip install requests && pip install pyTelegramBotAPI && pip install surrogates

WORKDIR /opt/alarmbot

COPY alarm.py /opt/alarmbot

COPY responce.data /opt/alarmbot

CMD ["python", "alarm.py"]
