from copy import deepcopy

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import (
    Command,
    CommandStart,
)
from filters.filters import (
    IsDigitCallbackData,
    IsDelBookmarkCallbackData,
)
from keyboards.pagination_kb import create_pagination_keyboard
from keyboards.bookmarks_kb import (
    create_bookmarks_keyboard,
    create_edit_keyboard,
)
from database.database import user_db, user_dict_templates
from lexicon.lexicon import LEXICON


router = Router()

@router.message(CommandStart)
async def process_start_command(message: Message):
    await message.answer(LEXICON[message.text])
    if message.from_user.id not in user_db:
        user_db[message.from_user.id] = deepcopy(user_dict_templates)
