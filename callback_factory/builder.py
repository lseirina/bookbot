from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import (
    Message
)
from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder


BOT_TOKEN = '6883498485:AAGtOZFurG3T-H2oDNwhQcUqeUzlMfqcJHE'
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


class GoodsCallbackFactory(CallbackData, prefix='goods'):
    category_id: int
    subcategory_id: int
    item_id: int


builder = InlineKeyboardBuilder()

builder.button(
    text='Category_1',
    callback_data=GoodsCallbackFactory(
        category_id=1,
        subcategory_id=0,
        item_id=0
    )
)

builder.button(
    text='Category_2',
    callback_data=GoodsCallbackFactory(
        category_id=2,
        subcategory_id=0,
        item_id=0
    )
)

builder.adjust()

@dp.message(CommandStart)
async def process_start_command(message: Message):
    await message.answer(
        text='This is a keyboard',
        reply_markup=builder.as_markup()
    )


if __name__ == '__main__':
    dp.run_polling(bot)

