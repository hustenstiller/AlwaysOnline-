# -*- coding: utf-8 -*-

import logging
import asyncio
from login import client
from telethon.tl.functions.account import UpdateStatusRequest
from data import delay

async def main():
    if await client.is_user_authorized():
        logging.info("You are now AlwaysOnline™, Yah!")
        while True:
            await client(UpdateStatusRequest(offline=False))
            await asyncio.sleep(delay)
            logging.debug("Sleep for %s seconds", delay)
    else:
        logging.fatal("Login Fails, please retry... 失败，请重试！")

if __name__ == "__main__":
    asyncio.run(main())
