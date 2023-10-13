# Man - UserBot
# Copyright (c) 2022 Man-Userbot
# Credits: @mrismanaziz || https://github.com/mrismanaziz
#
# This file is a part of < https://github.com/mrismanaziz/Man-Userbot/ >
# t.me/SharingUserbot & t.me/Lunatic0de

import asyncio

from telethon.tl.functions.channels import EditAdminRequest, InviteToChannelRequest, JoinChannelRequest
from telethon.tl.types import ChatAdminRights

from indomie import BOT_VER as version
from indomie import BOTLOG_CHATID
from indomie import CMD_HANDLER as cmd
from indomie import MIE2, MIE3, MIE4, MIE5, bot, branch, tgbot
from indomie.utils import HOSTED_ON, indomie_version as jembut

MSG_ON = """
✦ **Userbothon Berhasil Di Aktifkan**
━━
➠ **Userbothon Version -** `{}` **•[{}]•**
➠ **Userbot Version -** `{}@{}`
➠ **Ketik** `{}alive` **untuk Mengecheck Bot**
━━
➠ **Powered By:** @IndomieProject
"""


async def memek_userbot_on():
    new_rights = ChatAdminRights(
        add_admins=True,
        invite_users=True,
        change_info=True,
        ban_users=True,
        delete_messages=True,
        pin_messages=True,
        manage_call=True,
    )
    try:
        if bot and tgbot:
            MemekUBOT = await tgbot.get_me()
            BOT_USERNAME = MemekUBOT.username
            await bot(InviteToChannelRequest(int(BOTLOG_CHATID), [BOT_USERNAME]))
            await asyncio.sleep(3)
    except BaseException:
        pass
    try:
        if bot and tgbot:
            MemekUBOT = await tgbot.get_me()
            BOT_USERNAME = MemekUBOT.username
            await bot(EditAdminRequest(BOTLOG_CHATID, BOT_USERNAME, new_rights, "BOT"))
            await asyncio.sleep(3)
    except BaseException:
        pass
    try:
        if bot:
            await bot(JoinChannelRequest("@IndomieProject"))
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await bot.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(jembut, HOSTED_ON, version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if MIE2:
            await MIE2(JoinChannelRequest("@IndomieProject"))
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await MIE2.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(jembut, HOSTED_ON, version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if MIE3:
            await MIE3(JoinChannelRequest("@IndomieProject"))
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await MIE3.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(jembut, HOSTED_ON, version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if MIE4:
            await MIE4(JoinChannelRequest("@IndomieProject"))
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await MIE4.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(jembut, HOSTED_ON, version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if MIE5:
            await MIE5(JoinChannelRequest("@IndomieProject"))
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await MIE5.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(jembut, HOSTED_ON, version, branch, cmd),
                )
    except BaseException:
        pass
