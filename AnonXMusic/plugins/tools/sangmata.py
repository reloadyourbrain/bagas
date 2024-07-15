import asyncio
import random

from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.raw.functions.messages import DeleteHistory

from AnonXMusic import userbot as us, app
from AnonXMusic.core.userbot import assistants




@app.on_message(filters.command("sg"))
async def sg(client: Client, message: Message):
    if len(message.text.split()) < 1 and not message.reply_to_message:
        return await message.reply("sg username/id/reply")
    if message.reply_to_message:
        args = message.reply_to_message.from_user.id
    else:
        args = message.text.split()[1]
    lol = await message.reply("<code>Processing...</code>")
    if args:
        try:
            user = await client.get_users(f"{args}")
        except Exception:
            return await lol.edit("<code>Please specify a valid user!</code>")
    bo = ["sangmata_bot", "sangmata_beta_bot"]
    sg = random.choice(bo)
    if 1 in assistants:
      ubot = us.one
    if 2 in assistants:
      ubot = us.two
    if 3 in assistants:
      ubot = us.three
    if 4 in assistants:
      ubot = us.four
    if 5 in assistants:
      ubot = us.five
    try:
        a = await ubot.send_message(sg, f"{user.id}")
        await a.delete()
    except Exception as e:
        return await lol.edit(e)
    await asyncio.sleep(1)
    names = ""
    usernames = ""
    async for stalk in ubot.search_messages(a.chat.id):
        if stalk.text == None:
            continue
        if not stalk:
            await message.reply("botnya ngambek")
        elif stalk:
            text = stalk.text.split("\n", 1)[1]
            try:
                name = text.split("Usernames", 1)[0]
            except:
                name = text
            try:
                username = text.split("Usernames", 1)[1]
            except:
                try:
                    username = stalk.text.split("Usernames", 1)[1]
                except:
                    continue
            names += f"{name}"
            usernames += f"{username}"
    await message.reply(f"Names:\n{names}")
    await message.reply(f"Usernames:\n{usernames}")
    user_info = await ubot.resolve_peer(sg)
    await ubot.invoke(DeleteHistory(peer=user_info, max_id=0, revoke=True))
    await lol.delete()
