# -*- coding: utf-8 -*-
import os

from telethon.sync import TelegramClient, events
import os

api_id = 1372402
api_hash = 'f78f4c5d525984b7b4707188ffefeacb'
channel_id='@jok_khone'
send=True
f_id=True

client = TelegramClient('seasson_name', api_id=api_id, api_hash=api_hash)
client.start()

@client.on(events.NewMessage(pattern='/*'))
async def handler(event):
    global send
    global f_id
    if str(event.original_update.message.from_id)== '1029225297':
        if event.original_update.message.message =="خنده خونه خاموش شود":
            send=False
            await client.send_message('@Ashoj79', 'خاموش شد')
        elif event.original_update.message.message=='خنده خونه روشن شود':
            send=True
            await client.send_message('@Ashoj79', 'روشن شد')
        elif event.original_update.message.message =="ارسال خاموش شود":
            f_id=False
            await client.send_message('@Ashoj79', 'خاموش شد')
        elif event.original_update.message.message=='ارسال روشن شود':
            f_id=True
            await client.send_message('@Ashoj79', 'روشن شد')
    if send:
        msg = event.original_update.message.message
        if event.original_update.message.media is None:
            if 'http' not in event.original_update.message.message and 'https' not in event.original_update.message.message and '.com' not in event.original_update.message.message and '.ir' not in event.original_update.message.message:

                if 'More° @Mnteghe_Azad' in msg:
                    i = msg.index('More° @Mnteghe_Azad')
                    msg2=msg[:i-1]
                    msg2+="\n"+channel_id
                    await client.send_message(channel_id, msg2)
                elif '@TanzFool' in msg:
                    i = msg.index('@TanzFool')
                    msg2=msg[:i-1]
                    msg2+="\n"+channel_id
                    await client.send_message(channel_id, msg2)
                elif '@Haraam_sara' in msg:
                    i = msg.index('👅 @Haraam_sara 😎💦')
                    msg2=msg[:i-1]
                    msg2+="\n"+channel_id
                    await client.send_message(channel_id, msg2)
                elif "🇯‌🇴‌🇮‌🇳 ↯" in msg:
                    i = msg.index("🇯‌🇴‌🇮‌🇳 ↯")
                    msg2=msg[:i-1]
                    msg2+="\n"+channel_id
                    await client.send_message(channel_id, msg2)
        else:
            if 'http' not in event.original_update.message.message and 'https' not in event.original_update.message.message and '.com' not in event.original_update.message.message and '.ir' not in event.original_update.message.message:
                if "🇯‌🇴‌🇮‌🇳 ↯" in msg:
                    if f_id:
                        await client.send_message('@ashoj79', str(event.original_update.message.from_id)+' -> '+msg)
                    downloaded_file_name = await client.download_media(event.original_update.message)
                    i = msg.index("🇯‌🇴‌🇮‌🇳 ↯")
                    msg2 = msg[:i - 1]
                    msg2 += "\n" + channel_id
                    await client.send_file(entity=channel_id, file=downloaded_file_name, caption=msg2)
                    os.remove(downloaded_file_name)
                elif "╭" in msg:
                    if f_id:
                        await client.send_message('@ashoj79', str(event.original_update.message.from_id)+' -> '+msg)
                    downloaded_file_name = await client.download_media(event.original_update.message)
                    i = msg.index("╭")
                    msg2 = msg[:i - 1]
                    msg2 += "\n" + channel_id
                    await client.send_file(entity=channel_id, file=downloaded_file_name, caption=msg2)
                    os.remove(downloaded_file_name)

try:
    client.run_until_disconnected()
except:
    client.disconnect()