import json
import urllib.request


from indomie.events import register
from indomie import CMD_HELP


# Port By @VckyouuBitch From GeezProject
# Buat Kamu Yang Hapus Credits. Intinya Kamu Anjing:)
@register(outgoing=True, pattern="^.ip(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)

    adress = input_str

    token = "19e7f2b6fe27deb566140aae134dec6b"

    api = "http://api.ipstack.com/" + adress + "?access_key=" + token + "&format=1"

    result = urllib.request.urlopen(api).read()
    result = result.decode()

    result = json.loads(result)
    ab = result["type"]
    cd = result["country_code"]
    ef = result["region_name"]
    gh = result["city"]
    ij = result["zip"]
    kl = result["latitude"]
    mn = result["longitude"]
    await event.edit(
        f"<b><u>INFORMASI BERHASIL DIKUMPULKAN</b></u>\n\n<b>Ip type :-</b><code>{ab}</code>\n<b>Country code:- </b> <code>{cd}</code>\n<b>State name :-</b><code>{ef}</code>\n<b>City name :- </b><code>{gh}</code>\n<b>zip :-</b><code>{ij}</code>\n<b>Latitude:- </b> <code>{kl}</code>\n<b>Longitude :- </b><code>{mn}</code>\n",
        parse_mode="HTML",
    )


CMD_HELP.update(
    {
        "fakeaddress": "**IP HACK**\
	\n\n**Syntax : **`.ip <ip address>`\
	\n**Usage :** Memberikan detail tentang alamat ip."
    }
)
