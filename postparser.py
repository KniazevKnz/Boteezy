from db import (db, write_post, get_posts, set_delete_flag)
import settings
from telethon.sync import TelegramClient, events
import logging
import asyncio

logging.basicConfig(filename="bot.log", level=logging.INFO)


client = TelegramClient('Anon', settings.API_ID, settings.API_HASH)
channel_name = settings.CHANNEL_NAME


@client.on(events.NewMessage(chats=channel_name))
async def new_message(client):
    await write_post(db, client.message.message, client.message.date, client.message.edit_date)


async def check(client, channel_name):
    while True:
        print('я жив')
        posts_from_db = get_posts(db)
        posts_from_channel = client.iter_messages(channel_name)
        for post1 in posts_from_db:
            post_is_here = False
            async for post2 in posts_from_channel:
                if post1['date'].strftime('%b %d %Y %H:%M:%S') == post2.date.strftime('%b %d %Y %H:%M:%S'):
                    post_is_here = True
            if post_is_here is False:
                set_delete_flag(db, post1['date'])

                print(post_is_here)
                print(post2.date.strftime('%b %d %Y %H:%M:%S'))

        await asyncio.sleep(10)

with client:
    while True:
        client.loop.run_until_complete(check(client, channel_name))


client.start()
client.run_until_disconnected()
