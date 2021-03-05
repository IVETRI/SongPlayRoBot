import threading

from pyrogram.filters import chat

from TamilBots.sql import BASE, SESSION
from sqlalchemy import Column, String, UnicodeText


class Chats(BASE):
    __tablename__ = "chats"
    chat_id = Column(String(14), primary_key=True)
    chat_name = Column(UnicodeText)

    def __init__(self, chat_id, chat_name=None):
        self.chat_id = chat_id
        self.chat_name = chat_name


Chats.__table__.create(checkfirst=True)

CHATS_LOCK = threading.RLock()
CHATS_ID = set()


def add_chat_to_db(chat_id, chat_name=None):
    with CHATS_LOCK:
        chat = SESSION.query(Chats).get(str(chat_id))
        if not chat:
            chat = Chats(str(chat_id), chat_name)
        else:
            chat.chat_name = chat_name

        SESSION.add(chat)
        SESSION.commit()
        load_chats_list()


def remove_chat_from_db(chat_id):
    with CHATS_LOCK:
        chat = SESSION.query(Chats).get(str(chat_id))
        if chat:
            SESSION.delete(chat)

        SESSION.commit()
        load_chats_list()


def load_chats_list():
    global CHAT_ID
    try:
        CHAT_ID = {int(x.chat_id) for x in SESSION.query(Chats).all()}
        return CHAT_ID
    finally:
        SESSION.close()


load_chats_list()
