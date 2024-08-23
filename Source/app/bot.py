import app.GetID_Pyrogram as PyrogramEngine
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import ContentType
from app.config import TELEGRAM_TOKEN
from aiogram.filters import CommandStart

# Get API bot token
bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher()

# Setup keyboard for the quick actions
kb = [[types.KeyboardButton(text="❔ About")]]
keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, input_field_placeholder="")  # Create keyboard


# Run after /start command
@dp.message(CommandStart())
async def send_welcome(message: types.Message):
    await message.answer(
        "💡 Send a sticker or custom emoji in the chat and the creator's ID will be displayed.",
        parse_mode="Markdown", reply_markup=keyboard)


# Get about after pressing keyboard
@dp.message(F.text == "❔ About")
async def get_about(message: types.Message):
    await message.reply(
        "💡 Send a sticker or custom emoji in the chat and the creator's ID will be displayed.",
        parse_mode='Markdown')


# React on messages of type "stickers"
@dp.message(F.content_type == ContentType.STICKER)
async def get_sticker_id(message: types.Message):
    print(f'[v] {message.from_user.id} requested ID for sticker')
    # Extract short name
    short_name = message.sticker.set_name
    # Extract user ID
    user_id = await PyrogramEngine.get_id_by_sticker(short_name)
    if user_id is not None:
        await message.reply(
            f"📧 *ID:* `{user_id}`\n\n[[iOS]] t.me/@id{user_id} \n[[Android]] "
            + 'tg://openmessage?user_id='.replace("_", "\\_") + f'{user_id}',
            parse_mode="Markdown")


# React on messages of type "text" (process emoji)
@dp.message(F.content_type == ContentType.TEXT)
async def get_emoji_id(message: types.Message):
    print(f'[v] {message.from_user.id} requested ID for emoji')
    # Set up an array for all emojis in message
    custom_emoji_ids = []
    for i in range(len(message.entities)):
        if message.entities[i].custom_emoji_id is not None:
            cei = int(message.entities[i].custom_emoji_id)
            if cei not in custom_emoji_ids:
                custom_emoji_ids.append(cei)
    if len(custom_emoji_ids) > 0:
        user_id = await PyrogramEngine.get_id_by_emoji(custom_emoji_ids)
        for i in range(len(user_id)):
            if user_id[i] is not None:
                await message.reply(
                    f"📧 *ID:* `{user_id[i]}`\n\n[[iOS]] t.me/@id{user_id[i]} \n[[Android]] "
                    + 'tg://openmessage?user_id='.replace("_", "\\_") + f'{user_id[i]}',
                    parse_mode="Markdown")
