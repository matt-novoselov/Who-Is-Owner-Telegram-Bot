from pyrogram import Client
from pyrogram.raw.functions.messages import GetStickerSet
from pyrogram.raw.types import InputStickerSetShortName
from dotenv import load_dotenv
import os

load_dotenv()
session_string = os.getenv('SESSION_STRING')
app = Client("my_account", session_string=session_string)


async def get_id_by_sticker(set_short_name):
    await app.stop()
    try:
        sticker_set = await app.invoke(
            query=GetStickerSet(
                hash=0,
                stickerset=InputStickerSetShortName(short_name=set_short_name)
            )
        )
        return sticker_set.set.id >> 32
    except:
        pass


async def get_id_by_emoji(custom_emoji_ids):
    stickers = await app.get_custom_emoji_stickers(
        custom_emoji_ids=custom_emoji_ids
    )
    UserIDs = []
    for i in range(len(stickers)):
        UserIDs.append(await get_id_by_sticker(stickers[i].set_name))

    return UserIDs
