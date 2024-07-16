from pyrogram import Client, filters
from pyrogram.types import Message

from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from telethon.tl.types import ChannelParticipantCreator
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.errors import UserNotParticipantError

from AnonXMusic import app
from AnonXMusic.misc import SUDOERS
from AnonXMusic.core.bot import client


async def can_delete_messages(message):
    status = False
    if message.chat.admin_rights:
        status = message.chat.admin_rights.delete_messages
    return status

async def user_is_admin(user_id: int, message):
    status = False
    if message.is_private:
        return True

    async for user in client.iter_participants(message.chat_id,
                                             filter=ChannelParticipantsAdmins):
        SUDOS = []
        for us in SUDOERS:
            a = await app.get_users(us)
            SUDOS.append(a.id)
        if user_id == user.id or user_id in SUDOS:
            status = True
            return status
    return status


async def is_user_admin(user_id: int, chat_id):
    status = False
    async for user in client.iter_participants(chat_id,
                                             filter=ChannelParticipantsAdmins):
        SUDOS = []
        for us in SUDOERS:
            a = await app.get_users(us)
            SUDOS.append(a.id)
        if user_id == user.id or user_id in SUDOS:
            status = True
            return status
    return status

@client.on(events.NewMessage(pattern="/purge"))
async def purge(event):
    if event.from_id == None:
        return

    chat = event.chat_id

    if not await user_is_admin(user_id=event.from_id, message=event):
        await event.reply("Who dis non-admin telling me what to do?")
        return

    if not await can_delete_messages(message=event):
        await event.reply("I can't delete messages here! Make sure I'm admin and can delete other user's messages.")
        return

    msg = await event.get_reply_message()
    if not msg:
        await event.reply("Reply to a message to select where to start purging from.")
        return
    msgs = []
    msg_id = msg.id
    delete_to = event.message.id - 1
    await event.client.delete_messages(chat, event.message.id)

    msgs.append(event.reply_to_msg_id)
    for m_id in range(delete_to, msg_id - 1, -1):
        msgs.append(m_id)
        if len(msgs) == 100:
            await event.client.delete_messages(chat, msgs)
            msgs = []

    await event.client.delete_messages(chat, msgs)
    text = (chat, "Purge completed.")
    await event.respond(text, parse_mode='md')
