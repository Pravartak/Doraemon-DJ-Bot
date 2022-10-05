import asyncio
import importlib
import sys

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from config import BANNED_USERS
from Doraemon_DJ import LOGGER, app, userbot
from Doraemon_DJ.core.call import Dora
from Doraemon_DJ.plugins import ALL_MODULES
from Doraemon_DJ.utils.database import get_banned_users, get_gbanned

loop = asyncio.get_event_loop()


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("Doraemon_DJ").error(
            "WTF Baby ! Atleast add a pyrogram string, How Cheap..."
        )
        return
    if (
        not config.SPOTIFY_CLIENT_ID
        and not config.SPOTIFY_CLIENT_SECRET
    ):
        LOGGER("Doraemon_DJ").warning(
            "Spotify Client Id & Secret not added, itni simple cheez bhi nhi laa paye, huh."
        )
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("Doraemon_DJ.plugins" + all_module)
    LOGGER("Doraemon_DJ.plugins").info(
        "Necessary Modules Imported Successfully."
    )
    await userbot.start()
    await Dora.start()
    try:
        await Dora.stream_call(
            "https://telegra.ph/file/8d5db123638c2f6bb6ce4.mp4"
        )
    except NoActiveGroupCall:
        LOGGER("Doraemon_DJ").error(
            "[ERROR] - \n\nHey Baby, firstly open telegram and turn on voice chat in Logger Group. If you ever ended voice chat in log group i will stop working and users will fu*k you up."
        )
        sys.exit()
    except:
        pass
    await Dora.decorators()
    LOGGER("Doraemon_DJ").info("Music Bot Started Successfully, Now Rock yourself and every group or channel you have")
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("Doraemon_DJ").info("Stopping Music Bot")
