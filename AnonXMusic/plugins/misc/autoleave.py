import asyncio
from datetime import datetime

from pyrogram.enums import ChatType

import config
from AnonXMusic import app
from AnonXMusic.core.call import Anony, autoend
from AnonXMusic.utils.database import get_client, is_active_chat, is_autoend


async def auto_leave(chat):
    from AnonXMusic.core.userbot import assistants

    for num in assistants:
        client = await get_client(num)
        left = 0
        if left == 1:
            return await app.send_message(chat, "Music is comming..")
        try:
            async for i in client.get_dialogs():
                if i.chat.type in [
                            ChatType.SUPERGROUP,
                            ChatType.GROUP,
                            ChatType.CHANNEL,
                        ]:
                    if i.chat.id != config.LOGGER_ID:
                        if not await is_active_chat(i.chat.id):
                            try:
                                await client.leave_chat(i.chat.id)
                                left += 1
                            except:
                                continue
        except:
            pass


#asyncio.create_task(auto_leave())


async def auto_end():
    while not await asyncio.sleep(5):
        ender = await is_autoend()
        if not ender:
            continue
        for chat_id in autoend:
            timer = autoend.get(chat_id)
            if not timer:
                continue
            if datetime.now() > timer:
                if not await is_active_chat(chat_id):
                    autoend[chat_id] = {}
                    continue
                autoend[chat_id] = {}
                try:
                    await Anony.stop_stream(chat_id)
                except:
                    continue
                try:
                    await app.send_message(
                        chat_id,
                        "» ʙᴏᴛ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ʟᴇғᴛ ᴠɪᴅᴇᴏᴄʜᴀᴛ ʙᴇᴄᴀᴜsᴇ ɴᴏ ᴏɴᴇ ᴡᴀs ʟɪsᴛᴇɴɪɴɢ ᴏɴ ᴠɪᴅᴇᴏᴄʜᴀᴛ.",
                    )
                except:
                    continue


asyncio.create_task(auto_end())
