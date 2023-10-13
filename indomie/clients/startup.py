# Man - UserBot
# Copyright (c) 2022 Man-Userbot
# Credits: @mrismanaziz || https://github.com/mrismanaziz
#
# This file is a part of < https://github.com/mrismanaziz/Man-Userbot/ >
# t.me/SharingUserbot & t.me/Lunatic0de

import sys

from telethon.utils import get_peer_id

from indomie import BOT_TOKEN
from indomie import BOT_VER as version
from indomie import (
    DEFAULT,
    DEVS,
    LOGS,
    LOOP,
    MIE2,
    MIE3,
    MIE4,
    MIE5,
    STRING2,
    STRING3,
    STRING4,
    STRING5,
    STRING,
    memek,
    bot,
    call_py,
    tgbot,
)
from indomie.modules.gcast import GCAST_BLACKLIST as GBL

EOL = "EOL\nIndomieUserBot v{}, Copyright © 2021-2022 Indomie• <https://github.com/indomiegorengsatu>"
MSG_BLACKLIST = "MAKANYA GA USAH BERTINGKAH GOBLOK, USERBOT {} GUA MATIIN NAJIS BANGET DIPAKE BOCAH KONTOL KEK LU."


async def memek_client(client):
    client.me = await client.get_me()
    client.uid = get_peer_id(client.me)


def multimemek():
    if 1447438514 not in DEVS:
        LOGS.warning(EOL.format(version))
        sys.exit(1)
    if -1001473548283 not in GBL:
        LOGS.warning(EOL.format(version))
        sys.exit(1)
    if 1447438514 not in DEFAULT:
        LOGS.warning(EOL.format(version))
        sys.exit(1)
    failed = 0
    if STRING:
        try:
            bot.start()
            call_py.start()
            LOOP.run_until_complete(memek_client(bot))
            user = bot.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(
                f"STRING detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——"
            )
            if user.id in memek:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(str(e))

    if STRING2:
        try:
            MIE2.start()
            LOOP.run_until_complete(man_client(MIE2))
            user = MIE2.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(
                f"STRING2 detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——")
            if user.id in memek:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(str(e))

    if STRING3:
        try:
            MIE3.start()
            LOOP.run_until_complete(memek_client(MIE3))
            user = MIE3.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(
                f"STRING3 detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——")
            if user.id in memek:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(str(e))

    if STRING4:
        try:
            MIE4.start()
            LOOP.run_until_complete(memek_client(MIE4))
            user = MIE4.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(
                f"STRING4 detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——")
            if user.id in memek:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(str(e))

    if STRING5:
        try:
            MIE5.start()
            LOOP.run_until_complete(memek_client(MIE5))
            user = MIE5.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(
                f"STRING5 detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——")
            if user.id in memek:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(str(e))

    if BOT_TOKEN:
        try:
            user = tgbot.get_me()
            name = user.first_name
            uname = user.username
            LOGS.info(
                f"BOT_TOKEN detected!\n┌ First Name: {name}\n└ Username: @{uname}\n——"
            )
        except Exception as e:
            LOGS.info(str(e))

    if not STRING:
        failed += 1
    if not STRING2:
        failed += 1
    if not STRING3:
        failed += 1
    if not STRING4:
        failed += 1
    if not STRING5:
        failed += 1
    return failed
