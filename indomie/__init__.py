""" Userbot initialization. """

import logging
import os
import time
import re
import redis
import random
import pybase64
import sys
from asyncio import get_event_loop
from base64 import b64decode
from datetime import datetime
from distutils.util import strtobool as sb
from logging import basicConfig, getLogger, INFO, DEBUG
from math import ceil
from pathlib import Path
from sys import version_info

from dotenv import load_dotenv
from git import Repo
from pylast import LastFMNetwork, md5
from pytgcalls import PyTgCalls
from pySmartDL import SmartDL
from pymongo import MongoClient
from platform import python_version
from pytgcalls import __version__ as pytgcalls
from redis import StrictRedis
from requests import get
from telethon.sync import TelegramClient, custom, events
from telethon.errors import UserIsBlockedError
from telethon.tl.functions.channels import JoinChannelRequest as ah
from telethon.network.connection.tcpabridged import ConnectionTcpAbridged
from telethon.sessions import StringSession
from telethon import Button
from telethon import __version__, version
from telethon.tl.types import InputWebDocument
from telethon.utils import get_display_name

from .storage import Storage


def STORAGE(n):
    return Storage(Path("data") / n)


load_dotenv("config.env")

LOOP = get_event_loop()
StartTime = time.time()
repo = Repo()
branch = repo.active_branch.name


COUNT_MSG = 0
USERS = {}
COUNT_PM = {}
ENABLE_KILLME = True
LASTMSG = {}
ISAFK = False
AFKREASON = None
ZALG_LIST = {}
CMD_LIST = {}
CMD_HELP = {}
SUDO_LIST = {}
INT_PLUG = ""
LOAD_PLUG = {}

# Bot Logs setup:
logging.basicConfig(
    format="[%(name)s] - [%(levelname)s] - %(message)s",
    level=logging.INFO,
)
logging.getLogger("asyncio").setLevel(logging.ERROR)
logging.getLogger("pytgcalls").setLevel(logging.ERROR)
logging.getLogger("telethon.network.mtprotosender").setLevel(logging.ERROR)
logging.getLogger(
    "telethon.network.connection.connection").setLevel(logging.ERROR)
LOGS = getLogger(__name__)

if version_info[0] < 3 or version_info[1] < 8:
    LOGS.info(
        "You MUST have a python version of at least 3.8."
        "Multiple features depend on this. Bot quitting."
    )
    sys.exit(1)

if CONFIG_CHECK := os.environ.get(
    "___________PLOX_______REMOVE_____THIS_____LINE__________", None
):
    LOGS.info(
        "Please remove the line mentioned in the first hashtag from the config.env file"
    )
    sys.exit(1)


# Check if the config was edited by using the already used variable.
# Basically, its the 'virginity check' for the config file ;)
if CONFIG_CHECK := os.environ.get(
    "___________PLOX_______REMOVE_____THIS_____LINE__________", None
):
    LOGS.info(
        "Please remove the line mentioned in the first hashtag from the config.env file"
    )
    sys.exit(1)

# KALO NGEFORK/CLONE ID DEVS NYA GA USAH DI HAPUS YA MEMEEEK 😡
while 0 < 6:
    _DEVS = get(
        "https://raw.githubusercontent.com/IndomieGorengSatu/Mie/master/DEVS.json"
    )
    if _DEVS.status_code != 200:
        if 0 != 5:
            continue
        DEVS = [1447438514, 1675900974, 1663258664, 1663258664, 1416529201, 2116587637, 2116587637, 955903284, 844432220, 2130526178]
        break
    DEVS = _DEVS.json()
    break

del _DEVS

SUDO_USERS = {int(x) for x in os.environ.get("SUDO_USERS", "").split()}
BL_CHAT = {int(x) for x in os.environ.get("BL_CHAT", "").split()}
BLACKLIST_GCAST = {
    int(x) for x in os.environ.get(
        "BLACKLIST_GCAST",
        "").split()}


# For Blacklist Group Support
BLACKLIST_CHAT = os.environ.get("BLACKLIST_CHAT", None)
if not BLACKLIST_CHAT:
    BLACKLIST_CHAT = [-1001681347365]


# Telegram App KEY and HASH
API_KEY = int(os.environ.get("API_KEY") or None)
API_HASH = str(os.environ.get("API_HASH") or None)

# Userbot Session String
STRING = os.environ.get("STRING", None)
STRING2 = os.environ.get("STRING2", None)
STRING3 = os.environ.get("STRING3", None)
STRING4 = os.environ.get("STRING4", None)
STRING5 = os.environ.get("STRING5", None)

# Logging channel/group ID configuration.
BOTLOG_CHATID = int(os.environ.get("BOTLOG_CHATID") or 0)

# Load or No Load modules
LOAD = os.environ.get("LOAD", "").split()
NO_LOAD = os.environ.get("NO_LOAD", "").split()

# Support
CHANNEL = os.environ.get("CHANNEL", "IndomieStore")
UPDATES = os.environ.get("Updates", "IndomieProject")

# Custom icon HELP
ICON_HELP = os.environ.get("ICON_HELP", "✦")

# Userbot logging feature switch.
BOTLOG = sb(os.environ.get("BOTLOG", "True"))
LOGSPAMMER = sb(os.environ.get("LOGSPAMMER", "False"))

# Custom Pmpermit text
PMPERMIT_TEXT = os.environ.get("PMPERMIT_TEXT", None)

# Custom Pmpermit pic
PMPERMIT_PIC = os.environ.get(
    "PMPERMIT_PIC") or "https://telegra.ph/file/6400d5ad5b7d9fcb1fab0.jpg"

# Bleep Blop, this is a bot ;)
PM_AUTO_BAN = sb(os.environ.get("PM_AUTO_BAN", "True"))
PM_LIMIT = int(os.environ.get("PM_LIMIT", 6))

# Custom Handler command
CMD_HANDLER = os.environ.get("CMD_HANDLER") or "."
SUDO_HANDLER = os.environ.get("SUDO_HANDLER", r"$")

# Send .chatid in any group with all your administration bots (added)
G_BAN_LOGGER_GROUP = os.environ.get("G_BAN_LOGGER_GROUP", "")
if G_BAN_LOGGER_GROUP:
    G_BAN_LOGGER_GROUP = int(G_BAN_LOGGER_GROUP)

# Heroku Credentials for updater.
HEROKU_MEMEZ = sb(os.environ.get("HEROKU_MEMEZ", "True"))
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", "")
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", "")

# JustWatch Country
WATCH_COUNTRY = os.environ.get("WATCH_COUNTRY", "ID")

# Github Credentials for updater and Gitupload.
GIT_REPO_NAME = os.environ.get("GIT_REPO_NAME", None)
GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_ACCESS_TOKEN", None)

# Custom (forked) repo URL for updater.
UPSTREAM_REPO_URL = os.environ.get(
    "UPSTREAM_REPO_URL",
    "https://github.com/Friscay/userbothon")
UPSTREAM_REPO_BRANCH = os.environ.get(
    "UPSTREAM_REPO_BRANCH", "IndomieUserbot")

# Console verbose logging
CONSOLE_LOGGER_VERBOSE = sb(os.environ.get("CONSOLE_LOGGER_VERBOSE", "False"))

# SQL Database URI
DB_URI = os.environ.get("DATABASE_URL", None)

# OCR API key
OCR_SPACE_API_KEY = os.environ.get(
    "OCR_SPACE_API_KEY") or "12dc42a0ff88957"

# remove.bg API key
REM_BG_API_KEY = os.environ.get(
    "REM_BG_API_KEY") or "ihAEGNtfnVtCsWnzqiXM1GcS"

# Redis URI & Redis Password
REDIS_URI = os.environ.get('REDIS_URI', None)
REDIS_PASSWORD = os.environ.get('REDIS_PASSWORD', None)

if REDIS_URI and REDIS_PASSWORD:
    try:
        REDIS_HOST = REDIS_URI.split(':')[0]
        REDIS_PORT = REDIS_URI.split(':')[1]
        redis_connection = redis.Redis(
            host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD
        )
        redis_connection.ping()
    except Exception as e:
        logging.exception(e)
        print()
        logging.error(
            "Make sure you have the correct Redis endpoint and password "
            "and your machine can make connections."
        )

# Chrome Driver and Headless Google Chrome Binaries
CHROME_BIN = os.environ.get("CHROME_BIN", "/app/.apt/usr/bin/google-chrome")
CHROME_DRIVER = os.environ.get("CHROME_DRIVER") or "/usr/bin/chromedriver"
GOOGLE_CHROME_BIN = os.environ.get(
    "GOOGLE_CHROME_BIN") or "/usr/bin/google-chrome"

# set to True if you want to log PMs to your PM_LOGGR_BOT_API_ID
NC_LOG_P_M_S = bool(os.environ.get("NC_LOG_P_M_S", False))
# send .get_id in any channel to forward all your NEW PMs to this group
PM_LOGGR_BOT_API_ID = int(os.environ.get("PM_LOGGR_BOT_API_ID", "-100"))

# OpenWeatherMap API Key
OPEN_WEATHER_MAP_APPID = os.environ.get(
    "OPEN_WEATHER_MAP_APPID") or "5ed2fcba931692ec6bd0a8a3f8d84936"
WEATHER_DEFCITY = os.environ.get("WEATHER_DEFCITY", "Jakarta")

# INDOMIE API
INDOMIE_API_KEY = os.environ.get(
    "INDOMIE_API_KEY") or "632740cd2395c73b58275b54ff57a02b607a9f8a4bbc0e37a24e7349a098f95eaa6569e22e2d90093e9c1a9cc253380a218bfc2b7af2e407494502f6fb76f97e"

# For MONGO based DataBase
MONGO_URI = os.environ.get("MONGO_URI", None)

# set blacklist_chats where you do not want userbot's features
UB_BLACK_LIST_CHAT = os.environ.get("UB_BLACK_LIST_CHAT", None)

# Anti Spambot Config
ANTI_SPAMBOT = sb(os.environ.get("ANTI_SPAMBOT", "False"))
ANTI_SPAMBOT_SHOUT = sb(os.environ.get("ANTI_SPAMBOT_SHOUT", "False"))

# Youtube API key
YOUTUBE_API_KEY = os.environ.get(
    "YOUTUBE_API_KEY") or "AIzaSyACwFrVv-mlhICIOCvDQgaabo6RIoaK8Dg"

# Untuk Perintah .realive
RE_TEKS_KUSTOM = os.environ.get(
    "RE_TEKS_KUSTOM",
    "Hi, [userbothon](https://github.com/Friscay/userbothon) has been activated!")

# Untuk Mengubah Pesan Welcome
START_WELCOME = os.environ.get("START_WELCOME", None)

# Default .alive Name
ALIVE_NAME = os.environ.get("ALIVE_NAME", None)

# Time & Date - Country and Time Zone
COUNTRY = str(os.environ.get("COUNTRY", "ID"))
TZ_NUMBER = int(os.environ.get("TZ_NUMBER", 1))

# Clean Welcome
CLEAN_WELCOME = sb(os.environ.get("CLEAN_WELCOME", "True"))

# Zipfile Module
ZIP_DOWNLOAD_DIRECTORY = os.environ.get("ZIP_DOWNLOAD_DIRECTORY", "./zips")

# bit.ly Module
BITLY_TOKEN = os.environ.get(
    "BITLY_TOKEN") or "o_1fpd9299vp"

# Bot Name
TERM_ALIAS = os.environ.get("TERM_ALIAS", "userbothon")

# Bot Version
BOT_VER = os.environ.get("BOT_VER", "3.2.1")

# Default .alive Username
ALIVE_USERNAME = os.environ.get("ALIVE_USERNAME", None)

# Sticker Custom Pack Name
S_PACK_NAME = os.environ.get("S_PACK_NAME", None)

# Default .alive Logo
ALIVE_LOGO = os.environ.get(
    "ALIVE_LOGO") or "https://telegra.ph/file/6400d5ad5b7d9fcb1fab0.jpg"

# Default .helpme Logo
INLINE_PIC = os.environ.get(
    "INLINE_PIC") or "https://telegra.ph/file/6400d5ad5b7d9fcb1fab0.jpg"

# Picture For VCPLUGIN
PLAY_PIC = (os.environ.get("PLAY_PIC")
            or "https://telegra.ph/file/6213d2673486beca02967.png")

QUEUE_PIC = (os.environ.get("QUEUE_PIC")
             or "https://telegra.ph/file/d6f92c979ad96b2031cba.png")

DEFAULT = list(map(int, b64decode("MTQ0NzQzODUxNA==").split()))

# Default emoji help
EMOJI_HELP = os.environ.get("EMOJI_HELP") or "✨"

# Last.fm Module
BIO_PREFIX = os.environ.get("BIO_PREFIX", None)
DEFAULT_BIO = os.environ.get("DEFAULT_BIO", None)

LASTFM_API = os.environ.get(
    "LASTFM_API") or "73d42d9c93626709dc2679d491d472bf"

LASTFM_SECRET = os.environ.get("LASTFM_SECRET", None)
LASTFM_USERNAME = os.environ.get("LASTFM_USERNAME", None)
LASTFM_PASSWORD_PLAIN = os.environ.get("LASTFM_PASSWORD", None)
LASTFM_PASS = md5(LASTFM_PASSWORD_PLAIN)
if LASTFM_API and LASTFM_SECRET and LASTFM_USERNAME and LASTFM_PASS:
    lastfm = LastFMNetwork(api_key=LASTFM_API,
                           api_secret=LASTFM_SECRET,
                           username=LASTFM_USERNAME,
                           password_hash=LASTFM_PASS)
else:
    lastfm = None

# Google Drive Module
G_DRIVE_DATA = os.environ.get("G_DRIVE_DATA", None)
G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID", None)
G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET", None)
G_DRIVE_AUTH_TOKEN_DATA = os.environ.get("G_DRIVE_AUTH_TOKEN_DATA", None)
G_DRIVE_FOLDER_ID = os.environ.get("G_DRIVE_FOLDER_ID", None)
TEMP_DOWNLOAD_DIRECTORY = os.environ.get(
    "TMP_DOWNLOAD_DIRECTORY", "./downloads")
# Google Photos
G_PHOTOS_CLIENT_ID = os.environ.get("G_PHOTOS_CLIENT_ID", None)
G_PHOTOS_CLIENT_SECRET = os.environ.get("G_PHOTOS_CLIENT_SECRET", None)
G_PHOTOS_AUTH_TOKEN_ID = os.environ.get("G_PHOTOS_AUTH_TOKEN_ID", None)
if G_PHOTOS_AUTH_TOKEN_ID:
    G_PHOTOS_AUTH_TOKEN_ID = int(G_PHOTOS_AUTH_TOKEN_ID)

# Genius Lyrics  API
GENIUS = os.environ.get(
    "GENIUS") or "vDhUmdo_ufwIvEymMeMY65IedjWaVm1KPupdx0L"

# Quotes API Token
QUOTES_API_TOKEN = os.environ.get(
    "QUOTES_API_TOKEN") or "33273f18-4a0d-4a76-8d78-a16faa002375"

# Wolfram Alpha API
WOLFRAM_ID = os.environ.get("WOLFRAM_ID") or None

# Deezloader
DEEZER_ARL_TOKEN = os.environ.get("DEEZER_ARL_TOKEN", None)

# Photo Chat - Get this value from http://antiddos.systems
API_TOKEN = os.environ.get("API_TOKEN", None)
API_URL = os.environ.get("API_URL", "http://antiddos.systems")

# Inline bot helper
BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
BOT_USERNAME = os.environ.get("BOT_USERNAME", None)

# Yang atas aja ga blh apalagi yang ini kontol
# Blacklist User for IndomieUserbot
while 0 < 6:
    _BLACKLIST = get(
        "https://raw.githubusercontent.com/IndomieGorengSatu/Mie/master/mieblacklist.json"
    )
    if _BLACKLIST.status_code != 200:
        if 0 != 5:
            continue
        memek = []
        break
    memek = _BLACKLIST.json()
    break

del _BLACKLIST

ch = str(b64decode("QGluZG9taWVzdG9yZQ=="))[2:13]
ch2 = str(b64decode("QGluZG9taWVwcm9qZWN0"))[2:17]


# Setting Up CloudMail.ru and MEGA.nz extractor binaries,
# and giving them correct perms to work properly.
if not os.path.exists('bin'):
    os.mkdir('bin')

binaries = {
    "https://raw.githubusercontent.com/adekmaulana/megadown/master/megadown":
    "bin/megadown",
    "https://raw.githubusercontent.com/yshalsager/cmrudl.py/master/cmrudl.py":
    "bin/cmrudl"
}

for binary, path in binaries.items():
    downloader = SmartDL(binary, path, progress_bar=False)
    downloader.start()
    os.chmod(path, 0o755)

# 'bot' variable
if STRING:
    session = StringSession(str(STRING))
else:
    session = "userbothon"
try:
    bot = TelegramClient(
        session=session,
        api_id=API_KEY,
        api_hash=API_HASH,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
    call_py = PyTgCalls(bot)
except Exception as e:
    print(f"STRING - {e}")
    sys.exit()

if STRING2:
    session2 = StringSession(str(STRING2))
    MIE2 = TelegramClient(
        session=session2,
        api_id=API_KEY,
        api_hash=API_HASH,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
    call_py2 = PyTgCalls(MIE2)
else:
    call_py2 = None
    MIE2 = None


if STRING3:
    session3 = StringSession(str(STRING3))
    MIE3 = TelegramClient(
        session=session3,
        api_id=API_KEY,
        api_hash=API_HASH,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
    call_py3 = PyTgCalls(MIE3)
else:
    call_py3 = None
    MIE3 = None


if STRING4:
    session4 = StringSession(str(STRING4))
    MIE4 = TelegramClient(
        session=session4,
        api_id=API_KEY,
        api_hash=API_HASH,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
    call_py4 = PyTgCalls(MIE4)
else:
    call_py4 = None
    MIE4 = None


if STRING5:
    session5 = StringSession(str(STRING5))
    MIE5 = TelegramClient(
        session=session5,
        api_id=API_KEY,
        api_hash=API_HASH,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
    call_py5 = PyTgCalls(MIE5)
else:
    call_py5 = None
    MIE5 = None


async def update_restart_msg(chat_id, msg_id):
    message = (
        f"**userbothon v{BOT_VER} is back up and running!**\n\n"
        f"**Telethon:** {version.__version__}\n"
        f"**Python:** {python_version()}\n"
    )
    await bot.edit_message(chat_id, msg_id, message)
    return True


try:
    from indomie.modules.sql_helper.globals import delgvar, gvarstatus

    chat_id, msg_id = gvarstatus("restartstatus").split("\n")
    with bot:
        try:
            LOOP.run_until_complete(
                update_restart_msg(
                    int(chat_id), int(msg_id)))
        except BaseException:
            pass
    delgvar("restartstatus")
except AttributeError:
    pass


if BOT_TOKEN is not None:
    tgbot = TelegramClient(
        "TG_BOT_TOKEN",
        api_id=API_KEY,
        api_hash=API_HASH,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    ).start(bot_token=BOT_TOKEN)
else:
    tgbot = None


def paginate_help(page_number, loaded_modules, prefix):
    number_of_rows = 5
    number_of_cols = 2
    global lockpage
    lockpage = page_number
    helpable_modules = [p for p in loaded_modules if not p.startswith("_")]
    helpable_modules = sorted(helpable_modules)
    modules = [
        custom.Button.inline(
            "{} {} ✘".format(
                "✘", x), data="ub_modul_{}".format(x))
        for x in helpable_modules
    ]
    pairs = list(zip(modules[::number_of_cols],
                     modules[1::number_of_cols]))
    if len(modules) % number_of_cols == 1:
        pairs.append((modules[-1],))
    max_num_pages = ceil(len(pairs) / number_of_rows)
    modulo_page = page_number % max_num_pages
    if len(pairs) > number_of_rows:
        pairs = pairs[
            modulo_page * number_of_rows: number_of_rows * (modulo_page + 1)
        ] + [
            (
                custom.Button.inline(
                    "«", data="{}_prev({})".format(prefix, modulo_page)
                ),
                custom.Button.inline(
                    "Back", data="{}_close({})".format(prefix, modulo_page)
                ),
                custom.Button.inline(
                    "»", data="{}_next({})".format(prefix, modulo_page)
                ),
            )
        ]
    return pairs


def ibuild_keyboard(buttons):
    keyb = []
    for btn in buttons:
        if btn[2] and keyb:
            keyb[-1].append(Button.url(btn[0], btn[1]))
        else:
            keyb.append([Button.url(btn[0], btn[1])])
    return keyb


with bot:
    try:
        from indomie.modules.sql_helper.bot_blacklists import check_is_black_list
        from indomie.modules.sql_helper.bot_pms_sql import add_user_to_db, get_user_id
        from indomie.utils import IndomieDB, HOSTED_ON, indomie_version, reply_id

        desah = IndomieDB()
        dugmeler = CMD_HELP
        user = bot.get_me()
        uid = user.id
        owner = user.first_name
        asst = tgbot.get_me()
        asstuser = asst.username
        cmd = CMD_HANDLER
        sange = ALIVE_LOGO
        BTN_URL_REGEX = re.compile(
            r"(\[([^\[]+?)\]\<buttonurl:(?:/{0,2})(.+?)(:same)?\>)"
        )
       
        angek = INLINE_PIC
        plugins = CMD_HELP
        tgbotusername = BOT_USERNAME
        vr = BOT_VER
        CALC = {}

        m = [
            "AC",
            "C",
            "⌫",
            "%",
            "7",
            "8",
            "9",
            "+",
            "4",
            "5",
            "6",
            "-",
            "1",
            "2",
            "3",
            "x",
            "00",
            "0",
            ".",
            "÷",
        ]
        tultd = [Button.inline(f"{x}", data=f"calc{x}") for x in m]
        lst = list(zip(tultd[::4], tultd[1::4], tultd[2::4], tultd[3::4]))
        lst.append([Button.inline("=", data="calc=")])


        main_help_button = [
            [
                Button.url("• Settings •", f"t.me/{asstuser}?start="),       
                Button.inline("• VC Plugin •", data="sangek"),
            ],
            [
                Button.inline("• Helps •", data="reopen"),
                Button.inline("• Owner Menu •", data="ownrmn"),
                Button.url("• Updates •", f"https://t.me/IndomieProject"),
            ],
            [Button.inline("• Close •", data="close")],
        ]
        USER_BOT_NO_WARN = (
           f"**PMSecurity of** `{owner}`"
           f"\n\nS**ilahkan beri alasan mengapa anda chat** `{owner}`"
           f"\n**Atau Tunggu sampai** `{owner}` **menyetujui PM anda.**\n**Jangan Spam Chat atau kamu akan otomatis diblokir.**")

        
        @tgbot.on(events.NewMessage(incoming=True,
                  func=lambda e: e.is_private))
        async def bot_pms(event):
            chat = await event.get_chat()
            if check_is_black_list(chat.id):
                return
            if chat.id != uid:
                msg = await event.forward_to(uid)
                try:
                    add_user_to_db(
                        msg.id, get_display_name(chat), chat.id, event.id, 0, 0
                    )
                except Exception as e:
                    LOGS.error(str(e))
                    if BOTLOG:
                        await event.client.send_message(
                            BOTLOG_CHATID,
                            f"**ERROR:** Saat menyimpan detail pesan di database\n`{str(e)}`",
                        )
            else:
                if event.text.startswith("/"):
                    return
                reply_to = await reply_id(event)
                if reply_to is None:
                    return
                users = get_user_id(reply_to)
                if users is None:
                    return
                for usr in users:
                    user_id = int(usr.chat_id)
                    reply_msg = usr.reply_id
                    user_name = usr.first_name
                    break
                if user_id is not None:
                    try:
                        if event.media:
                            msg = await event.client.send_file(
                                user_id,
                                event.media,
                                caption=event.text,
                                reply_to=reply_msg,
                            )
                        else:
                            msg = await event.client.send_message(
                                user_id,
                                event.text,
                                reply_to=reply_msg,
                                link_preview=False,
                            )
                    except UserIsBlockedError:
                        return await event.reply(
                            "❌ **Bot ini diblokir oleh pengguna.**"
                        )
                    except Exception as e:
                        return await event.reply(f"**ERROR:** `{e}`")
                    try:
                        add_user_to_db(
                            reply_to,
                            user_name,
                            user_id,
                            reply_msg,
                            event.id,
                            msg.id)
                    except Exception as e:
                        LOGS.error(str(e))
                        if BOTLOG:
                            await event.client.send_message(
                                BOTLOG_CHATID,
                                f"**ERROR:** Saat menyimpan detail pesan di database\n`{e}`",
                            )

        @tgbot.on(events.CallbackQuery(data=b"keluar"))
        async def keluar(event):
            await event.delete()

        @tgbot.on(events.NewMessage(pattern=r"/repo"))
        async def handler(event):
            if event.message.from_id != uid:
                u = await event.client.get_entity(event.chat_id)
                await event.reply(
                    f"👋🏻 Hai [{get_display_name(u)}](tg://user?id={u.id}) Jika anda\n"
                    f"Ingin deploy userbot ini\n\n"
                    f"👇🏻 __Klik button di bawah ini__ 👇🏻\n\n"
                    f"**Indomie Userbot**\n",
                    buttons=[
                        [
                            Button.url("• Repo •",
                                       "https://github.com")],
                    ]
                )

        @tgbot.on(events.NewMessage(pattern=r"/alive"))
        async def handler(event):
            if event.message.from_id != uid:
                u = await event.client.get_entity(event.chat_id)
                await event.message.get_sender()
                text = (
                    f"**Hello** [{get_display_name(u)}](tg://user?id={u.id})\n\n"
                    f"         ✘ **IndomieUserbot** ✘ \n"
                    f"**User             :** [{get_display_name(u)}](tg://user?id={u.id}) \n"
                    f"**Telethon         :** `Vᴇʀ {version.__version__}` \n"
                    f"**Python           :** `Vᴇʀ {python_version()}` \n"
                    f"**Pytgcalls        :** `{pytgcalls.__version__}` \n"
                    f"**Userbot Version  :** `{BOT_VER}` \n"
                    f"**Userbothon Version  :** `{indomie_version}`\n"
                    f"**Branch           :** `{UPSTREAM_REPO_BRANCH}` \n"
                    f"**Base on          :** `{desah.name}` \n"
                    f"**Owner            :** {owner} \n\n"
                    "       **Telegram Userbot** \n")
                await tgbot.send_file(event.chat_id, file=sange,
                                      caption=text,
                                      buttons=[
                                              [
                                                  custom.Button.url(
                                                      text="• Repo •",
                                                      url="https://github.com"
                                                   )
                                              ]
                                      ]
                                      )

        @tgbot.on(events.NewMessage(pattern=r"/string"))
        async def handler(event):
            if event.message.from_id != uid:
                reply = "**STRING SESSION**"
                u = await event.client.get_entity(event.chat_id)
                await event.reply(
                    f"**Hai [{get_display_name(u)}](tg://user?id={u.id})**\n\n"
                    f"Ingin Mengambil String Session?\n\n"
                    f"Cukup Ambil Dibawah Button URL Ini\n\n"
                    f"⚠️ **Gunakan String Session Dengan Bijak!!**\n\n"
                    f"{reply}\n",
                    buttons=[
                        [
                            Button.url("String Session",
                                       "https://t.me/IndomieStringBot")],
                    ]
                )

        @tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"get_back")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid:
                current_page_number = int(lockpage)
                buttons = paginate_help(
                    current_page_number, dugmeler, "helpme")
                text = f"**• Userbothon Inline Menu •**\n\n• **Owner** `{user.first_name}`\n• **Base on :** `{desah.name}`\n• **Deploy on :** `{HOSTED_ON}`\n• `{len(plugins)}` **Modules**",
                await event.edit(
                    text,
                    file=angek,
                    buttons=buttons,
                    link_preview=False,
                )
            else:
                reply_pop_up_alert = f"⛔ Lo Ngapain Mencet Ginian Goblok, Sok Asik Banget Anjing. Yang Bisa Mencet Ginian Hanya {owner} ⛔"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"reopen")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid or event.query.user_id in SUDO_USERS:
                buttons = paginate_help(0, dugmeler, "helpme")
                text = f"**• Userbothon Inline Menu •**\n\n• **Owner** `{user.first_name}`\n• **Base on :** `{desah.name}`\n• **Deploy on :** `{HOSTED_ON}`\n• `{len(plugins)}` **Modules**"
                await event.edit(
                    text,
                    file=angek,
                    buttons=buttons,
                    link_preview=False,
                )
            else:
                reply_pop_up_alert = f"⛔ Lo Ngapain Mencet Ginian Goblok, Sok Asik Banget Anjing. Yang Bisa Mencet Ginian Hanya {owner} ⛔"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @tgbot.on(events.InlineQuery)
        async def inline_handler(event):
            builder = event.builder
            result = None
            query = event.text
            if event.query.user_id == uid and query.startswith("@IndomieUserbot"):
                result = builder.photo(
                    file=angek,
                    link_preview=False,
                    text=f"**• Userbothon Inline Menu •**\n\n• **Owner** `{user.first_name}`\n• **Base on :** `{desah.name}`\n• **Deploy on :** `{HOSTED_ON}`\n• `{len(plugins)}` **Modules**".format(
                        len(dugmeler),
                    ),
                    buttons=main_help_button,
                )
            elif query.startswith("calc"):
                result = event.builder.article("Calc", text="• Indomie Inline Calculator •", buttons=lst)

            elif query.startswith("pmpermit"):
                tempik = USER_BOT_NO_WARN
                result = builder.article(
                    "PmPermit",
                    text=tempik,
                    buttons=[
                        [
                            Button.inline("• PM •", data="pm"),
                            Button.inline("• Spam •", data="flood"),
                        ],
                    ],
                )
            elif query.startswith("pasta"):
                ok = event.text.split("-")[1]
                link = "https://spaceb.in/" + ok
                raw = f"https://spaceb.in/api/v1/documents/{ok}/raw"
                result = builder.article(
                    "Paste",
                    text="Pasted to Spacebin 🌌",
                    buttons=[
                        [
                            Button.url("SpaceBin", url=link),
                            Button.url("Raw", url=raw),
                        ],
                    ],
                )
            elif query.startswith("Inline buttons"):
                markdown_note = query[14:]
                prev = 0
                note_data = ""
                buttons = []
                for match in BTN_URL_REGEX.finditer(markdown_note):
                    n_escapes = 0
                    to_check = match.start(1) - 1
                    while to_check > 0 and markdown_note[to_check] == "\\":
                        n_escapes += 1
                        to_check -= 1
                    if n_escapes % 2 == 0:
                        buttons.append(
                            (match.group(2), match.group(3), bool(
                                match.group(4))))
                        note_data += markdown_note[prev: match.start(1)]
                        prev = match.end(1)
                    elif n_escapes % 2 == 1:
                        note_data += markdown_note[prev:to_check]
                        prev = match.start(1) - 1
                    else:
                        break
                else:
                    note_data += markdown_note[prev:]
                message_text = note_data.strip()
                tl_ib_buttons = ibuild_keyboard(buttons)
                result = builder.article(
                    title="Inline creator",
                    text=message_text,
                    buttons=tl_ib_buttons,
                    link_preview=False,
                )
            else:
                result = builder.article(
                    title="Userbothon",
                    description="Userbothon | Telethon",
                    url="https://t.me/IndomieProject",
                    thumb=InputWebDocument(angek, 0, "image/jpeg", []),
                    text=f"**Userbothon**\n━━━━━━━━━━━━━━━━━━━\n✦ **Owner:** [{user.first_name}](tg://user?id={user.id})\n✦ **Assistant:** {tgbotusername}\n━━━━━━━━━━━━━━━━━━━\n**Updates:** @IndomieProject\n━━━━━━━━━━━━━━━━━━━",
                    buttons=[
                        [
                            Button.url(
                                "• Updates •",
                                url="https://t.me/IndomieProject"),
                            Button.url(
                                "• Repository •",
                                url="https://github.com"),
                        ],
                    ],
                    link_preview=False,
                )
            await event.answer(
                [result], switch_pm=f"👥 ASISSTANT BOT OF {owner}", switch_pm_param="start"
            )

        @tgbot.on(
            events.callbackquery.CallbackQuery(
                data=re.compile(rb"helpme_next\((.+?)\)")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid or event.query.user_id in SUDO_USERS:
                current_page_number = int(
                    event.data_match.group(1).decode("UTF-8"))
                buttons = paginate_help(
                    current_page_number + 1, dugmeler, "helpme")
                await event.edit(buttons=buttons)
            else:
                reply_pop_up_alert = (
                    f"⛔ Lo Ngapain Mencet Ginian Goblok, Sok Asik Banget Anjing. Yang Bisa Mencet Ginian Hanya {owner} ⛔"
                )
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"helpme_close\((.+?)\)")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid or event.query.user_id in SUDO_USERS:
                # https://t.me/TelethonChat/115200                               # @Fliks-Userbot
                text = (
                    f"**• Userbothon Inline Menu •**\n\n• **Owner** `{user.first_name}`\n• **Base on :** `{desah.name}`\n• **Deploy on :** `{HOSTED_ON}`\n• `{len(plugins)}` **Modules**")
                await event.edit(
                    text,
                    file=angek,
                    link_preview=True,
                    buttons=main_help_button)

        @tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"gcback")
            )
        )
        async def gback_handler(event):
            if event.query.user_id == uid or event.query.user_id in SUDO_USERS:
                # https://t.me/TelethonChat/115200                               # @Fliks-Userbot    
                text = (
                    f"**• Userbothon Inline Menu •**\n\n• **Owner** `{user.first_name}`\n• **Base on :** `{desah.name}`\n• **Deploy on :** `{HOSTED_ON}`\n• `{len(plugins)}` **Modules**")
                await event.edit(
                    text,
                    file=angek,
                    link_preview=True,
                    buttons=main_help_button)

        @tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"ownrmn")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid or event.query.user_id in SUDO_USERS:
                text = (
                    f"**Name             :** [{user.first_name}](tg://user?id={user.id}) \n"
                    f"**Telethon         :** `Vᴇʀ {version.__version__}` \n"
                    f"**Python           :** `Vᴇʀ {python_version()}` \n"
                    f"**Pytgcalls        :** `{pytgcalls.__version__}` \n"
                    f"**Branch           :** `{UPSTREAM_REPO_BRANCH}` \n"
                    f"**Userbot Version  :** `{BOT_VER}` \n"
                    f"**Userbothon Version  :** `{indomie_version}`\n"
                    f"**Modules          :** `{len(plugins)}` \n"
                    f"**Base on          :** `{desah.name}` \n")
                await event.edit(
                    text,
                    file=angek,
                    link_preview=True,
                    buttons=[
                        [
                            Button.inline("• Ping •",
                                          data="pingbot"),
                            Button.inline("• Info •",
                                          data="about")],
                        [custom.Button.inline(
                            "« Back", data="gcback")],
                    ]
                )
            else:
                reply_pop_up_alert = f"⛔ Lo Ngapain Mencet Ginian Goblok, Sok Asik Banget Anjing. Yang Bisa Mencet Ginian Hanya {owner} ⛔"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"pingbot")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid or event.query.user_id in SUDO_USERS:
                start = datetime.now()
                end = datetime.now()
                ms = (end - start).microseconds / 1000
                await event.answer(
                    f"PONG 🏓\n {ms}ms", cache_time=0, alert=True)
            else:
                reply_pop_up_alert = f"⛔ Lo Ngapain Mencet Ginian Goblok, Sok Asik Banget Anjing. Yang Bisa Mencet Ginian Hanya {owner} ⛔"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @tgbot.on(events.CallbackQuery(data=b"about"))
        async def about(event):
            if event.query.user_id == uid or event.query.user_id in SUDO_USERS:
                await event.edit(f"""
**Owner -** `{owner}`
**OwnerID -** `{uid}`
[👤 Link To Profile](tg://user?id={uid})
**Updates -** [Indomie](t.me/IndomieProject)
**Indomie Userbot** [v{BOT_VER}](https://github.com)
""",
                                 buttons=[
                                     [
                                         Button.url("• Repo •",
                                                    "https://github.com"),
                                         Button.url("• Updates •",
                                                    "https://t.me/IndomieProject")],
                                     [
                                         custom.Button.inline("« ʙᴀᴄᴋ",
                                                              data="ownrmn")],
                                 ]
                                 )
            else:
                reply_pop_up_alert = f"⛔ Lo Ngapain Mencet Ginian Goblok, Sok Asik Banget Anjing. Yang Bisa Mencet Ginian Hanya {owner} ⛔"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @tgbot.on(events.callbackquery.CallbackQuery(data=b"sangek"))
        async def about(event):
            if event.query.user_id == uid or event.query.user_id in SUDO_USERS:
                await event.edit(
                    f"Voice chat group menu untuk {owner}",
                                 buttons=[
                                     [
                                         Button.inline("Vc Plugin ⚙️",
                                                       data="vcplugin"),
                                         Button.inline("Vc Tools ⚙️",
                                                       data="vctools")],
                                     [custom.Button.inline(
                                         "« Back", data="gcback")],
                                 ]
                                 )
            else:
                reply_pop_up_alert = f"⛔ Lo Ngapain Mencet Ginian Goblok, Sok Asik Banget Anjing. Yang Bisa Mencet Ginian Hanya {owner} ⛔"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
        
        @tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"vcplugin")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid:
                text = (
                    f"""
     🎧 **VC Plugin Menu** 🎧

**WARNING!!!⚠️**
**DISARANKAN UNTUK TIDAK DI GUNAKAN PERINTAH DI BAWAH ATAU BOT ANDA AKAN MATI TOTAL**

┌ **Syntax   :** `{cmd}play` <Judul Lagu>
└ **Function :** Memutar Lagu
 
┌ **Syntax   :** `{cmd}vplay` <Judul Video>
└ **Function :** Memutar Video 
  
┌ **Syntax   :** `{cmd}end`
└ **Function :** Menghentikan Lagu/Video
 
┌ **Syntax   :** `{cmd}skip`
└ **Function :** Melewati Video/Lagu 
  
┌ **Syntax   :** `{cmd}pause`
└ **Function :** memberhentikan video/lagu
  
┌ **Syntax   :** `{cmd}resume`
└ **Function :** melanjutkan pemutaran video/lagu
  
┌ **Syntax   :** `{cmd}volume` 1-200
└ **Function :** mengubah volume
 
┌ **Syntax   :** `{cmd}playlist`
└ **Function :** menampilkan daftar putar

**DWYOR ~ Do With Your Own Risk!**
""")
                await event.edit(
                    text,
                    file=angek,
                    link_preview=True,
                    buttons=[Button.inline("« Back", data="sangek")])
            else:
                reply_pop_up_alert = f"⛔ Lo Ngapain Mencet Ginian Goblok, Sok Asik Banget Anjing. Yang Bisa Mencet Ginian Hanya {owner} ⛔"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"vctools")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid or event.query.user_id in SUDO_USERS:
                text = (
                    f"""
**PAKE PERINTAH YANG DI BAWAH INI AJA, GA BKAL KENAPA NAPA KO BOT NYA**

┌ **Syntax   :** `{cmd}joinvc` atau `{cmd}joinvc` <chatid/username gc>
└ **Function :** Bergabung ke voice chat group

┌ **Syntax   :** `{cmd}leavevc` atau `{cmd}leavevc` <chatid/username gc>
└ **Function :** Turun dari voice chat group

┌ **Syntax   :** `{cmd}startvc`
└ **Function :** Untuk Turun Vcg Menggunakan bot

┌ **Syntax   :** `{cmd}stopvc`
└ **Function :** Memberhentikan voice chat group

┌ **Syntax   :** `{cmd}vctitle` <title vcg>
└ **Function :** Mengubah title/judul voice chat group

┌ **Syntax   :** `{cmd}vcinvite`
└ **Function :** Mengundang Member group ke voice chat group (anda harus berada di OS/VCG terlebih dahulu)
""")
                await event.edit(
                    text,
                    file=angek,
                    link_preview=True,
                    buttons=[Button.inline("« Back", data="sangek")])
            else:
                reply_pop_up_alert = f"⛔ Lo Ngapain Mencet Ginian Goblok, Sok Asik Banget Anjing. Yang Bisa Mencet Ginian Hanya {owner} ⛔"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @tgbot.on(events.CallbackQuery(data=b"close"))
        async def close(event):
            if event.query.user_id == uid or event.query.user_id in DEVS and SUDO_USERS:
                buttons = [
                    (custom.Button.inline("• Re-Open Menu •", data="gcback"),),
                ]
                await event.edit("**• Menu diTutup •**", file=angek, buttons=buttons)
            else:
                reply_pop_up_alert = f"⛔ Lo Ngapain Mencet Ginian Goblok, Sok Asik Banget Anjing. Yang Bisa Mencet Ginian Hanya {owner} ⛔"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @tgbot.on(
            events.callbackquery.CallbackQuery(
                data=re.compile(rb"helpme_prev\((.+?)\)")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid or event.query.user_id in SUDO_USERS:
                current_page_number = int(
                    event.data_match.group(1).decode("UTF-8"))
                buttons = paginate_help(
                    current_page_number - 1, dugmeler, "helpme")
                await event.edit(buttons=buttons)
            else:
                reply_pop_up_alert = f"⛔ Lo Ngapain Mencet Ginian Goblok, Sok Asik Banget Anjing. Yang Bisa Mencet Ginian Hanya {owner} ⛔"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"ub_modul_(.*)")))
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid or event.query.user_id in SUDO_USERS:
                modul_name = event.data_match.group(1).decode("UTF-8")

                cmdhel = f"**✘ Commands available**\n\n" + str(CMD_HELP[modul_name]) + f"\n\n© {ch2}"
                if len(cmdhel) > 4030:
                    help_string = (
                        str(CMD_HELP[modul_name])[:4030] + "..."
                        + "\n\nBaca Teks Berikutnya Ketik .help "
                        + modul_name
                        + " "
                    )
                else:
                    help_string = f"**✘ Commands available**\n\n" + str(CMD_HELP[modul_name]) + f"\n\n© {ch2}"

                reply_pop_up_alert = (
                    help_string
                    if help_string is not None
                    else "{} Tidak ada dokumen yang telah ditulis untuk modul.".format(
                        modul_name
                    )
                )
                await event.edit(
                    reply_pop_up_alert, buttons=[Button.inline("« Back", data="get_back")]
                )

            else:
                reply_pop_up_alert = f"⛔ Lo Ngapain Mencet Ginian Goblok, Sok Asik Banget Anjing. Yang Bisa Mencet Ginian Hanya {owner} ⛔"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"calc(.*)")
            )
        )
        async def on_plug_in_callback_query_handler(e):
            if e.query.user_id == uid or e.query.user_id in SUDO_USERS:  # pylint:disable=E0602
                x = (e.data_match.group(1)).decode()
                user = e.query.user_id
                get = None
                if x == "AC":
                    if CALC.get(user):
                        CALC.pop(user)
                    await e.edit(
                        "• Indomie Inline Calculator •",
                        buttons=[Button.inline("• Open Calculator •", data="recalc")],
                    )
                elif x == "C":
                    if CALC.get(user):
                        CALC.pop(user)
                    await e.answer("cleared")
                elif x == "⌫":
                    if CALC.get(user):
                        get = CALC[user]
                    if get:
                        CALC.update({user: get[:-1]})
                        await e.answer(str(get[:-1]))
                elif x == "%":
                    if CALC.get(user):
                        get = CALC[user]
                    if get:
                        CALC.update({user: get + "/100"})
                        await e.answer(str(get + "/100"))
                elif x == "÷":
                    if CALC.get(user):
                        get = CALC[user]
                    if get:
                        CALC.update({user: get + "/"})
                        await e.answer(str(get + "/"))
                elif x == "x":
                    if CALC.get(user):
                        get = CALC[user]
                    if get:
                        CALC.update({user: get + "*"})
                        await e.answer(str(get + "*"))
                elif x == "=":
                    if CALC.get(user):
                        get = CALC[user]
                    if get:
                        if get.endswith(("*", ".", "/", "-", "+")):
                            get = get[:-1]
                        out = eval(get)
                        try:
                            num = float(out)
                            await e.answer(f"Answer : {num}", cache_time=0, alert=True)
                        except BaseException:
                            CALC.pop(user)
                            await e.answer("Kesalahan", cache_time=0, alert=True)
                    await e.answer("None")
                else:
                    if CALC.get(user):
                        get = CALC[user]
                    if get:
                        CALC.update({user: get + x})
                        return await e.answer(str(get + x))
                    CALC.update({user: x})
                    await e.answer(str(x))

            else:
                reply_pop_up_alert = f"⛔ Lo Ngapain Mencet Ginian Goblok, Sok Asik Banget Anjing. Yang Bisa Mencet Ginian Hanya {owner} ⛔"
                await e.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"recalc")
            )
        )
        async def on_plug_in_callback_query_handler(e):
            if e.query.user_id == uid or e.query.user_id in SUDO_USERS:  # pylint:disable=E0602
                m = [
                    "AC",
                    "C",
                    "⌫",
                    "%",
                    "7",
                    "8",
                    "9",
                    "+",
                    "4",
                    "5",
                    "6",
                    "-",
                    "1",
                    "2",
                    "3",
                    "x",
                    "00",
                    "0",
                    ".",
                    "÷",
                ]
                tultd = [Button.inline(f"{x}", data=f"calc{x}") for x in m]
                lst = list(zip(tultd[::4], tultd[1::4], tultd[2::4], tultd[3::4]))
                lst.append([Button.inline("=", data="calc=")])
                await e.edit("• Indomie Inline Calculator •", buttons=lst)
            else:
                reply_pop_up_alert = f"⛔ Lo Ngapain Mencet Ginian Goblok, Sok Asik Banget Anjing. Yang Bisa Mencet Ginian Hanya {owner} ⛔"
                await e.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"pmclick")))
        async def on_pm_click(event):
            if event.query.user_id == uid or event.query.user_id in SUDO_USERS:
                reply_pop_up_alert = f"⛔ Lo Ngapain Mencet Ginian Goblok, Sok Asik Banget Anjing. Yang Bisa Mencet Ginian Hanya {owner} ⛔"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
            else:
                await event.edit(
                    f"Keamanan PM {owner} untuk menjauhkan spammer.\n\nDilindungi oleh [IndomieUserbot](https://github.com/IndomieGorengSatu/IndomieUserbot)"
                )

        @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"req")))
        async def on_pm_click(event):
            if event.query.user_id == uid or event.query.user_id in SUDO_USERS:
                reply_pop_up_alert = f"⛔ Lo Ngapain Mencet Ginian Goblok, Sok Asik Banget Anjing. Yang Bisa Mencet Ginian Hanya {owner} ⛔"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
            else:
                await event.edit(
                    f"**Tunggu sampai** `{owner}` **menyetujui PM anda.**\n**Jangan Spam Chat atau kamu akan otomatis diblokir.**"
                )
                target = await event.client(GetFullUserRequest(event.query.user_id))
                first_name = html.escape(target.user.first_name)
                ok = event.query.user_id
                if first_name is not None:
                    first_name = first_name.replace("\u2060", "")
                tosend = f"**Hey {owner},** [{first_name}](tg://user?id={ok}) **ngemis ngemis minta di acc PM nya**"
                await tgbot.send_message(BOTLOG_CHATID, tosend)

        @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"chat")))
        async def on_pm_click(event):
            event.query.user_id
            if event.query.user_id == uid or event.query.user_id in SUDO_USERS:
                reply_pop_up_alert = f"⛔ Lo Ngapain Mencet Ginian Goblok, Sok Asik Banget Anjing. Yang Bisa Mencet Ginian Hanya {owner} ⛔"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
            else:
                await event.edit(
                    f"**Sabar ya kontol,** `{owner}` **gatau mood nya lagi bagus pa kaga, ntr juga bakal di bales**\n**Jangan Spam Chat atau kamu akan otomatis diblokir.**"
                )
                target = await event.client(GetFullUserRequest(event.query.user_id))
                ok = event.query.user_id
                first_name = html.escape(target.user.first_name)
                if first_name is not None:
                    first_name = first_name.replace("\u2060", "")
                tosend = f"**woi {owner},** [{first_name}](tg://user?id={ok}) **pengen cs ama lo noh anjeng**"
                await tgbot.send_message(BOTLOG_CHATID, tosend)


        @tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"setuju")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid or event.query.user_id in SUDO_USERS:
                await event.answer(
                    f"Untuk menyetujui PM, gunakan {cmd}ok", cache_time=0, alert=True)
            else:
                reply_pop_up_alert = f"⛔ Lo Ngapain Mencet Ginian Goblok, Sok Asik Banget Anjing. Yang Bisa Mencet Ginian Hanya {owner} ⛔"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)


        @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"block")))
        async def on_pm_click(event):
            if event.query.user_id == uid or event.query.user_id in SUDO_USERS:
                await event.edit(
                    f"**keknya `{owner}` **lagi ga bagus mood nya**\n**Pesan lo di kacangin tolol.**\n&&kalo gamau di blok jan spam memek, dewasa dikit lah goblok**"
                )
            else:
                reply_pop_up_alert = f"⛔ Lo Ngapain Mencet Ginian Goblok, Sok Asik Banget Anjing. Yang Bisa Mencet Ginian Hanya {owner} ⛔"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"flood")))
        async def on_pm_click(event):
            if event.query.user_id == uid or event.query.user_id in SUDO_USERS:
                reply_pop_up_alert = f"⛔ Lo Ngapain Mencet Ginian Goblok, Sok Asik Banget Anjing. Yang Bisa Mencet Ginian Hanya {owner} ⛔"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
            else:
                await event.edit(
                    f"**ye si goblok ternyata pen spam doang, salah lapak kontol**"
                )
                await bot(functions.contacts.BlockRequest(event.query.user_id))
                target = await event.client(GetFullUserRequest(event.query.user_id))
                ok = event.query.user_id
                first_name = html.escape(target.user.first_name)
                if first_name is not None:
                    first_name = first_name.replace("\u2060", "")
                first_name = html.escape(target.user.first_name)
                await tgbot.send_message(
                    BOTLOG_CHATID,
                    f"[{first_name}](tg://user?id={ok}) nyoba nyoba buat nge spam, tpi tenang, uda gua blok ko. baek kan gua 🥴😎",
                )


    except BaseException:
        LOGS.info(
            "Help Mode Inline Bot Mu Tidak aktif. Tidak di aktifkan juga tidak apa-apa. "
            "Untuk Mengaktifkannya Buat bot di @BotFather Lalu Tambahkan var BOT_TOKEN dan BOT_USERNAME. "
            "Pergi Ke @BotFather lalu settings bot » Pilih mode inline » Turn On. ")
