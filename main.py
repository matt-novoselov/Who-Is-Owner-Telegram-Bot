import GetID_Pyrogram
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os

load_dotenv()
bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)

kb = [[types.KeyboardButton(text="🛠️ Contact Support"), types.KeyboardButton(text="❔ About")]]
keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, input_field_placeholder="")  # Create keyboard


@dp.message_handler(commands=['start'])  # Run after /start command
async def send_welcome(message: types.Message):
    await message.answer(
        "💡 Send a sticker or custom emoji in the chat and the creator's ID will be displayed.",
        parse_mode="Markdown", reply_markup=keyboard)


@dp.message_handler(text="🛠️ Contact Support")  # Run action after pressing keyboard
async def get_support(message: types.Message):
    await message.reply("🛠️ You can contact support here: @NoveSupportBot")


@dp.message_handler(text="❔ About")  # Run action after pressing keyboard
async def get_about(message: types.Message):
    await message.reply(
        "💡 Send a sticker or custom emoji in the chat and the creator's ID will be displayed.",
        parse_mode='Markdown')


@dp.message_handler(content_types=["sticker"])
async def get_sticker_id(message: types.Message):
    print(f'[v] {message.from_user.id} requested ID for sticker')
    short_name = message.sticker.set_name
    user_id = await GetID_Pyrogram.get_id_by_sticker(short_name)
    if user_id is not None:
        await message.reply(
            f"📧 *ID:* `{user_id}`\n\n[[iOS]] t.me/@id{user_id} \n[[Android]] "
            + 'tg://openmessage?user_id='.replace("_", "\\_") + f'{user_id}',
            parse_mode="Markdown")


@dp.message_handler(content_types=["text"])
async def get_emoji_id(message: types.Message):
    print(f'[v] {message.from_user.id} requested ID for emoji')
    custom_emoji_ids = []
    for i in range(len(message.entities)):
        if message.entities[i].custom_emoji_id is not None:
            cei = int(message.entities[i].custom_emoji_id)
            if cei not in custom_emoji_ids:
                custom_emoji_ids.append(cei)
    if len(custom_emoji_ids) > 0:
        user_id = await GetID_Pyrogram.get_id_by_emoji(custom_emoji_ids)
        for i in range(len(user_id)):
            if user_id[i] is not None:
                await message.reply(
                    f"📧 *ID:* `{user_id[i]}`\n\n[[iOS]] t.me/@id{user_id[i]} \n[[Android]] "
                    + 'tg://openmessage?user_id='.replace("_", "\\_") + f'{user_id[i]}',
                    parse_mode="Markdown")

async def on_startup(_):
    await GetID_Pyrogram.app.start()


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
