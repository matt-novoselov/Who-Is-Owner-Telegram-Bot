from pyrogram import Client
from pyrogram.raw.functions.messages import GetStickerSet
from pyrogram.raw.types import InputStickerSetShortName
from app.config import SESSION_STRING


# Setup app client
app = Client("my_account", session_string=SESSION_STRING)


# Function to get User ID form sticker set short name
async def get_id_by_sticker(set_short_name):
    try:
        # Setup query
        sticker_set = await app.invoke(
            query=GetStickerSet(
                hash=0,
                stickerset=InputStickerSetShortName(short_name=set_short_name)
            )
        )
        # Shift sticker ID by 32 bits to extract User ID
        return sticker_set.set.id >> 32
    except Exception as e:
        print("We were unable to get id of sticker set, because:", e)


# Function to get User ID form emoji
async def get_id_by_emoji(custom_emoji_ids):
    stickers = await app.get_custom_emoji_stickers(
        custom_emoji_ids=custom_emoji_ids
    )
    UserIDs = []
    for i in range(len(stickers)):
        UserIDs.append(await get_id_by_sticker(stickers[i].set_name))

    return UserIDs
