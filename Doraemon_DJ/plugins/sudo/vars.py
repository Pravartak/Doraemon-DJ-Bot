import asyncio

from pyrogram import filters

import config
from strings import get_command
from Doraemon_DJ import app
from Doraemon_DJ.misc import SUDOERS
from Doraemon_DJ.utils.database.memorydatabase import get_video_limit
from Doraemon_DJ.utils.formatters import convert_bytes

VARS_COMMAND = get_command("VARS_COMMAND")


@app.on_message(filters.command(VARS_COMMAND) & SUDOERS)
async def varsFunc(client, message):
    mystic = await message.reply_text(
        "ᘜᗴTTIᑎᘜ YOᑌᖇ ᑕOᑎᖴIᘜ... ᑭᒪᗴᗩՏᗴ ᗯᗩIT..."
    )
    v_limit = await get_video_limit()
    bot_name = config.MUSIC_BOT_NAME
    up_r = f"[ᖇᗴᑭO]({config.UPSTREAM_REPO})"
    up_b = config.UPSTREAM_BRANCH
    auto_leave = config.AUTO_LEAVE_ASSISTANT_TIME
    yt_sleep = config.YOUTUBE_DOWNLOAD_EDIT_SLEEP
    tg_sleep = config.TELEGRAM_DOWNLOAD_EDIT_SLEEP
    playlist_limit = config.SERVER_PLAYLIST_LIMIT
    fetch_playlist = config.PLAYLIST_FETCH_LIMIT
    song = config.SONG_DOWNLOAD_DURATION
    play_duration = config.DURATION_LIMIT_MIN
    cm = config.CLEANMODE_DELETE_MINS
    auto_sug = config.AUTO_SUGGESTION_TIME
    if config.AUTO_LEAVING_ASSISTANT == str(True):
        ass = "YᗴՏ"
    else:
        ass = "ᑎO"
    if config.PRIVATE_BOT_MODE == str(True):
        pvt = "Yᗴᗪ"
    else:
        pvt = "ᑎO"
    if config.AUTO_SUGGESTION_MODE == str(True):
        a_sug = "YᗴՏ"
    else:
        a_sug = "ᑎO"
    if config.AUTO_DOWNLOADS_CLEAR == str(True):
        down = "YᗴՏ"
    else:
        down = "ᑎO"

    if not config.GITHUB_REPO:
        git = "ᑎO"
    else:
        git = f"[ᖇᗴᑭO]({config.GITHUB_REPO})"
    if not config.START_IMG_URL:
        start = "ᑎO"
    else:
        start = f"[Iᗰᗩᘜᗴ]({config.START_IMG_URL})"
    if not config.SUPPORT_CHANNEL:
        s_c = "ᑎO"
    else:
        s_c = f"[ᑕᕼᗩᑎᑎᗴᒪ]({config.SUPPORT_CHANNEL})"
    if not config.SUPPORT_GROUP:
        s_g = "ᑎO"
    else:
        s_g = f"[ᘜᖇOᑌᑭ]({config.SUPPORT_GROUP})"
    if not config.GIT_TOKEN:
        token = "ᑎO"
    else:
        token = "YᗴՏ"
    if (
        not config.SPOTIFY_CLIENT_ID
        and not config.SPOTIFY_CLIENT_SECRET
    ):
        sotify = "ᑎO"
    else:
        sotify = "YᗴՏ"
    owners = [str(ids) for ids in config.OWNER_ID]
    owner_id = " ,".join(owners)
    tg_aud = convert_bytes(config.TG_AUDIO_FILESIZE_LIMIT)
    tg_vid = convert_bytes(config.TG_VIDEO_FILESIZE_LIMIT)
    text = f"""**ᗰᑌՏIᑕ ᗷOT ᑕOᑎᖴIᘜ ᐯᗩᖇՏ:**

**<u>ᗷᗩՏIᑕ ᐯᗩᖇՏ:</u>**
**ᗰᑌՏIᑕ_ᗷOT_ᑎᗩᗰᗴ** : **{bot_name}**
**ᗪᑌᖇᗩTIOᑎ_ᒪIᗰIT** : **{play_duration} ᗰIᑎᑌTᗴՏ**
**ՏOᑎᘜ_ᗪOᗯᑎᒪOᗩᗪ_ᗪᑌᖇᗩTIOᑎ_ᒪIᗰIT** :** {song} ᗰIᑎᑌTᗴՏ**
**Oᗯᑎᗴᖇ_Iᗪ** : **{owner_id}**
    
**<u>ᑕᑌՏTOᗰ ᖇᗴᑭO ᐯᗩᖇՏ:</u>**
**ᑌᑭՏTᖇᗴᗩᗰ_ᖇᗴᑭO** : **{up_r}**
**ᑌᑭՏTᖇᗴᗩᗰ_ᗷᖇᗩᑎᑕᕼ** : **{up_b}**
**ᘜITᕼᑌᗷ_ᖇᗴᑭO** :** {git}**
**ᘜIT_TOKᗴᑎ**:** {token}**


**<u>ᗷOT ᐯᗩᖇՏ:</u>**
**ᗩᑌTO_ᒪᗴᗩᐯIᑎᘜ_ᗩՏՏIՏTᗩᑎT** : **{ass}**
**ᗩՏՏIՏTᗩᑎT_ᒪᗴᗩᐯᗴ_TIᗰᗴ** : **{auto_leave} ՏᗴᑕOᑎᗪՏ**
**ᗩᑌTO_ՏᑌᘜᘜᗴՏTIOᑎ_ᗰOᗪᗴ** :** {a_sug}**
**ᗩᑌTO_ՏᑌᘜᘜᗴՏTIOᑎ_TIᗰᗴ** : **{auto_sug} ՏᗴᑕOᑎᗪՏ**
**ᗩᑌTO_ᗪOᗯᑎᒪOᗩᗪՏ_ᑕᒪᗴᗩᖇ** : **{down}**
**ᑭᖇIᐯᗩTᗴ_ᗷOT_ᗰOᗪᗴ** : **{pvt}**
**YOᑌTᑌᗷᗴ_EDIT_SLEEP` : **{yt_sleep} ՏᗴᑕOᑎᗪՏ**
**Tᗴᒪᗴᘜᖇᗩᗰ_ᗴᗪIT_Տᒪᗴᗴᑭ** :** {tg_sleep} ՏᗴᑕOᑎᗪՏ**
**ᑕᒪᗴᗩᑎᗰOᗪᗴ_ᗰIᑎՏ** : **{cm} ᗰIᑎᑌTᗴՏ**
**ᐯIᗪᗴO_ՏTᖇᗴᗩᗰ_ᒪIᗰIT** : **{v_limit} ᑕᕼᗩTՏ**
**Տᗴᖇᗴᐯᗴᖇ_ᑭᒪᗩYᒪIՏT_ᒪIᗰIT** :** {playlist_limit}**
**ᑭᒪᗩYᒪIՏT_ᖴᗴTᑕᕼ_ᒪIᗰIT** :** {fetch_playlist}**

**<u>ՏᑭOTIᖴY ᐯᗩᖇՏ:</u>**
**ՏᑭOTIᖴY_ᑕᒪIᗴᑎT_Iᗪ** :** {sotify}**
**ՏᑭOTIᖴY_ᑕᒪIᗴᑎT_ՏᗴᑕᖇᗴT** : **{sotify}**

**<u>ᑭᒪᗩYՏIᘔᗴ ᐯᗩᖇՏ:</u>**
**Tᘜ_ᗩᑌᗪIO_ᖴIᒪᗴՏIᘔᗴ_ᒪIᗰIT** :** {tg_aud}**
**Tᘜ_ᐯIᗪᗴO_ᖴIᒪᗴՏIᘔᗴ_ᒪIᗰIT** :** {tg_vid}**

**<u>ᑌᖇᒪ ᐯᗩᖇՏ:</u>**
**ՏᑌᑭᑭOᖇT_ᑕᕼᗩᑎᑎᗴᒪ* : **{s_c}**
**ՏᑌᑭᑭOᖇT_ᘜᖇOᑌᑭ** : ** {s_g}**
**ՏTᗩᖇT_Iᗰᘜ_ᑌᖇᒪ** : ** {start}**
    """
    await asyncio.sleep(1)
    await mystic.edit_text(text)
