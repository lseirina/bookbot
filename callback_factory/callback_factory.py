from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.filters.callback_data import CallbackData
from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    CallbackQuery,
    Message,
)

BOT_TOKEN = '6883498485:AAGtOZFurG3T-H2oDNwhQcUqeUzlMfqcJHE'
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


class GoodsCallbackDataFactory(CallbackData, prefix='goods'):
    id_category: int
    id_subcategory: int
    id_item: int


button_1 = InlineKeyboardButton(
    text='1 Category',
    callback_data=GoodsCallbackDataFactory(
        id_category=1,
        id_subcategory=0,
        id_item=0
    ).pack()
)
button_2 = InlineKeyboardButton(
    text="2 category",
    callback_data=GoodsCallbackDataFactory(
        id_category=2,
        id_subcategory=0,
        id_item=0
    ).pack()
)
markup = InlineKeyboardMarkup(
    inline_keyboard=[[button_1], [button_2]]
    )


@dp.message(CommandStart)
async def process_start_command(message: Message):
    await message.answer(
        text='This is inlineKeyboard',
        reply_markup=markup
    )


@dp.callback_query(GoodsCallbackDataFactory.filter(F.id_category == 1))
async def procces_category_press(callback: CallbackQuery,
                                 callback_data=GoodsCallbackDataFactory):
    await callback.message.answer(text=callback_data.pack())
    await callback.answer()


# @dp.callback_query(GoodsCallbackDataFactory.filter())
# async def process_category_press(callback: CallbackQuery,
#                                  callback_data: GoodsCallbackDataFactory
#                                  ):
#     await callback.message.answer(text=callback_data.pack())
#     await callback.answer()


# @dp.callback_query()
# async def procces_button_press(callback: CallbackQuery):
#     await callback.model_dump_json(indent=4, exclude_none=True)
#     await callback.answer()


if __name__ == '__main__':
    dp.run_polling(bot)
