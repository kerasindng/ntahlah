# © Man-Userbot <Github.com/mrismanaziz/Man-Userbot>
import heroku3
import io
import re
import time
from datetime import datetime
from os import remove

from telegraph import Telegraph, upload_file
from telethon import Button, custom, events
from telethon.tl import types
from telethon.tl.types import MessageMediaWebPage
from telethon.utils import get_display_name, pack_bot_file_id

from indomie import (
    BOT_USERNAME,
    BOTLOG_CHATID,
    CMD_HANDLER,
    HEROKU_API_KEY,
    HEROKU_APP_NAME,
    SUDO_HANDLER,
    StartTime,
    tgbot,
    user,
)
from indomie.modules.sql_helper.bot_blacklists import check_is_black_list
from indomie.modules.sql_helper.bot_starters import (
    add_starter_to_db,
    get_all_starters,
    get_starter_details,
)
from indomie.modules.sql_helper.globals import gvarstatus
from indomie.utils import _format, asst_cmd, callback, reply_id

from indomie.modules.ping import get_readable_time

botusername = BOT_USERNAME

OWNER = user.first_name
OWNER_ID = user.id
telegraph = Telegraph()
r = telegraph.create_account(short_name="telegraph")
auth_url = r["auth_url"]


heroku_api = "https://api.heroku.com"
if HEROKU_APP_NAME is not None and HEROKU_API_KEY is not None:
    Heroku = heroku3.from_key(HEROKU_API_KEY)
    app = Heroku.app(HEROKU_APP_NAME)
    heroku_var = app.config()
else:
    app = None


async def setit(event, name, value):
    try:
        heroku_var[name] = value
    except BaseException:
        return await event.edit("**Maaf Gagal Menyimpan Karena ERROR**")


def get_back_button(name):
    return [Button.inline("« ʙᴀᴄᴋ", data=f"{name}")]


def text_to_url(event):
    if isinstance(event.media, MessageMediaWebPage):
        webpage = event.media.webpage
        if not isinstance(
                webpage,
                types.WebPageEmpty) and webpage.type in ["photo"]:
            return webpage.display_url
    return event.text


async def check_bot_started_users(user, event):
    if user.id == OWNER_ID:
        return
    check = get_starter_details(user.id)
    if check is None:
        start_date = str(datetime.now().strftime("%B %d, %Y"))
        notification = f"🔮 **#BOT_START**\n**First Name:** {_format.mentionuser(user.first_name , user.id)} \
                \n**User ID: **`{user.id}`\
                \n**Action: **Telah Memulai saya."
    else:
        start_date = check.date
        notification = f"🔮 **#BOT_RESTART**\n**First Name:** {_format.mentionuser(user.first_name , user.id)}\
                \n**ID: **`{user.id}`\
                \n**Action: **Telah Me-Restart saya"

    try:
        add_starter_to_db(
            user.id,
            get_display_name(user),
            start_date,
            user.username)
    except Exception as e:
        LOGS.error(str(e))
    if BOTLOG_CHATID:
        await event.client.send_message(BOTLOG_CHATID, notification, buttons=[[Button.url("Profile", f"tg://openmessage?user_id={user.id}")]])


@callback(data=re.compile(b"pmclose"))
async def pmclose(event):
    if event.query.user_id == OWNER_ID:
        await event.delete()


@callback(data=re.compile(b"kontol"))
async def pmclose(event):
    await event.delete()


@callback(data=re.compile(b"cmdhndlr"))
async def cmdhndlr(event):
    await event.delete()
    pru = event.sender_id
    var = "CMD_HANDLER"
    name = "CMD Handler/ Trigger"
    async with event.client.conversation(pru) as conv:
        await conv.send_message(
            f"**Kirim Simbol yang anda inginkan sebagai Handler/Pemicu untuk menggunakan bot\nPenangan Anda Saat Ini adalah** [ `{CMD_HANDLER}` ]\n\nGunakan /cancel untuk membatalkan.",
        )
        response = conv.wait_event(events.NewMessage(chats=pru))
        response = await response
        themssg = response.message.message
        if themssg == "/cancel":
            await conv.send_message(
                "Membatalkan Proses Settings VAR!",
                buttons=get_back_button("hndlrmenu"),
            )
        elif len(themssg) > 1:
            await conv.send_message(
                "Handler yang anda masukan salah harap gunakan simbol",
                buttons=get_back_button("hndlrmenu"),
            )
        elif themssg.startswith(("/", "#", "@")):
            await conv.send_message(
                "Simbol ini tidak dapat digunakan sebagai handler, Silahkan Gunakan Simbol lain",
                buttons=get_back_button("hndlrmenu"),
            )
        else:
            await setit(event, var, themssg)
            await conv.send_message(
                f"{name} **Berhasil diganti Menjadi** `{themssg}`",
                buttons=get_back_button("hndlrmenu"),
            )


@callback(data=re.compile(b"apiset"))
async def apiset(event):
    await event.edit(
        "**Silahkan Pilih VAR yang ingin anda Setting**",
        buttons=[
            [Button.inline("ᴍᴜʟᴛɪ ᴄʟɪᴇɴᴛ", data="multiclient")],
            [
                Button.inline("ᴀʟɪᴠᴇ", data="alivemenu"),
                Button.inline("ɪɴʟɪɴᴇ", data="inlinemenu"),
            ],
            [
                Button.inline("ʜᴀɴᴅʟᴇʀ", data="hndlrmenu"),
                Button.inline("ᴘᴍᴘᴇʀᴍɪᴛ", data="pmpermitmenu"),
            ],
            [Button.inline("ʙᴀᴄᴋ", data="settings")],
        ],
    )


@callback(data=re.compile(b"hndlrmenu"))
async def hndlrmenu(event):
    await event.edit(
        "**Silahkan Pilih VAR yang ingin anda Setting**",
        buttons=[
            [
                Button.inline("ᴄᴍᴅ ʜᴀɴᴅʟᴇʀ", data="cmdhndlr"),
                Button.inline("sᴜᴅᴏ ʜᴀɴᴅʟᴇʀ", data="sdhndlr"),
            ],
            [Button.inline("ʙᴀᴄᴋ", data="apiset")],
        ],
    )


@callback(data=re.compile(b"alivemenu"))
async def alivemenu(event):
    await event.edit(
        "**Silahkan Pilih VAR yang ingin anda Setting**",
        buttons=[
            [
                Button.inline("ᴀʟɪᴠᴇ ʟᴏɢᴏ", data="alvlogo"),
            ],
            [
                Button.inline("ʙᴀᴄᴋ", data="apiset"),
            ],
        ],
    )


@callback(data=re.compile(b"inlinemenu"))
async def inlinemenu(event):
    await event.edit(
        "**Silahkan Pilih VAR yang ingin anda Setting**",
        buttons=[
            [
                Button.inline("ɪɴʟɪɴᴇ ᴘɪᴄ", data="inpics"),
            ],
            [Button.inline("ʙᴀᴄᴋ", data="apiset")],
        ],
    )


@callback(data=re.compile(b"pmbot"))
async def pmbot(event):
    await event.delete()
    if event.query.user_id == OWNER_ID:
        await tgbot.send_message(
            event.chat_id,
            message=f"""**Perintah di Bot ini adalah:**\n
**NOTE: Perintah ini hanya berfungsi di {botusername}**\n
 • **Command : **/uinfo <reply ke pesan>
 • **Function : **Untuk Mencari Info Pengirim Pesan.\n
 • **Command : **/ban <alasan> atau /ban <username/userid> <alasan>
 • **Function : **Untuk Membanned Pengguna dari BOT.(Gunakan alasan saat ban)\n
 • **Command : **/unban <alasan> atau /unban <username/userid>
 • **Function : **Membuka Banned pengguna dari bot, agar bisa mengirim pesan lagi dibot.
 • **NOTE : **Untuk memeriksa daftar pengguna yang dibanned Ketik `.bblist`\n
 • **Command : **/broadcast
 • **Function : **Balas ke pesan untuk diBroadcast ke setiap pengguna yang memulai bot Anda. Untuk mendapatkan daftar pengguna Ketik `.botuser`\n
 • **NOTE : ** Jika pengguna menghentikan/memblokir bot maka dia akan dihapus dari database Anda yaitu dia akan dihapus dari daftar bot_starters
""",
            buttons=[
                [
                    custom.Button.inline(
                        "« ʙᴀᴄᴋ",
                        data="settings",
                    )
                ],
            ],
        )


@callback(data=re.compile(b"users"))
async def users(event):
    await event.delete()
    if event.query.user_id == OWNER_ID:
        total_users = get_all_starters()
        msg = "Daftar Pengguna Di Bot \n\n"
        for user in total_users:
            msg += f"• First Name: {user.first_name}\nUser ID: {user.user_id}\nTanggal: {user.date}\n\n"
        with io.BytesIO(str.encode(msg)) as fileuser:
            fileuser.name = "listusers.txt"
            await tgbot.send_file(
                event.chat_id,
                fileuser,
                force_document=True,
                thumb="indomie/resources/logo.jpg",
                caption="**Total Pengguna Di Bot anda.**",
                allow_cache=False,
                buttons=[
                    (
                        Button.inline("« ʙᴀᴄᴋ", data="settings"),
                        Button.inline("ᴄʟᴏsᴇ", data="pmclose"),
                    )
                ],
            )


@callback(data=re.compile(b"settings"))
async def botsettings(event):
    await event.delete()
    if event.query.user_id == OWNER_ID:
        await tgbot.send_message(
            event.chat_id,
            message=f"**Hallo [{OWNER}](tg://user?id={OWNER_ID}) Adakah Yang Bisa Saya Bantu?**",
            buttons=[
                (
                    Button.inline("sᴇᴛᴛɪɴɢs", data="apiset"),
                    Button.inline("ᴘᴍʙᴏᴛ", data="pmbot"),
                ),
                (
                    Button.inline("ᴘɪɴɢ", data="pingbot"),
                    Button.inline("ᴜᴘᴛɪᴍᴇ", data="uptimebot"),
                ),
                (
                    Button.inline("ʙʀᴏᴀᴅᴄᴀsᴛ", data="bcast"),
                    Button.inline("sᴛᴀᴛs", data="stat"),
                ),
                (Button.inline("ᴄʟᴏsᴇ", data="pmclose"),),
            ],
        )


@callback(data=re.compile(b"pmpermitmenu"))
async def alivemenu(event):
    await event.edit(
        "**Silahkan Pilih VAR yang ingin anda Setting**",
        buttons=[
            [
                Button.inline("ᴘᴍᴘᴇʀᴍɪᴛ ᴏɴ", data="pmon"),
                Button.inline("ᴘᴍᴘᴇʀᴍɪᴛ ᴏᴏꜰ", data="pmoff"),
            ],
            [Button.inline("« ʙᴀᴄᴋ", data="apiset")],
        ],
    )


@callback(data=re.compile(b"multiclient"))
async def menuclient(event):
    await event.edit(
        "**Silahkan Pilih VAR yang ingin anda Setting**",
        buttons=[
            [
                Button.inline("sᴛʀɪɴɢ", data="strone"),
            ],
            [
                Button.inline("sᴛʀɪɴɢ 2", data="strtwo"),
                Button.inline("sᴛʀɪɴɢ 3", data="strtri"),
            ],
            [
                Button.inline("sᴛʀɪɴɢ 4", data="strfor"),
                Button.inline("sᴛʀɪɴɢ 5", data="strfiv"),
            ],
            [Button.inline("« ʙᴀᴄᴋ", data="apiset")],
        ],
    )


@callback(data=re.compile(b"strone"))
async def strone(event):
    await event.delete()
    pru = event.sender_id
    var = "STRING"
    async with event.client.conversation(pru) as conv:
        await conv.send_message(
            f"**Silahkan Kirimkan {var} Telethon anda dari @IndomieStringBot**\n\nGunakan /cancel untuk membatalkan."
        )
        response = conv.wait_event(events.NewMessage(chats=pru))
        response = await response
        themssg = response.message.message
        if themssg == "/cancel":
            return await conv.send_message(
                f"Membatalkan Proses Settings VAR {var}",
                buttons=get_back_button("multiclient"),
            )
        await setit(event, var, themssg)
        await conv.send_message(
            f"**{var} Berhasil diganti**\n\nSedang MeRestart Heroku untuk Menerapkan Perubahan.",
            buttons=get_back_button("multiclient"),
        )


@callback(data=re.compile(b"strtwo"))
async def strtwo(event):
    await event.delete()
    pru = event.sender_id
    var = "STRING2"
    name = "MULTI CLIENT ke 2"
    async with event.client.conversation(pru) as conv:
        await conv.send_message(
            f"**Silahkan Kirimkan {var} Telethon anda dari @IndomieStringBot**\n\nGunakan /cancel untuk membatalkan."
        )
        response = conv.wait_event(events.NewMessage(chats=pru))
        response = await response
        themssg = response.message.message
        if themssg == "/cancel":
            return await conv.send_message(
                f"Membatalkan Proses Settings VAR {name}",
                buttons=get_back_button("multiclient"),
            )
        await setit(event, var, themssg)
        await conv.send_message(
            f"**{name} Berhasil disettings**\n\nSedang MeRestart Heroku untuk Menerapkan Perubahan.",
            buttons=get_back_button("multiclient"),
        )


@callback(data=re.compile(b"strtri"))
async def strtri(event):
    await event.delete()
    pru = event.sender_id
    var = "STRING3"
    name = "MULTI CLIENT ke 3"
    async with event.client.conversation(pru) as conv:
        await conv.send_message(
            f"**Silahkan Kirimkan {var} Telethon anda dari @IndomieStringBot**\n\nGunakan /cancel untuk membatalkan."
        )
        response = conv.wait_event(events.NewMessage(chats=pru))
        response = await response
        themssg = response.message.message
        if themssg == "/cancel":
            return await conv.send_message(
                f"Membatalkan Proses Settings VAR {name}",
                buttons=get_back_button("multiclient"),
            )
        await setit(event, var, themssg)
        await conv.send_message(
            f"**{name} Berhasil disettings**\n\nSedang MeRestart Heroku untuk Menerapkan Perubahan.",
            buttons=get_back_button("multiclient"),
        )


@callback(data=re.compile(b"strfor"))
async def strfor(event):
    await event.delete()
    pru = event.sender_id
    var = "STRING4"
    name = "MULTI CLIENT ke 4"
    async with event.client.conversation(pru) as conv:
        await conv.send_message(
            f"**Silahkan Kirimkan {var} Telethon anda dari @IndomieStringBot**\n\nGunakan /cancel untuk membatalkan."
        )
        response = conv.wait_event(events.NewMessage(chats=pru))
        response = await response
        themssg = response.message.message
        if themssg == "/cancel":
            return await conv.send_message(
                f"Membatalkan Proses Settings VAR {name}",
                buttons=get_back_button("multiclient"),
            )
        await setit(event, var, themssg)
        await conv.send_message(
            f"**{name} Berhasil disettings**\n\nSedang MeRestart Heroku untuk Menerapkan Perubahan.",
            buttons=get_back_button("multiclient"),
        )


@callback(data=re.compile(b"strfiv"))
async def strfiv(event):
    await event.delete()
    pru = event.sender_id
    var = "STRING5"
    name = "MULTI CLIENT ke 5"
    async with event.client.conversation(pru) as conv:
        await conv.send_message(
            f"**Silahkan Kirimkan {var} Telethon anda dari @IndomieStringBot**\n\nGunakan /cancel untuk membatalkan."
        )
        response = conv.wait_event(events.NewMessage(chats=pru))
        response = await response
        themssg = response.message.message
        if themssg == "/cancel":
            return await conv.send_message(
                f"Membatalkan Proses Settings VAR {name}",
                buttons=get_back_button("multiclient"),
            )
        await setit(event, var, themssg)
        await conv.send_message(
            f"**{name} Berhasil disettings**\n\nSedang MeRestart Heroku untuk Menerapkan Perubahan.",
            buttons=get_back_button("multiclient"),
        )


@callback(data=re.compile(b"pmon"))
async def pmonn(event):
    var = "PM_AUTO_BAN"
    await setit(event, var, "True")
    await event.edit(
        "Done! PMPermit telah diaktifkan!!",
        buttons=get_back_button("settings"),
    )


@callback(data=re.compile(b"pmoff"))
async def pmofff(event):
    var = "PM_AUTO_BAN"
    await setit(event, var, "False")
    await event.edit(
        "Done! PMPermit telah dimatikan!!",
        buttons=get_back_button("settings"),
    )


@callback(data=re.compile(b"sdhndlr"))
async def sdhndlr(event):
    await event.delete()
    pru = event.sender_id
    var = "SUDO_HANDLER"
    name = "SUDO Handler/ Trigger"
    async with event.client.conversation(pru) as conv:
        await conv.send_message(
            f"**Kirim Simbol yang anda inginkan sebagai HANDLER untuk pengguna sudo bot anda\nSUDO_HANDLER anda Saat Ini adalah** [ `{SUDO_HANDLER}` ]\n\nGunakan /cancel untuk membatalkan.",
        )
        response = conv.wait_event(events.NewMessage(chats=pru))
        response = await response
        themssg = response.message.message
        if themssg == "/cancel":
            await conv.send_message(
                "Membatalkan Proses Settings VAR!",
                buttons=get_back_button("hndlrmenu"),
            )
        elif len(themssg) > 1:
            await conv.send_message(
                "Handler yang anda masukan salah harap gunakan simbol",
                buttons=get_back_button("hndlrmenu"),
            )
        elif themssg.startswith(("/", "#", "@")):
            await conv.send_message(
                "Simbol ini tidak dapat digunakan sebagai handler, Silahkan Gunakan Simbol lain",
                buttons=get_back_button("hndlrmenu"),
            )
        else:
            await setit(event, var, themssg)
            await conv.send_message(
                f"{name} **Berhasil diganti Menjadi** `{themssg}`",
                buttons=get_back_button("hndlrmenu"),
            )


@callback(data=re.compile(b"inpics"))
async def inpics(event):
    await event.delete()
    pru = event.sender_id
    var = "INLINE_PIC"
    async with event.client.conversation(pru) as conv:
        await conv.send_message(
            "**Silahkan Kirimkan Link Telegraph Untuk var INLINE_PIC anda**\n\nGunakan /cancel untuk membatalkan."
        )
        response = conv.wait_event(events.NewMessage(chats=pru))
        response = await response
        themssg = response.message.message
        if themssg == "/cancel":
            return await conv.send_message(
                "Membatalkan Proses Settings VAR!",
                buttons=get_back_button("inlinemenu"),
            )
        await setit(event, var, themssg)
        await conv.send_message(
            f"**INLINE_PIC Berhasil di Ganti Menjadi** `{themssg}`\n\nSedang MeRestart Heroku untuk Menerapkan Perubahan.",
            buttons=get_back_button("inlinemenu"),
        )


@callback(data=re.compile(b"inmoji"))
async def inmoji(event):
    await event.delete()
    pru = event.sender_id
    var = "INLINE_EMOJI"
    async with event.client.conversation(pru) as conv:
        await conv.send_message(
            "**Silahkan Kirimkan Teks Untuk var INLINE_EMOJI anda**\n\nGunakan /cancel untuk membatalkan."
        )
        response = conv.wait_event(events.NewMessage(chats=pru))
        response = await response
        themssg = response.message.message
        if themssg == "/cancel":
            return await conv.send_message(
                "Membatalkan Proses Settings VAR!",
                buttons=get_back_button("inlinemenu"),
            )
        await setit(event, var, themssg)
        await conv.send_message(
            f"**INLINE_EMOJI Berhasil di Ganti Menjadi** `{themssg}`\n\nSedang MeRestart Heroku untuk Menerapkan Perubahan.",
            buttons=get_back_button("inlinemenu"),
        )


@callback(data=re.compile(b"alvmoji"))
async def alvmoji(event):
    await event.delete()
    pru = event.sender_id
    var = "ALIVE_EMOJI"
    async with event.client.conversation(pru) as conv:
        await conv.send_message(
            "**Silahkan Kirimkan Emoji Untuk var ALIVE_EMOJI anda**\n\nGunakan /cancel untuk membatalkan."
        )
        response = conv.wait_event(events.NewMessage(chats=pru))
        response = await response
        themssg = response.message.message
        if themssg == "/cancel":
            return await conv.send_message(
                "Membatalkan Proses Settings VAR!",
                buttons=get_back_button("alivemenu"),
            )
        await setit(event, var, themssg)
        await conv.send_message(
            f"**ALIVE_EMOJI Berhasil di Ganti Menjadi** `{themssg}`\n\nSedang MeRestart Heroku untuk Menerapkan Perubahan.",
            buttons=get_back_button("alivemenu"),
        )


@callback(data=re.compile(b"alvlogo"))
async def alvlogo(event):
    await event.delete()
    pru = event.sender_id
    var = "ALIVE_LOGO"
    async with event.client.conversation(pru) as conv:
        await conv.send_message(
            f"**Silahkan Kirimkan Foto Untuk var {var} anda**\n\nGunakan /cancel untuk membatalkan."
        )
        response = await conv.get_response()
        try:
            themssg = response.message.message
            if themssg == "/cancel":
                return await conv.send_message(
                    f"Membatalkan Proses Settings VAR {var}",
                    buttons=get_back_button("alivemenu"),
                )
        except BaseException:
            pass
        if (
            not (response.text).startswith("/")
            and response.text != ""
            and (not response.media or isinstance(response.media, MessageMediaWebPage))
        ):
            url = text_to_url(response)
        elif response.sticker:
            url = response.file.id
        else:
            media = await event.client.download_media(response, "alvpc")
            try:
                x = upload_file(media)
                url = f"https://telegra.ph/{x[0]}"
                remove(media)
            except BaseException:
                return await conv.send_message(
                    f"**Maaf Gagal Mengganti Foto Untuk {var}**",
                    buttons=get_back_button("alivemenu"),
                )
        await setit(event, var, url)
        await conv.send_message(
            f"**{var} Berhasil di Ganti Tod**\n\nSabar Ya Babi Ini Sedang MeRestart Heroku untuk Menerapkan Perubahan.",
            buttons=get_back_button("alivemenu"),
        )


@callback(data=re.compile(b"bcast"))
async def bdcast(event):
    ok = get_all_starters()
    await event.edit(f"• Siaran ke {len(ok)} pengguna.")
    async with event.client.conversation(OWNER_ID) as conv:
        await conv.send_message(
            "Masukkan pesan siaran Anda.\nGunakan /cancel untuk menghentikan siaran.",
        )
        response = await conv.get_response()
        if response.message == "/cancel":
            return await conv.send_message("Cancelled!!")
        success = 0
        fail = 0
        await conv.send_message(f"Memulai siaran ke {len(ok)} pengguna...")
        start = datetime.now()
        for i in ok:
            try:
                await event.client.send_message(int(i.user_id), response)
                success += 1
            except BaseException:
                fail += 1
        end = datetime.now()
        time_taken = (end - start).seconds
        await conv.send_message(
            f"""
**Siaran selesai dalam {time_taken} detik.**
Total Pengguna di Bot - {len(ok)}
**Dikirim ke** : `{success} users.`
**Gagal untuk** : `{fail} user(s).`""",
        )


@callback(data=re.compile(b"stat"))
async def botstat(event):
    orang = len(get_all_starters())
    msg = """Indomie Assistant - Stats
Jumlah Pengguna - {}""".format(
        orang,
    )
    await event.answer(msg, cache_time=0, alert=True)


@asst_cmd(pattern="^/start?([\\s]+)?$", func=lambda e: e.is_private)
async def bot_start(event):
    chat = await event.get_chat()
    user = await event.client.get_me()
    if check_is_black_list(chat.id):
        return
    reply_to = await reply_id(event)
    mention = f"[{chat.first_name}](tg://user?id={chat.id})"
    my_mention = f"[{user.first_name}](tg://user?id={user.id})"
    first = chat.first_name
    last = chat.last_name
    fullname = f"{first} {last}" if last else first
    username = f"@{chat.username}" if chat.username else mention
    userid = chat.id
    my_first = user.first_name
    my_last = user.last_name
    my_fullname = f"{my_first} {my_last}" if my_last else my_first
    my_username = f"@{user.username}" if user.username else my_mention
    if chat.id != OWNER_ID:
        customstrmsg = gvarstatus("START_TEXT") or None
        if customstrmsg is not None:
            start_msg = customstrmsg.format(
                mention=mention,
                first=first,
                last=last,
                fullname=fullname,
                username=username,
                userid=userid,
                my_first=my_first,
                my_last=my_last,
                my_fullname=my_fullname,
                my_username=my_username,
                my_mention=my_mention,
            )
        else:
            start_msg = f"**👋 Hai {mention}\
                        \n\n**Saya adalah {my_mention} \
                        \n**Anda dapat Menghubungi  [{OWNER}](tg://user?id={OWNER_ID}) dari sini. \
                        \n**Jangan Melakukan Spam Atau anda akan di blokir** \
                        \n\n**Powered by**: [IndomieProject](https://t.me/IndomieProject)**"
            buttons = [
                (
                    Button.inline("ɪɴꜰᴏ", data="infor"),
                )
            ]
    else:
        start_msg = f"**Hallo [{OWNER}](tg://user?id={OWNER_ID}) Adakah Yang Bisa Saya Bantu?**"
        buttons = [
            (
                Button.inline("sᴇᴛᴛɪɴɢs", data="apiset"),
                Button.inline("ᴘᴍʙᴏᴛ", data="pmbot"),
            ),
            (
                Button.inline("ᴘɪɴɢ", data="pingbot"),
                Button.inline("ᴜᴘᴛɪᴍᴇ", data="uptimebot"),
            ),
            (
                Button.inline("ʙʀᴏᴀᴅᴄᴀsᴛ", data="bcast"),
                Button.inline("sᴛᴀᴛs", data="stat"),
            ),
            (Button.inline("ᴄʟᴏsᴇ", data="pmclose"),),
        ]
    try:
        await event.client.send_message(
            chat.id,
            start_msg,
            link_preview=False,
            buttons=buttons,
            reply_to=reply_to,
        )
    except Exception as e:
        if BOTLOG_CHATID:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"**ERROR:** Saat Pengguna memulai Bot anda.\n`{e}`",
            )

    else:
        await check_bot_started_users(chat, event)


@callback(data=re.compile(b"uptimebot"))
async def _(event):
    uptime = await get_readable_time((time.time() - StartTime))
    pin = f"⏱ ᴜᴘᴛɪᴍᴇ = {uptime}"
    await event.answer(pin, cache_time=0, alert=True)


@callback(data=re.compile(b"pingbot"))
async def _(event):
    start = datetime.now()
    end = datetime.now()
    ms = (end - start).microseconds
    pin = f"🏓 ᴘɪɴɢ = {ms} microseconds"
    await event.answer(pin, cache_time=0, alert=True)


@asst_cmd(pattern="^/id")
async def _(event):
    if event.reply_to_msg_id:
        await event.get_input_chat()
        r_msg = await event.get_reply_message()
        if r_msg.media:
            bot_api_file_id = pack_bot_file_id(r_msg.media)
            await tgbot.send_message(
                event.chat_id,
                "**👥 Chat ID:** `{}`\n**🙋‍♂️ From User ID:** `{}`\n**💎 Bot API File ID:** `{}`".format(
                    str(event.chat_id), str(r_msg.sender_id), bot_api_file_id
                ),
            )
        else:
            await tgbot.send_message(
                event.chat_id,
                "**👥 Chat ID:** `{}`\n**🙋‍♂️ From User ID:** `{}`".format(
                    str(event.chat_id), str(r_msg.sender_id)
                ),
            )
    else:
        await tgbot.send_message(
            event.chat_id, f"**👥 Chat ID:** `{str(event.chat_id)}`"
        )


@asst_cmd(pattern="^/ping$")
async def _(event):
    start = datetime.now()
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await tgbot.send_message(event.chat_id, "🏓**Pong!**\n`%sms`" % duration)


@callback(data=re.compile(b"infor"))
async def infor(event):
    await event.edit(
                f"**Owner** - {OWNER} \
                \n**ID** - {OWNER_ID} \
                \n**Profile** - [Link](tg://user?id={OWNER_ID}) \
                \n**Store** - [Link](t.me/IndomieStore) \
                \n**Repo** - [Github](github.com/IndomieGorengSatu) \
                \n\n**Powerd By [IndomieProject](https://t.me/IndomieProject)**",
        buttons=[
            [
                custom.Button.inline(
                    "ᴄʟᴏꜱᴇ",
                    data="kontol",
                )
            ],
        ],
    )
