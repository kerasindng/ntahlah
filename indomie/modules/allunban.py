# Port By @VckyouuBitch From GeezProjects
# Copyright © 2021 Geez-Projects

from time import sleep
from telethon.tl.types import ChatBannedRights
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChannelParticipantsKicked

from indomie import CMD_HANDLER as cmd
from indomie.utils import indomie_cmd
from indomie import CMD_HELP


@indomie_cmd(pattern="allban(?: |$)(.*)")
async def testing(event):
    nikal = await event.get_chat()
    chutiya = await event.client.get_me()
    admin = nikal.admin_rights
    creator = nikal.creator
    if not admin and not creator:
        await event.edit("`Anda Tidak Mempunyai Hak Disini`")
        return
    await event.edit("**Berjalan.**")
    sleep(3)
    await event.edit("**Berjalan..**")
    sleep(3)
    await event.edit("**Berjalan...**")
    sleep(3)
    await event.edit("**Berjalan....**")

    everyone = await event.client.get_participants(event.chat_id)
    for user in everyone:
        if user.id == chutiya.id:
            pass
        try:
            await event.client(EditBannedRequest(event.chat_id, int(user.id), ChatBannedRights(until_date=None, view_messages=True)))
        except Exception as e:
            await event.edit(str(e))
        await sleep(.5)
    await event.edit("**Perintah berhasil di jalankan**\n\n__Semua member telah terblokir__ 🙂")


@indomie_cmd(pattern="allunban(?: |$)(.*)")
async def _(event):
    await event.edit("`Sedang Mencari List Banning.`")
    p = 0
    (await event.get_chat()).title
    async for i in event.client.iter_participants(
        event.chat_id,
        filter=ChannelParticipantsKicked,
        aggressive=True,
    ):
        try:
            await event.client.edit_permissions(event.chat_id, i, view_messages=True)
            p += 1
        except BaseException:
            pass
    await event.edit("`Sukses Menghapus List Banning`")


CMD_HELP.update(
    {
        "allunban": f"𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}allunban`\
    \n↳ : Membatalkan semua Ban Di Anggota Grup."
    }
)
