from pyrogram import Client, filters
from pyrogram.types import Message
from AnonXMusic import app

@app.on_message(~filters.me & filters.command("/purge"))
async def purgefunc(client, message):
    await message.delete()
    if not message.reply_to_message:
        return await message.reply_text("Membalas pesan untuk dibersihkan.")
    chat_id = message.chat.id
    message_ids = []
    for message_id in range(
        message.reply_to_message.id,
        message.id,
    ):
        message_ids.append(message_id)
        if len(message_ids) == 100:
            await client.delete_messages(
                chat_id=chat_id,
                message_ids=message_ids,
                revoke=True,
            )
            message_ids = []
    if len(message_ids) > 0:
        await client.delete_messages(
            chat_id=chat_id,
            message_ids=message_ids,
            revoke=True,
        )
