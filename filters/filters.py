from aiogram.filters import BaseFilter
from aiogram.types import CallbackQuery


class IsDigitCallbackData(BaseFilter):
    async def __call__(self, callback: CallbackQuery):
        await callback.data.isdigit()


class IsDelBookmarkCallbackData(BaseFilter):
    async def __call__(self, callback: CallbackQuery):
        await callback.data.endswith('del') and callback.data[:-3].isdigit()
