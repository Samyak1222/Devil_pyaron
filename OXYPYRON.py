import sys
import asyncio

from os import execle, getenv, environ

from pyrogram import Client, filters, idle
from pyrogram.types import Message
from pyrogram.handlers import MessageHandler
from pyrogram.errors import FloodWait


# ------------- SESSIONS -------------

SESSION1 = getenv('SESSION1', default=None)
SESSION2 = getenv('SESSION2', default=None)
SESSION3 = getenv('SESSION3', default=None)
SESSION4 = getenv('SESSION4', default=None)
SESSION5 = getenv('SESSION5', default=None)


# ------------- CLIENTS -------------

if SESSION1:
    M1 = Client(SESSION1, api_id=25981592, api_hash="709f3c9d34d83873d3c7e76cdd75b866")
else:
    M1 = None

if SESSION2:
    M2 = Client(SESSION2, api_id=25981592, api_hash="709f3c9d34d83873d3c7e76cdd75b866")
else:
    M2 = None

if SESSION3:
    M3 = Client(SESSION3, api_id=25981592, api_hash="709f3c9d34d83873d3c7e76cdd75b866")
else:
    M3 = None

if SESSION4:
    M4 = Client(SESSION4, api_id=25981592, api_hash="709f3c9d34d83873d3c7e76cdd75b866")
else:
    M4 = None

if SESSION5:
    M5 = Client(SESSION5, api_id=25981592, api_hash="709f3c9d34d83873d3c7e76cdd75b866")
else:
    M5 = None


ONE_WORDS = ["𝗦𝗣𝗘𝗘𝗗 𝗣𝗞𝗗 𝗠𝗔𝗗𝗥𝗖𝗛𝗢𝗗 𝗞𝗘 𝗣𝗜𝗟𝗟𝗘", "Ⓐ︎Ⓤ︎Ⓚ︎Ⓐ︎Ⓣ︎Ⓛ︎Ⓔ︎Ⓢ︎Ⓢ︎", "B͜͡H͜͡A͜͡G͜͡N͜͡A͜͡ M͜͡A͜͡T͜͡ R͜͡N͜͡D͜͡I͜͡ K͜͡E͜͡ B͜͡C͜͡C͜͡H͜͡E͜͡", "🇲 🇦 🇩 🇭 🇦 🇷 🇨 🇭 🇴 🇩", "R̶N̶D̶I̶", "T͎E͎R͎I͎", "𝙼𝙰𝙸𝚈𝙰", "𝙺𝙸", "Chut", "Faad", "Dunga", "gandu", "kalap", "Baap",
           "Hu", "Kidx", "Speed", "Pakad", "mere se ldega", "bap se chud gyaa", "mera land lele", "Teri", "Maa", "Chodne",
           "Ab", "Teri", "Maa", "Chudegi", "Kutte", "Ki", "Tarah", "Beta", "Teri", "Maa", "Ke", "chut",
           "me", "apna", "land", "6inch", "andar", "tak", "dal", "dunga", "betichod", "fat", "gye",
           "raat", "lagatr", "Teri", "Maa", "Ke", "Saath", "suhagrat", "mnauanga", "teri", "Maa", "Ke", "boobs",
           "Dbaunga","uff","Teri","Maa","Kaa","Chut","fadu","randi","Kee","Pille","Teri","Maa","Kaa","bhosda",
           "Maru","randi","Kee","Chode","Teri","Maa","Kee","gand","bechunga","Randi","Kee","Pille","Teri","Maa",
           "Chodu","Suar","Kee","PILEE","speed","pkd","na","bap","se ldega","Madhrchhod","Aukat","Bana",
           "Lwde","Tera","father","Hu","Teri","behn","Kaa","chut","Maru","Madhrchhod","teri","maa","Kaa",
           "gand","Maru","Teri","Behn","Kaa","gand","Maru","Randi","Kee","Chode","Teri","bndi","Ka","chut",
           "garam","Kar","Tere","Pure","Khandan","Ko","Chodunga","bap","See","Backchode","Krega","randi",
           "Ke","Pille","gand","Me","lwda","Baap","Koo","Kabhi","Nahi","Bolna","betichod","muh","me",
           "le mera","Lwda","Jaise","uff","Kalap","gaya","Teri","Maa","sister","girlfriend","maa","din","Raat","SOte",
           "Jagte","Pelta","Huu","Lodee","jhatu","Char","Ghode","kaa","land","tere","maa","ke","gand",
           "Maa","Ka","Boobs","dabata hu", "Teri", "Maa", "Ke", "chut", "uff", "Teri", "Maa", "Ki", "Chut",
           "Faad", "Dunga", "randichod", "Tera", "Baap","Hu", "rndi", "Speed", "Pakad", "Behnchod", "Aa rndi",
           "Aaagya", "Teri", "Maa", "chudegi","ab", "Teri", "Maa", "Chudegi", "lwde", "Ki", "Tarah", "madhrchhod",
           "Teri", "Maa", "Ke", "chut", "Me", "paris", "Ka", "effile", "tower", "dal", "dumga", "kalap", "betichod",
           "madhrchhod", "Puri","Raat", "nonstop", "Teri", "Maa", "Ke", "Sath", "Sex", "krunga", "teri", "Maa", "Ke",
           "chut","lwda","uff","Teri","Maa","Kaa","gand","Maru","Randi","Kee","Pille","Teri","Maa","Kaa","Bhosda",
           "maru","gandu","Kee","Chode","Teri","Maa","Kee","chut","sell","krunGa","rand","betichod","teri","Maa",
           "Chodu","suar","Ke","aulad","Teri","Maa","Daily","Chudte","Hai","bhosdiwale","typing","sikh",
           "Le","Tera","Baap","Hu","Teri","crush","Kaa","kalap", "Gaya", "bccha", "baap se",
           "kyaa hua", "chud", "gyaa","Bhosda","fadu","nalle","Teri","girlfriend","Kaa",
           "gand","Maru","Teri","Behn","Kaa","chut","mari","randi","Ke","Chode","Teri","auntu","Ka","Boor",
           "fad","du","Tere","Pure","khandan","Ko","nanga kr Dunga","mere","Se","ldega","behnchod","jhatu",
           "Kee","aulad","gand","ke","ba","Bap","Ko","Kabhi","Nah","Bolna","Beta","Chus","Lee",
           "Maru","Loda","sale","dogla","rndiwala","chakka","Teri","Maa","ko","Gf","sbko","nanga","kar","ke",
           "kothe","Pe","nchanunga","Lwde","aaa","na","kya","betichod","Tum","Mere","Lode","Pe","Teri",
           "Maa","Ke","gand","chodu", "jake", "apni", "maa", "se", "puch", "madharchod", "behnchod ke aulad",
           "aaja", "Aaagya", "Teri", "Maa", "Chodne",
           "uff", "Teri", "Maa", "Chudegi", "lwde", "Ke", "bal", "Betimchod", "Teri", "behn", "Ko", "abhi",
           "chod", "ke", "aa", "rha", "hu", "kalap", "betichod", "chud gyaa", "uff", "teri", "maa",
           "ko", "Lagatar", "Teri", "Maa", "Ke", "Sath", "porn shoot", "Karunga", "Chud", "Gaya", "Betichod", "mere se",
           "Aukat me", "Reh le", "Warna", "maa Chod Dunga tumhari"]


async def pyrone(client: Client, message: Message):
    chat_id = message.chat.id
    ruser = None

    if message.reply_to_message:
        ruser = message.reply_to_message.message_id
    
    try:
        for word in ONE_WORDS:
            await client.send_chat_action(chat_id, "typing")
            await client.send_message(chat_id, word, reply_to_message_id=ruser)
            await asyncio.sleep(0.3)
    except FloodWait:
        pass


async def restart(_, __):
    args = [sys.executable, "pyrone.py"]
    execle(sys.executable, *args, environ)


# ADDING HANDLERS

if M1:
    M1.add_handler(MessageHandler(pyrone, filters.command(["tohr", "L0L", "AJA", "bahinchod", "START"], prefixes=None) & filters.me))
    M1.add_handler(MessageHandler(restart, filters.command(["huii", "FARAR", "STOP", "uff"], prefixes=None) & filters.me))

if M2:
    M2.add_handler(MessageHandler(pyrone, filters.command(["tohr", "L0L", "AJA", "bahinchod", "START"], prefixes=None) & filters.me))
    M2.add_handler(MessageHandler(restart, filters.command(["huii", "FARAR", "STOP", "uff"], prefixes=None) & filters.me))

if M3:
    M3.add_handler(MessageHandler(pyrone, filters.command(["tohr", "L0L", "AJA", "bahinchod", "START"], prefixes=None) & filters.me))
    M3.add_handler(MessageHandler(restart, filters.command(["huii", "FARAR", "STOP", "uff"], prefixes=None) & filters.me))

if M4:
    M4.add_handler(MessageHandler(pyrone, filters.command(["tohr", "L0L", "AJA", "bahinchod", "START"], prefixes=None) & filters.me))
    M4.add_handler(MessageHandler(restart, filters.command(["huii", "FARAR", "STOP", "uff"], prefixes=None) & filters.me))

if M5:
    M5.add_handler(MessageHandler(pyrone, filters.command(["tohr", "L0L", "AJA", "bahinchod", "START"], prefixes=None) & filters.me))
    M5.add_handler(MessageHandler(restart, filters.command(["huii", "FARAR", "STOP", "uff"], prefixes=None) & filters.me))


# STARTING CLIENTS

if M1:
    M1.start()
    M1.join_chat("BWANDARLOK")

if M2:
    M2.start()
    M2.join_chat("BWANDARLOK")

if M3:
    M3.start()
    M3.join_chat("BWANDARLOK")

if M4:
    M4.start()
    M4.join_chat("BWANDARLOK")

if M5:
    M5.start()
    M5.join_chat("BWANDARLOK")

print("𝐎𝐗𝐘𝐏𝐘𝐑𝐎𝐍 Started Successfully")

idle()


# STOPPING CLIENTS

if M1:
    M1.stop()

if M2:
    M2.stop()

if M3:
    M3.stop()

if M4:
    M4.stop()

if M5:
    M5.stop()
