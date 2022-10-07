from typing import Union

from pyrogram.types import InlineKeyboardButton

import config
from Doraemon_DJ import app


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="🥺 ᗩᗪᗪ ᗰᗴ ᑭᒪᗴᗩՏᗴ 🥺",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="ᕼᗴᒪᑭ",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="ՏᗴTTIᑎᘜՏ", callback_data="settings_helper"
            ),
        ],
        [
            InlineKeyboardButton(
                text="ᗰᗩIᑎTᗩIᑎᗴᖇ", user_id=OWNER),
            InlineKeyboardButton(
                text="ՏᑌᑭᑭOᖇT", url=f"{config.SUPPORT_GROUP}"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="ᗩᗪᗪ ᗰᗴ ᗩᑎᗪ ᖇOᑕK ",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="ᕼᗴᒪᑭ", callback_data="settings_back_helper"
            ),
        ],
        [
            InlineKeyboardButton(text="ᗰᗩIᑎTᗩIᑎᗴᖇ", user_id=OWNER),
            InlineKeyboardButton(
                text="ՏᑌᑭᑭOᖇT", url=f"{config.SUPPORT_GROUP}"
            ),
        ],
        [
            InlineKeyboardButton(
                    text="ᗪᗴᑭᒪOY YOᑌᖇ Oᗯᑎ ᗷOT", url=f"{config.UPSTREAM_REPO}"
                )
        ],
     ]
    return buttons
