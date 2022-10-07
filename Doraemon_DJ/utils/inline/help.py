from typing import Union

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from Doraemon_DJ import app
from config import SUPPORT_GROUP


def help_pannel(_, START: Union[bool, int] = None):
    first = [
        InlineKeyboardButton(
            text=_["CLOSEMENU_BUTTON"], callback_data=f"close"
        )
    ]
    second = [
        InlineKeyboardButton(
            text=_["BACK_BUTTON"],
            callback_data=f"settingsback_helper",
        ),
        InlineKeyboardButton(
            text=_["CLOSEMENU_BUTTON"], callback_data=f"close"
        ),
    ]
    mark = second if START else first
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="ᗩᗪᗰIᑎ",
                    callback_data="help_callback hb1",
                ),
                InlineKeyboardButton(
                    text="ᗩᑌTᕼ",
                    callback_data="help_callback hb2",
                ),
                InlineKeyboardButton(
                    text="ᗷᒪᗩᑕKᒪIՏT",
                    callback_data="help_callback hb3",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="ᗷᖇOᗩᗪᑕᗩՏT",
                    callback_data="help_callback hb4",
                ),
                InlineKeyboardButton(
                    text="ᘜᗷᗩᑎ",
                    callback_data="help_callback hb12",
                ),
                InlineKeyboardButton(
                    text="ᒪYᖇIᑕՏ",
                    callback_data="help_callback hb5",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="ᑭIᑎᘜ",
                    callback_data="help_callback hb7",
                ),
                InlineKeyboardButton(
                    text="ᑭᒪᗩY",
                    callback_data="help_callback hb8",
                ),
                InlineKeyboardButton(
                    text="ᑭᒪᗩYᒪIՏT",
                    callback_data="help_callback hb6",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="ᐯIᗪᗴOᑕᕼᗩTՏ",
                    callback_data="help_callback hb10",
                ),
                InlineKeyboardButton(
                    text="ՏTᗩᖇT",
                    callback_data="help_callback hb11",
                ),
                InlineKeyboardButton(
                    text="ՏᑌᗪO",
                    callback_data="help_callback hb9",
                ),
            ],
            mark,
        ]
    )
    return upl


def help_back_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data=f"settings_back_helper",
                ),
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"], callback_data=f"close"
                ),
                InlineKeyboardButton(
                    text="• ՏᑌᑭᑭOᖇT •", url=f"{SUPPORT_GROUP}"
                ),
            ]
        ]
    )
    return upl


def private_help_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"],
                url=f"https://t.me/{app.username}?start=help",
            ),
        ],
    ]
    return buttons
