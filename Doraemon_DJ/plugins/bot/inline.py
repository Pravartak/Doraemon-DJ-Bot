from pyrogram.types import (InlineKeyboardButton,
                            InlineKeyboardMarkup,
                            InlineQueryResultPhoto)
from youtubesearchpython.__future__ import VideosSearch

from config import BANNED_USERS, MUSIC_BOT_NAME
from Doraemon_DJ import app
from Doraemon_DJ.utils.inlinequery import answer


@app.on_inline_query(~BANNED_USERS)
async def inline_query_handler(client, query):
    text = query.query.strip().lower()
    answers = []
    if text.strip() == "":
        try:
            await client.answer_inline_query(
                query.id, results=answer, cache_time=10
            )
        except:
            return
    else:
        a = VideosSearch(text, limit=20)
        result = (await a.next()).get("result")
        for x in range(15):
            title = (result[x]["title"]).title()
            duration = result[x]["duration"]
            views = result[x]["viewCount"]["short"]
            thumbnail = result[x]["thumbnails"][0]["url"].split("?")[
                0
            ]
            channellink = result[x]["channel"]["link"]
            channel = result[x]["channel"]["name"]
            link = result[x]["link"]
            published = result[x]["publishedTime"]
            description = f"{views} | {duration} Mins | {channel}  | {published}"
            buttons = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="ðº á¯á©Táá¼ Oá YOáTáá·á´",
                            url=link,
                        )
                    ],
                ]
            )
            searched_text = f"""
ð**TITáªá´:** [{title}]({link})

â³**áªááá©TIOá:** {duration} á°IááTá´Õ
ð**á¯Iá´á¯Õ:** `{views}`
â°**áá­áªOá©áªá´áª Oá:** {published}
ð¥**áá¼á©ááá´áª áá©á°á´:** {channel}
ð**áá¼á©ááá´áª áªIáK:** [ á¯IÕIT áá¼á©ááá´áª]({channellink})

**áá´á­áªY á¯ITá¼ /play Oá Tá¼IÕ Õá´á©ááá¼á´áª á°á´ÕÕá©áá´ TO ÕTáá´á©á° IT Oá á¯OIáá´ áá¼á©T.**

ð® **Õá´á©ááá¼ á­Oá¯á´áá´áª á·Y {MUSIC_BOT_NAME} ð**"""
            answers.append(
                InlineQueryResultPhoto(
                    photo_url=thumbnail,
                    title=title,
                    thumb_url=thumbnail,
                    description=description,
                    caption=searched_text,
                    reply_markup=buttons,
                )
            )
        try:
            return await client.answer_inline_query(
                query.id, results=answers
            )
        except:
            return

