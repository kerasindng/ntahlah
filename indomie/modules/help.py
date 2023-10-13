# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#

from indomie import CHANNEL, UPDATES, ch2
from indomie import CMD_HELP, ICON_HELP
from indomie import CMD_HANDLER as cmd
from indomie.utils import edit_delete, edit_or_reply, indomie_cmd

modules = CMD_HELP


@indomie_cmd(pattern="help(?: |$)(.*)")
async def help(indomie):
    args = indomie.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await edit_or_reply(indomie, f"{CMD_HELP[args]}\n\n© {ch2}")
        else:
            await edit_delete(indomie, f"`{args}`**NGETIK YANG BENER NGENTOT!!.**")
    else:
        memek = await indomie.client.get_me()
        string = ""
        for i in CMD_HELP:
            string += "`" + str(i)
            string += f"`\t\t\t{ICON_HELP}\t\t\t"
        await edit_or_reply(
            indomie,
            f"**• List Help Userbothon •**\n\n"
            f"**• Jumlah** `{len(CMD_HELP)}` **Modules**\n"
            f"**• Bot Owner :** [{memek.first_name}](tg://user?id={memek.id})\n\n"
            "**• Help •**\n"
            f"{ICON_HELP}   {string}"
            f"\n\nChannel @{CHANNEL}"
            f"\nUpdates @{UPDATES}",
        )
        await indomie.reply(
            f"\n**Contoh Ketik** `{cmd}help ping` **Untuk Melihat Informasi Pengunaan.\nJangan Lupa Berdoa Sebelum Mencoba yahahaha...**"
        )
