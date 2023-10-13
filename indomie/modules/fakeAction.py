# Port By @IndomieGenetik From IndomieUserbot
# # Copyright (C) 2021 IndomieUserbot
from indomie.events import register
from indomie import CMD_HELP
from indomie import CMD_HANDLER as cmd
import asyncio


@register(outgoing=True, pattern="^.ftyping(?: |$)(.*)")
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await event.edit("`Incorrect Format`")
    await event.edit(f"`Memulai Pengetikan Palsu Selama {t} sec.`")
    async with event.client.action(event.chat_id, "typing"):
        await asyncio.sleep(t)


@register(outgoing=True, pattern="^.faudio(?: |$)(.*)")
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await event.edit("`Incorrect Format`")
    await event.edit(f"`Memulai merekam audio palsu Selama {t} sec.`")
    async with event.client.action(event.chat_id, "record-audio"):
        await asyncio.sleep(t)


@register(outgoing=True, pattern="^.fvideo(?: |$)(.*)")
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await event.edit("`Incorrect Format`")
    await event.edit(f"`Memulai merekam video palsu selama {t} sec.`")
    async with event.client.action(event.chat_id, "record-video"):
        await asyncio.sleep(t)


@register(outgoing=True, pattern="^.fgame(?: |$)(.*)")
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await event.edit("`Incorrect Format`")
    await event.edit(f"`Memulai Bermain Game Palsu Selama {t} sec.`")
    async with event.client.action(event.chat_id, "game"):
        await asyncio.sleep(t)


@register(outgoing=True, pattern="^.fround(?: |$)(.*)")
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await event.edit("`Masukan jumlah detik yang benar`")
    await event.edit(f"`Memulai merekam video message palsu Selama {t} sec.`")
    await asyncio.sleep(3)
    await event.delete()
    async with event.client.action(event.chat_id, "record-round"):
        await asyncio.sleep(t)


@register(outgoing=True, pattern="^.fphoto(?: |$)(.*)")
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await event.edit("`Masukan jumlah detik yang benar`")
    await event.edit(f"`Memulai Mengirim Photo Palsu Selama` {t} sec.`")
    await asyncio.sleep(3)
    await event.delete()
    async with event.client.action(event.chat_id, "photo"):
        await asyncio.sleep(t)


@register(outgoing=True, pattern="^.fdocument(?: |$)(.*)")
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await event.edit("`Masukan jumlah detik yang benar`")
    await event.edit(f"`Memulai Mengirim Document Palsu Selama` {t} sec.`")
    await asyncio.sleep(3)
    await event.delete()
    async with event.client.action(event.chat_id, "document"):
        await asyncio.sleep(t)


@register(outgoing=True, pattern="^.flocation(?: |$)(.*)")
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await event.edit("`Masukan jumlah detik yang benar`")
    await event.edit(f"`Memulai Share Lokasi Palsu Selama` {t} sec.`")
    await asyncio.sleep(3)
    await event.delete()
    async with event.client.action(event.chat_id, "location"):
        await asyncio.sleep(t)


@register(outgoing=True, pattern="^.fcontact(?: |$)(.*)")
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await event.edit("`Masukan jumlah detik yang benar`")
    await event.edit(f"`Memulai Mengirim Contact Palsu Selama` {t} sec.`")
    await asyncio.sleep(3)
    await event.delete()
    async with event.client.action(event.chat_id, "contact"):
        await asyncio.sleep(t)


@register(outgoing=True, pattern="^.fsticker(?: |$)(.*)")
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await event.edit("`Masukan jumlah detik yang benar`")
    await event.edit(f"`Memulai Mengirim Sticker Palsu Selama` {t} sec.`")
    await asyncio.sleep(3)
    await event.delete()
    async with event.client.action(event.chat_id, "sticker"):
        await asyncio.sleep(t)


CMD_HELP.update(
    {
        "fakeaction": f"**Plugin :** `fakeaction`\
        \n\n  •  **Perintah :** `{cmd}ftyping`  <jumlah detik>\
        \n  •  **Kegunaan :** Menampilkan Pengetikan Palsu dalam obrolan\
        \n\n  •  **Perintah :** `{cmd}faudio` <jumlah detik>\
        \n  •  **Kegunaan :** Menampilkan Tindakan Merekam suara Palsu dalam obrolan\
        \n\n  •  **Perintah :** `{cmd}fvideo` <jumlah detik>\
        \n  •  **Kegunaan :** Menampilkan Tindakan Merekam Video Palsu dalam obrolan\
        \n\n  •  **Perintah :** `{cmd}fround` <jumlah detik>\
        \n  •  **Kegunaan :** Menampilkan Tindakan Merekam Live Video Round Palsu dalam obrolan\
        \n\n  •  **Perintah :** `{cmd}fgame` <jumlah detik>\
        \n  •  **Kegunaan :** Menampilkan sedang bermain game Palsu dalam obrolan\
        \n\n  •  **Perintah :** `{cmd}fphoto` <jumlah detik>\
        \n  •  **Kegunaan :** Menampilkan Tindakan Mengirim Photo Palsu dalam obrolan\
        \n\n  •  **Perintah :** `{cmd}fdocument` <jumlah detik>\
        \n  •  **Kegunaan :** Menampilkan Tindakan Mengirim Document/File Palsu dalam obrolan\
        \n\n  •  **Perintah :** `{cmd}flocation` <jumlah detik>\
        \n  •  **Kegunaan :** Menampilkan Tindakan Share Lokasi Palsu dalam obrolan\
        \n\n  •  **Perintah :** `{cmd}fcontact` <jumlah detik>\
        \n  •  **Kegunaan :** Menampilkan Tindakan Share Contact Palsu dalam obrolan\
        \n\n  •  **Perintah :** `{cmd}fsticker` <jumlah detik>\
        \n  •  **Kegunaan :** Menampilkan Tindakan Memilih Sticker Palsu dalam obrolan\
    "
    }
)
