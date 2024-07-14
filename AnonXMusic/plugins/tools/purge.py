from pyrogram import Client, filters
from pyrogram.types import Message
from AnonXMusic import app

@app.on_message(~filters.me & filters.command("/purge"))
async def purge(client, message):
    msg = message.reply_to_message
    send = await message.reply("Starting To Purge Messages!")
    if msg:
        itermsg = list(range(msg.id, message.id))
    else:
        await send.edit("Reply To Message To Purge!")
        return
    count = 0

    for i in itermsg:
        try:
            count = count + 1
            await client.delete_messages(
                chat_id=message.chat.id, message_ids=i, revoke=True
            )
        except FloodWait as e:
            print(e)
            await asyncio.sleep(e.x)
        except Exception as e:
            await send.edit(f"ERROR: ```\n{e}```")
            return

    await send.edit(
        f"Fast Purge Completed!\nBerhasil Menghapus {str(count)} Pesan."
    )
