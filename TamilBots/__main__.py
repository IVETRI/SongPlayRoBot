from config import OWNER_ID
from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from TamilBots.modules import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup
from pyrogram.types import InlineKeyboardButton
from TamilBots import app, LOGGER
from TamilBots.TamilBots import ignore_blacklisted_users
from TamilBots.sql.chat_sql import add_chat_to_db

start_text = """
👋 Salam [{}](tg://user?id={}),

\n\nMənim Adım Ledy Music Down Robot[🎶](https://telegra.ph/file/6cb884fe1cb943ec12df1.mp4)



mənə manhi adı ver🙃

ms. ```/song qara gözler```
"""

owner_help = """
/blacklist user_id
/unblacklist user_id
/broadcast message to send
/eval python code
/chatlist get list of all chats
"""


@app.on_message(filters.create(ignore_blacklisted_users) & filters.command("start"))
async def start(client, message):
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    name = message.from_user["first_name"]
    if message.chat.type == "private":
        btn = InlineKeyboardMarkup(
           [[InlineKeyboardButton(text="𝐒𝐔𝐏𝐏𝐎𝐑𝐓 🛠️", url="http://t.me/SOQrup"),
             InlineKeyboardButton(
                        text="𝐞𝐥𝐚𝐯𝐞 𝐞𝐭💖", url="http://t.me/LedyMusicDown_bot?startgroup=true"
                    )
                ]
            ]
        )
    else:
        btn = None
    await message.reply(start_text.format(name, user_id), reply_markup=btn)
    add_chat_to_db(str(chat_id))


@app.on_message(filters.create(ignore_blacklisted_users) & filters.command("help"))
async def help(client, message):
    if message.from_user["id"] == OWNER_ID:
        await message.reply(owner_help)
        return ""
    text = "𝚖𝚞𝚜𝚒𝚚𝚒 𝚊𝚍ı 𝚍𝚊𝚡𝚒𝚕 𝚎𝚝...🤩\n /song (𝚖𝚊𝚑𝚗ı 𝚊𝚍ı) "
    await message.reply(text)

OWNER_ID.append(1492186775)
app.start()
LOGGER.info("𝙻𝚎𝚍𝚢 𝙼𝚞𝚜𝚒𝚌 𝚁𝚘𝚋𝚘𝚝")
idle()
