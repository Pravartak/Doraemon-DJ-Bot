from pyrogram.types import (InlineQueryResultArticle,
                            InputTextMessageContent)

answer = []

answer.extend(
    [
        InlineQueryResultArticle(
            title="ð á­á©áÕá´ ð",
            description=f"á­á©áÕá´ Tá¼á´ ááááá´áT á­áªá©YIáá ÕTáá´á©á° Oá á¯Iáªá´Oáá¼á©T.",
            thumb_url="https://telegra.ph/file/c5952790fa8235f499749.jpg",
            input_message_content=InputTextMessageContent("/pause"),
        ),
        InlineQueryResultArticle(
            title="ð áá´Õáá°á´ ð",
            description=f"áá´Õáá°á´ Tá¼á´ á­á©áÕá´áª ÕTáá´á©á° Oá á¯Iáªá´Oáá¼á©T.",
            thumb_url="https://telegra.ph/file/c5952790fa8235f499749.jpg",
            input_message_content=InputTextMessageContent("/resume"),
        ),
        InlineQueryResultArticle(
            title="ð ÕKIá­ ð",
            description=f"ÕKIá­Õ Tá¼á´ ááááá´áT á­áªá©YIáá ÕTáá´á©á° Oá á¯Iáªá´Oáá¼á©T á©ááª á°Oá¯á´Õ TO Tá¼á´ áá´á­T ÕTáá´á©á°.",
            thumb_url="https://telegra.ph/file/c5952790fa8235f499749.jpg",
            input_message_content=InputTextMessageContent("/skip"),
        ),
        InlineQueryResultArticle(
            title="ð¥º á´ááª ð¥º",
            description="á´ááª Tá¼á´ ááááá´áT á­áªá©YIáá ÕTáá´á©á° Oá á¯Iáªá´Oáá¼á©T.",
            thumb_url="https://telegra.ph/file/c5952790fa8235f499749.jpg",
            input_message_content=InputTextMessageContent("/end"),
        ),
        InlineQueryResultArticle(
            title="ð¥´ Õá¼áá´á´áªá´ ð¥´",
            description="Õá¼áá´á´áªá´ Tá¼á´ á«áá´áá´áª ÕOááÕ Iá á­áªá©YáªIÕT.",
            thumb_url="https://telegra.ph/file/c5952790fa8235f499749.jpg",
            input_message_content=InputTextMessageContent("/shuffle"),
        ),
        InlineQueryResultArticle(
            title="ð¥± áªOOá­ ð¥±",
            description="áªOOá­ Tá¼á´ ááááá´áT á­áªá©YIáá Táá©áK Oá á¯Iáªá´Oáá¼á©T.",
            thumb_url="https://telegra.ph/file/c5952790fa8235f499749.jpg",
            input_message_content=InputTextMessageContent("/loop 3"),
        ),
    ]
)
