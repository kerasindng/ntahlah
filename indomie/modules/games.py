from indomie import CMD_HELP, bot
from indomie import CMD_HANDLER as cmd
from indomie.events import register as memek


@memek(outgoing=True, pattern=r"^\.xogame(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    botusername = "@xobot"
    noob = "play"
    if event.reply_to_msg_id:
        await event.get_reply_message()
    tap = await bot.inline_query(botusername, noob)
    await tap[0].click(event.chat_id)
    await event.delete()


@memek(outgoing=True, pattern=r"^\.whisp(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    wwwspr = event.pattern_match.group(1)
    botusername = "@whisperBot"
    if event.reply_to_msg_id:
        await event.get_reply_message()
    tap = await bot.inline_query(botusername, wwwspr)
    await tap[0].click(event.chat_id)
    await event.delete()


@memek(outgoing=True, pattern=r"^\.mod(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    modr = event.pattern_match.group(1)
    botusername = "@PremiumAppBot"
    if event.reply_to_msg_id:
        await event.get_reply_message()
    tap = await bot.inline_query(botusername, modr)
    await tap[0].click(event.chat_id)
    await event.delete()

CMD_HELP.update(
    {
        "games": f"**Plugin : **`games`\
        \n\n  •  **Perintah :** `{cmd}xogame`\
        \n  •  **Kegunaan : **Mainkan game XO bersama temanmu.\
        \n\n  •  **Perintah :** `{cmd}whisp <teks> <username/ID>`\
        \n  •  **Kegunaan : **Berikan pesan rahasia\
        \n\n  •  **Perintah :** `{cmd}mod <nama app>`\
        \n  •  **Kegunaan : **Dapatkan applikasi mod\
    "
    }
)