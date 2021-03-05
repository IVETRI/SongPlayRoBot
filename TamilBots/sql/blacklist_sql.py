from pyrogram.types import Message
from sqlalchemy import Column, String, UnicodeText
from . import SESSION, BASE


class BlackList(BASE):
    __tablename__ = "blacklist"
    chat_id = Column(String(14), primary_key=True)
    reason = Column(UnicodeText)

    def __init__(self, chat_id, reason):
        self.chat_id = str(chat_id)  # ensure string
        self.reason = reason

    def __repr__(self):
        return "<BL %s>" % self.chat_id


BlackList.__table__.create(checkfirst=True)


def add_user_to_bl(chat_id: int, reason=None):
    __user = BlackList(str(chat_id), reason)
    SESSION.add(__user)
    SESSION.commit()


def check_is_black_list(message: Message):
    if message and message.from_user and message.from_user.id:
        try:
            s__ = SESSION.query(BlackList).get(str(message.from_user.id))
            return s__
        finally:
            SESSION.close()


def rem_user_from_bl(chat_id: int):
    s__ = SESSION.query(BlackList).get(str(chat_id))
    if s__:
        SESSION.delete(s__)
        SESSION.commit()
        return True
    SESSION.close()
    return False
