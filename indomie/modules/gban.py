# by:koala @mixiologist
# Lord Userbot


from indomie import CMD_HELP, DEVS
from indomie import CMD_HANDLER as cmd
from indomie.events import register
from indomie.utils import chataction, get_user_from_event, indomie_cmd

# Ported For Lord-Userbot by liualvinas/Alvin


@chataction()
async def handler(tele):
    if not tele.user_joined and not tele.user_added:
        return
    try:
        from indomie.modules.sql_helper.gmute_sql import is_gmuted

        guser = await tele.get_user()
        gmuted = is_gmuted(guser.id)
    except BaseException:
        return
    if gmuted:
        for i in gmuted:
            if i.sender == str(guser.id):
                chat = await tele.get_chat()
                admin = chat.admin_rights
                creator = chat.creator
                if admin or creator:
                    try:
                        await client.edit_permissions(
                            tele.chat_id, guser.id, view_messages=False
                        )
                        await tele.reply(
                            f"**Gbanned Spoted** \n"
                            f"**First Name :** [{guser.id}](tg://user?id={guser.id})\n"
                            f"**Action :** `Banned`"
                        )
                    except BaseException:
                        return


@indomie_cmd(pattern="gban(?: |$)(.*)")
@register(pattern=r"^\.cgban(?: |$)(.*)", sudo=True)
async def gben(userbot):
    dc = userbot
    sender = await dc.get_sender()
    me = await dc.client.get_me()
    if sender.id != me.id:
        dark = await dc.reply("`GUA GBAN LO ANJING!!!`")
    else:
        dark = await dc.edit("`Memproses Global Banned Pengguna Ini!!`")
    await dark.edit("`Global Banned Akan Segera Aktif..`")
    a = b = 0
    if userbot.is_private:
        user = userbot.chat
        reason = userbot.pattern_match.group(1)
    try:
        user, reason = await get_user_from_event(userbot)
    except BaseException:
        pass
    try:
        if not reason:
            reason = "Private"
    except BaseException:
        return await dark.edit("`Gagal Global Banned`")
    if user:
        if user.id in DEVS:
            return await dark.edit("**Lu Mau Ngapain Anjg NgeGban Tuhan Gua? Goblok Mana Bisa Lah Anjg!!!**")
        try:
            from indomie.modules.sql_helper.gmute_sql import gmute
        except BaseException:
            pass
        testuserbot = [
            d.entity.id
            for d in await userbot.client.get_dialogs()
            if (d.is_group or d.is_channel)
        ]
        for i in testuserbot:
            try:
                await userbot.client.edit_permissions(i, user, view_messages=False)
                a += 1
                await dark.edit(
                    r"\\**#GBanned_User**//"
                    f"\n\n**First Name:** [{user.first_name}](tg://user?id={user.id})\n"
                    f"**User ID:** `{user.id}`\n"
                    f"**Action:** `Global Banned`"
                )
            except BaseException:
                b += 1
    else:
        await dark.edit("**Balas ke pesan atau masukan ID atau Username pengguna.**")
    try:
        if gmute(user.id) is False:
            return await dark.edit(
                "**#Already_GBanned**\n\nUser Already Exists in My Gban List.**"
            )

    except BaseException:
        pass
    return await dark.edit(
        r"\\**#GBanned_User**//"
        f"\n\n**First Name:** [{user.first_name}](tg://user?id={user.id})\n"
        f"**User ID:** `{user.id}`\n"
        f"**Action:** `Global Banned by {me.first_name}`"
    )


@indomie_cmd(pattern=r"ungban(?: |$)(.*)")
@register(pattern=r"^\.cungban(?: |$)(.*)", sudo=True)
async def gunben(userbot):
    dc = userbot
    sender = await dc.get_sender()
    me = await dc.client.get_me()
    if sender.id != me.id:
        dark = await dc.reply("`Yah di Gban...bentar gua bukain dulu`")
    else:
        dark = await dc.edit("`Ungbanning....`")
    await dark.edit("`Membatalkan Perintah Global Banned, Pengguna Ini Akan Dapat Bergabung Ke Grup Anda`")
    a = b = 0
    if userbot.is_private:
        user = userbot.chat
        reason = userbot.pattern_match.group(1)
    try:
        user, reason = await get_user_from_event(userbot)
    except BaseException:
        pass
    try:
        if not reason:
            reason = "Private"
    except BaseException:
        return await dark.edit("`Gagal Global Banned`")
    if user:
        if user.id in DEVS:
            return await dark.edit(
                "**Nge Gban Aja Kgk Bisa Apalagi Lu Mau Nge Ungban Goblok!!!**"
            )
        if user.id in blacklistman:
            return await dark.edit(
                "**Gagal ungbanned, Karna pengguna tersebut ada di dalam daftar blacklist**"
            )
        try:
            from indomie.modules.sql_helper.gmute_sql import ungmute
        except BaseException:
            pass
        testuserbot = [
            d.entity.id
            for d in await userbot.client.get_dialogs()
            if (d.is_group or d.is_channel)
        ]
        for i in testuserbot:
            try:
                await userbot.client.edit_permissions(i, user, send_messages=True)
                a += 1
                await dark.edit("`Membatalkan Global Banned...`")
            except BaseException:
                b += 1
    else:
        await dark.edit("**Balas ke pesan atau masukan ID atau Username pengguna**")
    try:
        if ungmute(user.id) is False:
            return await dark.edit("**Error! Pengguna Tidak Ada Di Dalam Daftar Global Banned.**")
    except BaseException:
        pass
    return await dark.edit(
        r"\\**#UnGbanned_User**//"
        f"\n\n**First Name:** [{user.first_name}](tg://user?id={user.id})\n"
        f"**User ID:** `{user.id}`\n"
        f"**Action:** `UnGBanned by {me.first_name}`"
    )


CMD_HELP.update({"gban": f"𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}gban` <username/balas ke pesan>"
                 "\n↳: Melakukan Banned Secara Global Ke Semua Grup Dimana Anda Sebagai Admin"
                 f"\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}ungban` <username/balas ke pesan>"
                 "\n↳ : Membatalkan Global Banned Ke Semua Grup Dimana Anda Sebagai Admin"})
