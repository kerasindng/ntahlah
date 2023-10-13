# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
# Copyright (C) 2021 TeamUltroid for autobot
# FROM Man-Userbot <https://github.com/mrismanaziz/Man-Userbot>
# t.me/SharingUserbot & t.me/Lunatic0de
# Credits : @mrismanaziz
# Recode by @indomiegenetik
#
""" Userbot start point """


import sys
from importlib import import_module
from platform import python_version

from pytgcalls import __version__ as pytgcalls
from telethon import version

from indomie import BOT_TOKEN
from indomie import BOT_VER as ubotversion
from indomie import BOTLOG_CHATID, LOGS, bot
from indomie.clients import memek_userbot_on, multimemek
from indomie.core.git import git
from indomie.modules import ALL_MODULES
from indomie.modules.assistant import ASST_MODULES
from indomie.utils import autobot, autopilot
from indomie.utils import IndomieDB, HOSTED_ON, autobot, autopilot, indomie_version as ngewe

try:
    aduh = IndomieDB()
    client = multimemek()
    total = 5 - client
    git()
    LOGS.info(f"Total Clients = {total} User")
except BaseException as e:
    LOGS.info(str(e), exc_info=True)
    sys.exit(1)

for module_name in ALL_MODULES:
    imported_module = import_module("indomie.modules." + module_name)

for module_name in ASST_MODULES:
    imported_module = import_module("indomie.modules.assistant." + module_name)


bot.loop.run_until_complete(memek_userbot_on())
if not BOTLOG_CHATID:
    bot.loop.run_until_complete(autopilot())
if not BOT_TOKEN:
    LOGS.info(
        "BOT_TOKEN Vars kaga di isi, otewe bikin bot di @Botfather ngeeeng..."
    )
    bot.loop.run_until_complete(autobot())
LOGS.info(f"Python Version - {python_version()}")
LOGS.info(f"Telethon Version - {version.__version__}")
LOGS.info(f"PyTgCalls Version - {pytgcalls.__version__}")
LOGS.info(f"Userbot Version - {ubotversion} •[{aduh.name}]•")
LOGS.info(f"Userbothon Version - {ngewe} •[{HOSTED_ON}]•")
LOGS.info("[ BERHASIL DIAKTIFKAN! ]")
if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
