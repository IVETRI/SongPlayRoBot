from pyrogram import Client, filters
from pyrogram.types import Message
from TamilBots.sql.blacklist_sql import check_is_black_list


async def ignore_blacklisted_users(filter, client: Client, message: Message):
    check = check_is_black_list(message)
    if check:
        return False
    else:
        return True


def get_arg(message):
    msg = message.text
    msg = msg.replace(" ", "", 1) if msg[1] == " " else msg
    split = msg[1:].replace("\n", " \n").split(" ")
    if " ".join(split[1:]).strip() == "":
        return ""
    return " ".join(split[1:])
