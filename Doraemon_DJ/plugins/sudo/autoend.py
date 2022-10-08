from pyrogram import filters

import config
from strings import get_command
from Doraemon_DJ import app
from Doraemon_DJ.misc import SUDOERS
from Doraemon_DJ.utils.database import autoend_off, autoend_on
from Doraemon_DJ.utils.decorators.language import language

# Commands
AUTOEND_COMMAND = get_command("AUTOEND_COMMAND")


@app.on_message(filters.command(AUTOEND_COMMAND) & SUDOERS)
async def auto_end_stream(client, message):
    usage = "**ᑌՏᗩᘜᗴ:**\n\n/autoend [enable|disable]"
    if len(message.command) != 2:
        return await message.reply_text(usage)
    state = message.text.split(None, 1)[1].strip()
    state = state.lower()
    if state == "enable":
        await autoend_on()
        await message.reply_text(
            "ᗩᑌTO ᗴᑎᗪ ՏTᖇᗴᗩᗰ ᗴᑎᗩᗷᒪᗴᗪ.\n\nᗷOT ᗯIᒪᒪ ᒪᗴᗩᐯᗴ ᐯOIᑕᗴ ᑕᕼᗩT ᗩᑌTOᗰᗩTIᑕᗩᒪᒪY ᗩᖴTᗴᖇ 3 ᗰIᑎՏ Iᖴ ᑎO Oᑎᗴ IՏ ᒪIՏTᗴᑎIᑎᘜ ᗯITᕼ ᗩ ᗯᗩᖇᑎIᑎᘜ ᗰᗴՏՏᗩᘜᗴ..."
        )
    elif state == "disable":
        await autoend_off()
        await message.reply_text("ᗩᑌTO ᗴᑎᗪ ՏTᖇᗴᗩᗰ ᗪIՏᗩᗷᒪᗴᗪ.")
    else:
        await message.reply_text(usage)

