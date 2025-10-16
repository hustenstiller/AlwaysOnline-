# -*- coding: utf-8 -*-

import logging
from telethon import TelegramClient
from data import *

logging.basicConfig(level=logging.INFO)

if api_id == '' or api_hash == '':
    logging.fatal("You must assign a API before using this script! 在登录前你必须给定ID和HASH @ data.py")

client = TelegramClient('session_file', api_id, api_hash)

async def init_client():
    logging.info("Trying to Login to Telegram... 正在尝试登录...")
    await client.start(password=globals().get('password', None))
    return client
