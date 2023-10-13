from sqlalchemy import Column, Numeric, UnicodeText
from indomie.modules.sql_helper import SESSION, BASE


class IndomieAI(BASE):
    __tablename__ = "indomie_ai"
    user_id = Column(Numeric, primary_key=True)
    chat_id = Column(Numeric, primary_key=True)
    session_id = Column(UnicodeText)
    session_expires = Column(Numeric)

    def __init__(
        self,
        user_id,
        chat_id,
        session_id,
        session_expires
    ):
        self.user_id = user_id
        self.chat_id = chat_id
        self.session_id = session_id
        self.session_expires = session_expires


IndomieAI.__table__.create(checkfirst=True)


def get_s(user_id, chat_id):
    try:
        return SESSION.query(IndomieAI).get((user_id, chat_id))
    except BaseException:
        return None
    finally:
        SESSION.close()


def get_all_s():
    try:
        return SESSION.query(IndomieAI).all()
    except BaseException:
        return None
    finally:
        SESSION.close()


def add_s(
    user_id,
    chat_id,
    session_id,
    session_expires
):
    adder = SESSION.query(IndomieAI).get((user_id, chat_id))
    if adder:
        adder.session_id = session_id
        adder.session_expires = session_expires
    else:
        adder = IndomieAI(
            user_id,
            chat_id,
            session_id,
            session_expires
        )
    SESSION.add(adder)
    SESSION.commit()


def remove_s(
    user_id,
    chat_id
):
    note = SESSION.query(IndomieAI).get((user_id, chat_id))
    if note:
        SESSION.delete(note)
        SESSION.commit()
