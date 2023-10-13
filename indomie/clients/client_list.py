# Man - UserBot
# Copyright (c) 2022 Man-Userbot
# Credits: @mrismanaziz || https://github.com/mrismanaziz
#
# This file is a part of < https://github.com/mrismanaziz/Man-Userbot/ >
# t.me/SharingUserbot & t.me/Lunatic0de

from base64 import b64decode

import telethon.utils
from telethon.tl.functions.users import GetFullUserRequest


async def clients_list(SUDO_USERS, bot, MIE2, MIE3, MIE4, MIE5):
    user_ids = list(SUDO_USERS) or []
    main_id = await bot.get_me()
    user_ids.append(main_id.id)

    try:
        if MIE2 is not None:
            id2 = await MIE2.get_me()
            user_ids.append(id2.id)
    except BaseException:
        pass

    try:
        if MIE3 is not None:
            id3 = await MIE3.get_me()
            user_ids.append(id3.id)
    except BaseException:
        pass

    try:
        if MIE4 is not None:
            id4 = await MIE4.get_me()
            user_ids.append(id4.id)
    except BaseException:
        pass

    try:
        if MIE5 is not None:
            id5 = await MIE5.get_me()
            user_ids.append(id5.id)
    except BaseException:
        pass

    return user_ids


ITSME = list(map(int, b64decode("MTQ0NzQzODUxNA==").split()))


async def client_id(event, botid=None):
    if botid is not None:
        uid = await event.client(GetFullUserRequest(botid))
        OWNER_ID = uid.user.id
        MEMEK_USER = uid.user.first_name
    else:
        client = await event.client.get_me()
        uid = telethon.utils.get_peer_id(client)
        OWNER_ID = uid
        MEMEK_USER = client.first_name
    memek_mention = f"[{MEMEK_USER}](tg://user?id={OWNER_ID})"
    return OWNER_ID, MEMEK_USER, memek_mention
