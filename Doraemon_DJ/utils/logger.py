from config import LOG, LOG_GROUP_ID, MUSIC_BOT_NAME
from Doraemon_DJ import app
from Doraemon_DJ.utils.database import is_on_off


async def play_logs(message, streamtype):
    if await is_on_off(LOG):
        if message.chat.username:
            chatusername = f"@{message.chat.username}"
        else:
            chatusername = "ᑭᖇIᐯᗩTᗴ ᑕᕼᗩT"
        logger_text = f"""
**{MUSIC_BOT_NAME} ᑭᒪᗩY ᒪOᘜᘜᗴᖇ**

**ᑕᕼᗩT:** {message.chat.title} [`{message.chat.id}`]
**ᑌՏᗴᖇ:** {message.from_user.mention}
**ᑌՏᗴᖇᑎᗩᗰᗴ:** @{message.from_user.username}
**Iᗪ:** `{message.from_user.id}`
**ᑕᕼᗩT ᒪIᑎK:** {chatusername}

**Տᗴᗩᖇᑕᕼᗴᗪ ᖴOᖇ:** {message.text}

**ՏTᖇᗴᗩᗰ TYᑭᗴ:** {streamtype}"""
        if message.chat.id != LOG_GROUP_ID:
            try:
                await app.send_message(
                    LOG_GROUP_ID,
                    f"{logger_text}",
                    disable_web_page_preview=True,
                )
            except:
                pass
        return


