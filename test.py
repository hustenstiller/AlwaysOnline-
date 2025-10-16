from telethon.sync import TelegramClient 
from telethon.sessions import StringSession
api_id = input('Enter API ID: ') 
api_hash = input('Enter API HASH: ') 
with TelegramClient(StringSession(), api_id, api_hash) as client: print(client.session.save())