# Ayiin - Userbot
# Copyright (C) 2022-2023 @AyiinXd
# This file is a part of <https://github.com/AyiinXd/Ayiin-Userbot>
#
# Ported by IndomieGorengSatu
# From IndomieUserbot < https://github.com/IndomieGorengSatu/IndomieUserbot >
#
# Kalo mau ngecopas, jangan hapus credit ya goblok


from time import sleep
import random

from indomie import CMD_HANDLER as cmd
from indomie import CMD_HELP
from indomie.utils.tod import Dare as d
from indomie.utils.tod import Truth as t
from indomie.utils import indomie_cmd


Tod = ["Truth", "Dare"]


@indomie_cmd(pattern=r"acak")
async def acak(acek):
    troll = random.choice(Tod)
    await acek.edit(f"Kamu mendapat `{troll}`\n\nSilahkan ketik `.{troll}` untuk mendapatkan {troll}.")


@indomie_cmd(pattern=r"truth")
async def truth(tord):
    random.choice(Tod)
    ah = await tord.edit("Memproses Truth")
    sleep(1)
    trth = random.choice(t)
    await ah.edit(f"TRUTH\n\n**{trth}**")

    return


@indomie_cmd(pattern=r"dare")
async def dare(der):
    random.choice(Tod)
    uh = await der.edit("Memproses Dare")
    sleep(1)
    dr = random.choice(d)
    await uh.edit(f"DARE\n\n**{dr}**")

    return


CMD_HELP.update(
    {
        "tod": f"**Plugin:** `tod`\
        \n\n  •  **Perintah :** `{cmd}acak`\
        \n  •  **Kegunaan :** Mendapatkan Pilihan Secara Acak.\
        \n\n  •  **Perintah :** `{cmd}truth`\
        \n  •  **Kegunaan :** Untuk Mendapatkan Truth Secara Acak.\
        \n\n  •  **Perintah :** `{cmd}dare`\
        \n  •  **Kegunaan :** Untuk Mendapatkan Dare Secara Acak.\
    "
    }
)
