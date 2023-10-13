# Copyright (c) 2021 Man-Userbot
# Created by mrismanaziz
# FROM <https://github.com/mrismanaziz/Man-Userbot>
# Recode By @IndomieGenetik
# BUATLO NI ANAK ANAK ANJING YANG KALO NGAMBIL MODUL DENGAN HAPUS CREDITS.
# WOI NGENTOT, KALO FORK KASIH BINTANG
# Yang apus kredit Lo ngentot!

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest

from indomie import CMD_HELP, CMD_HANDLER as cmd
from indomie.utils import edit_or_reply, indomie_cmd
from indomie.events import register


@indomie_cmd(pattern="limit(?: |$)(.*)")
@register(pattern=r"^\.climit(?: |$)(.*)", sudo=True)
async def _(event):
    xx = await edit_or_reply(event, "`Proses Ngecek Limit akun, Gausah panik lah ngentot!...`")
    async with event.client.conversation("@SpamBot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=178220800)
            )
            await conv.send_message("/start")
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.client(UnblockRequest("@SpamBot"))
            await conv.send_message("/start")
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        await xx.edit(f"~ {response.message.message}")


CMD_HELP.update(
    {
        "limit": f"**Plugin : **`limit`\
        \n\n  •  **Perintah :** `{cmd}limit`\
        \n  •  **Kegunaan : **__ngecek akun kena limit atau ga.__\
    "
    }
)
