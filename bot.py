import asyncio
import logging
from sys import argv
from telethon.sync import TelegramClient, events
from telethon.tl.types import ChannelParticipantsAdmins, ChatBannedRights
from telethon.tl.functions.channels import EditBannedRequest

permissions = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,

)

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

API_ID = 2184829
API_HASH = '6930b92388baabff4cb4a1d377085035'
SUDO_USERS = [1212368262, 5340517139]
BOT_TOKEN1 = "5477732634:AAEhLmX2_Yqm5WdSzoHhm1EyRrxWvw62b2U"
BOT_TOKEN2 = "5543610541:AAFfI4TE_QkCHllrEabFa1M-yIoHj9IzuCk"
BOT_TOKEN3 = "5393996186:AAE8FNQ4NOoLvpvuFPloS7b27NJtuMCNdhc"
BOT_TOKEN4 = "5439195038:AAH9818B4zjWYBFLh7lEvMjQTizZzrP-IjQ"
BOT_TOKEN5 = "5347103671:AAEPOgfs3cH-KPaAHugIqKOyrJqaPf9YBxU"

MafiaBot1 = ""
MafiaBot2 = ""
MafiaBot3 = ""
MafiaBot4 = ""
MafiaBot5 = ""

async def main():
    global MafiaBot1
    global MafiaBot2
    global MafiaBot3
    global MafiaBot4
    global MafiaBot5

if BOT_TOKEN1:
    print("Working On Bot Token 1!")
    try:
        MafiaBot1 = TelegramClient("MafiaSpamBot1", api_id=API_ID, api_hash=API_HASH).start(bot_token=BOT_TOKEN1)
        print("Bot Token 1 OK!")
        MafiaBot1.start()
    except Exception as e:
        print(e)
        pass
else:
    print("Bot Token Is'nt Available Or Invalid Bot Token")
    try:
        session_name = "MafiaSpamBot1"
        MafiaBot1 = TelegramClient(session_name, api_id=API_ID, api_hash=API_HASH).start(bot_token=BOT_TOKEN1)
        MafiaBot1.start()
    except Exception as e:
        pass

if BOT_TOKEN2:
    print("Working On Bot Token 2!")
    try:
        MafiaBot2 = TelegramClient("MafiaSpamBot2", api_id=API_ID, api_hash=API_HASH).start(bot_token=BOT_TOKEN2)
        print("Bot Token 2 OK!")
        MafiaBot2.start()
    except Exception as e:
        print(e)
        pass
else:
    print("Bot Token Is'nt Available Or Invalid Bot Token")
    try:
        session_name = "MafiaSpamBot2"
        MafiaBot2 = TelegramClient(session_name, api_id=API_ID, api_hash=API_HASH).start(bot_token=BOT_TOKEN2)
        MafiaBot2.start()
    except Exception as e:
        pass

if BOT_TOKEN3:
    print("Working On Bot Token 3!")
    try:
        print("Bot Token 3 OK!")
        MafiaBot3 = TelegramClient("MafiaSpamBot3", api_id=API_ID, api_hash=API_HASH).start(bot_token=BOT_TOKEN3)
        MafiaBot3.start()
    except Exception as e:
        print(e)
        pass
else:
    print("Bot Token Is'nt Available Or Invalid Bot Token")
    try:
        session_name = "MafiaSpamBot3"
        MafiaBot3 = TelegramClient(session_name, api_id=API_ID, api_hash=API_HASH).start(bot_token=BOT_TOKEN3)
        MafiaBot3.start()
    except Exception as e:
        pass

if BOT_TOKEN4:
    print("Working On Bot Token 4!")
    try:
        MafiaBot4 = TelegramClient("MafiaSpamBo4", api_id=API_ID, api_hash=API_HASH).start(bot_token=BOT_TOKEN4)
        print("Bot Token 4 OK!")
        MafiaBot4.start()
    except Exception as e:
        print(e)
        pass
else:
    print("Bot Token Is'nt Available Or Invalid Bot Token")
    try:
        session_name = "MafiaSpamBot4"
        MafiaBot4 = TelegramClient(session_name, api_id=API_ID, api_hash=API_HASH).start(bot_token=BOT_TOKEN4)
        MafiaBot4.start()
    except Exception as e:
        pass

if BOT_TOKEN5:
    print("Working On Bot Token 5!")
    try:
        print("Bot Token 5 OK!")
        MafiaBot5 = TelegramClient("MafiaSpamBot5", api_id=API_ID, api_hash=API_HASH).start(bot_token=BOT_TOKEN5)
        MafiaBot5.start()
    except Exception as e:
        print(e)
        pass
else:
    print("Bot Token Is'nt Available Or Invalid Bot Token")
    try:
        session_name = "MafiaSpamBot1"
        MafiaBot5 = TelegramClient(session_name, api_id=API_ID, api_hash=API_HASH).start(bot_token=BOT_TOKEN5)
        MafiaBot5.start()
    except Exception as e:
        pass

# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())

@MafiaBot1.on(events.NewMessage(incoming=True, pattern='/start'))
@MafiaBot2.on(events.NewMessage(incoming=True, pattern='/start'))
@MafiaBot3.on(events.NewMessage(incoming=True, pattern='/start'))
@MafiaBot4.on(events.NewMessage(incoming=True, pattern='/start'))
@MafiaBot5.on(events.NewMessage(incoming=True, pattern='/start'))
async def start(e):
    if e.sender_id in SUDO_USERS:
            await e.client.send_message(e.chat_id, "Working")

@MafiaBot1.on(events.NewMessage(incoming=True, pattern='omkvaii'))
@MafiaBot2.on(events.NewMessage(incoming=True, pattern='omkvaii'))
@MafiaBot3.on(events.NewMessage(incoming=True, pattern='omkvaii'))
@MafiaBot4.on(events.NewMessage(incoming=True, pattern='omkvaii'))
@MafiaBot5.on(events.NewMessage(incoming=True, pattern='omkvaii'))
async def banall(e):
    if e.sender_id in SUDO_USERS:
        try:
            noobs = await e.client.get_participants(e.chat_id, filter=ChannelParticipantsAdmins)
            cant_ban = [admin.id for admin in noobs]
            async for users in e.client.iter_participants(e.chat_id):
                if users.id not in cant_ban:
                    await e.client(EditBannedRequest(e.chat_id, users.id, permissions))
                    await asyncio.sleep(0.1)
        except Exception as e:
            print(str(e))



if len(argv) not in (1, 3, 4):
    try:
        MafiaBot1.disconnect()
    except Exception as er:
        print(er)
        pass
    try:
        MafiaBot2.disconnect()
    except Exception as er:
        print(er)
        pass
    try:
        MafiaBot3.disconnect()
    except Exception as er:
        print(er)
        pass
    try:
        MafiaBot4.disconnect()
    except Exception as er:
        print(er)
        pass
    try:
        MafiaBot5.disconnect()
    except Exception as er:
        print(er)
        pass
else:
    try:
        MafiaBot1.run_until_disconnected()
    except Exception as er:
        print(er)
        pass
    try:
        MafiaBot2.run_until_disconnected()
    except Exception as er:
        print(er)
        pass
    try:
        MafiaBot3.run_until_disconnected()
    except Exception as er:
        print(er)
        pass
    try:
        MafiaBot4.run_until_disconnected()
    except Exception as er:
        print(er)
        pass
    try:
        MafiaBot5.run_until_disconnected()
    except Exception as er:
        print(er)
        pass

