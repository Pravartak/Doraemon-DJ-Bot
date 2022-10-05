from pyrogram.types import (InlineQueryResultArticle,
                            InputTextMessageContent)

answer = []

answer.extend(
    [
        InlineQueryResultArticle(
            title="🙄 ᑭᗩᑌՏᗴ 🙄",
            description=f"ᑭᗩᑌՏᗴ Tᕼᗴ ᑕᑌᖇᖇᗴᑎT ᑭᒪᗩYIᑎᘜ ՏTᖇᗴᗩᗰ Oᑎ ᐯIᗪᗴOᑕᕼᗩT.",
            thumb_url="https://telegra.ph/file/c5952790fa8235f499749.jpg",
            input_message_content=InputTextMessageContent("/pause"),
        ),
        InlineQueryResultArticle(
            title="😋 ᖇᗴՏᑌᗰᗴ 😋",
            description=f"ᖇᗴՏᑌᗰᗴ Tᕼᗴ ᑭᗩᑌՏᗴᗪ ՏTᖇᗴᗩᗰ Oᑎ ᐯIᗪᗴOᑕᕼᗩT.",
            thumb_url="https://telegra.ph/file/c5952790fa8235f499749.jpg",
            input_message_content=InputTextMessageContent("/resume"),
        ),
        InlineQueryResultArticle(
            title="🙂 ՏKIᑭ 🙂",
            description=f"ՏKIᑭՏ Tᕼᗴ ᑕᑌᖇᖇᗴᑎT ᑭᒪᗩYIᑎᘜ ՏTᖇᗴᗩᗰ Oᑎ ᐯIᗪᗴOᑕᕼᗩT ᗩᑎᗪ ᗰOᐯᗴՏ TO Tᕼᗴ ᑎᗴ᙭T ՏTᖇᗴᗩᗰ.",
            thumb_url="https://telegra.ph/file/c5952790fa8235f499749.jpg",
            input_message_content=InputTextMessageContent("/skip"),
        ),
        InlineQueryResultArticle(
            title="🥺 ᗴᑎᗪ 🥺",
            description="ᗴᑎᗪ Tᕼᗴ ᑕᑌᖇᖇᗴᑎT ᑭᒪᗩYIᑎᘜ ՏTᖇᗴᗩᗰ Oᑎ ᐯIᗪᗴOᑕᕼᗩT.",
            thumb_url="https://telegra.ph/file/c5952790fa8235f499749.jpg",
            input_message_content=InputTextMessageContent("/end"),
        ),
        InlineQueryResultArticle(
            title="🥴 Տᕼᑌᖴᖴᒪᗴ 🥴",
            description="Տᕼᑌᖴᖴᒪᗴ Tᕼᗴ ᑫᑌᗴᑌᗴᗪ ՏOᑎᘜՏ Iᑎ ᑭᒪᗩYᒪIՏT.",
            thumb_url="https://telegra.ph/file/c5952790fa8235f499749.jpg",
            input_message_content=InputTextMessageContent("/shuffle"),
        ),
        InlineQueryResultArticle(
            title="🥱 ᒪOOᑭ 🥱",
            description="ᒪOOᑭ Tᕼᗴ ᑕᑌᖇᖇᗴᑎT ᑭᒪᗩYIᑎᘜ TᖇᗩᑕK Oᑎ ᐯIᗪᗴOᑕᕼᗩT.",
            thumb_url="https://telegra.ph/file/c5952790fa8235f499749.jpg",
            input_message_content=InputTextMessageContent("/loop 3"),
        ),
    ]
)
