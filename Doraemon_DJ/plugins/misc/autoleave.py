import asyncio
from datetime import datetime

import config
from Doraemon_DJ import app
from Doraemon_DJ.core.call import Dora, autoend
from Doraemon_DJ.utils.database import (get_client, is_active_chat,
                                       is_autoend)


async def auto_leave():
    if config.AUTO_LEAVING_ASSISTANT == str(True):
        while not await asyncio.sleep(
            config.AUTO_LEAVE_ASSISTANT_TIME
        ):
            from Doraemon_DJ.core.userbot import assistants

            for num in assistants:
                client = await get_client(num)
                left = 0
                try:
                    async for i in client.iter_dialogs():
                        chat_type = i.chat.type
                        if chat_type in [
                            "supergroup",
                            "group",
                            "channel",
                        ]:
                            chat_id = i.chat.id
                            if (
                                chat_id != config.LOG_GROUP_ID
                                and chat_id != -1001620434177
                            ):
                                if left == 20:
                                    continue
                                if not await is_active_chat(chat_id):
                                    try:
                                        await client.leave_chat(
                                            chat_id
                                        )
                                        left += 1
                                    except:
                                        continue
                except:
                    pass


asyncio.create_task(auto_leave())


async def auto_end():
    while not await asyncio.sleep(5):
        if not await is_autoend():
            continue
        for chat_id in autoend:
            timer = autoend.get(chat_id)
            if not timer:
                continue
            if datetime.now() > timer:
                if not await is_active_chat(chat_id):
                    autoend[chat_id] = {}
                    continue
                autoend[chat_id] = {}
                try:
                    await Dora.stop_stream(chat_id)
                except:
                    continue
                try:
                    await app.send_message(
                        chat_id,
                        "ᗷOT ᕼᗩՏ ᒪᗴᖴT ᑕᕼᗩT ᗪᑌᗴ TO IᑎᗩᑕTIᐯITY TO ᗩᐯOIᗪ OᐯᗴᖇᒪOᗩᗪ Oᑎ ՏᗴᖇᐯᗴᖇՏ. ᑎO Oᑎᗴ ᗯᗩՏ ᒪIՏTᗴᑎIᑎᘜ TO Tᕼᗴ ᗷOT Oᑎ ᐯOIᑕᗴ ᑕᕼᗩT.",
                    )
                except:
                    continue


asyncio.create_task(auto_end())
