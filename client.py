from telethon import TelegramClient, events, sync

api_id = 'PUT HERE YOUR API_ID FROM API TELEGRAM'
api_hash = 'PUT HERE YOUR API_HASH FROM API TELEGRAM'

client = TelegramClient('your_sesion_name', api_id, api_hash)
client.start()

client.send_message('@your_bot_name', '/renew')
