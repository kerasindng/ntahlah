
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from indomie.events import register
from indomie import bot, CMD_HELP
from indomie import CMD_HANDLER as cmd


@register(outgoing=True, pattern="^.igsaver ?(.*)")
async def igsaver(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("`Mohon Reply Ke Link Instagram Ya..`")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.text:
        await event.edit("`Mohon Maaf, Saya Membutuhkan Link Media Instagram Untuk di Download`")
        return
    chat = "@SaveAsBot"
    reply_message.sender
    if reply_message.sender.bot:
        await event.edit("`Sedang Memproses...`")
        return
    await event.edit("`Sedang Memproses...`")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=523131145)
            )
            await event.client.send_message(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.edit("`Mohon Pergi ke ` @SaveAsbot `Lalu Tekan Start dan Coba Lagi.`")
            return
        if response.text.startswith("Forward"):
            await event.edit(
                "Uhmm Sepertinya Private."
            )
        else:
            await event.delete()
            aku = await event.client.get_me()
            await event.client.send_file(
                event.chat_id,
                response.message.media,
                caption=f"**Download By {aku.first_name}**",
            )
            await event.client.send_read_acknowledge(conv.chat_id)
            await bot(functions.messages.DeleteHistoryRequest(peer=chat, max_id=0))
            await event.delete()


CMD_HELP.update({
    "instasaver": f"𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}igsaver`"
    "\n↳ : Download Postingan di Instagram, Silahkan Salin Link Postingan Instagram Yang Ingin Anda Download Terus Kirim Link, Lalu Reply dan Ketik `.igsaver`."
})
