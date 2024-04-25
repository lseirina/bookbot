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
from services.file_handling import book


router = Router()


@router.message(CommandStart)
async def process_start_command(message: Message):
    await message.answer(LEXICON[message.text])
    if message.from_user.id not in user_db:
        user_db[message.from_user.id] = deepcopy(user_dict_templates)


@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(LEXICON[message.text])


@router.message(Command(commands='beginning'))
async def process_beginning_command(message: Message):
    user_db[message.from_user.id]['page'] = 1
    text = book[user_db[message.from_user.id]['page']]
    await message.answer(
        text=text,
        reply_markup=create_pagination_keyboard(
            'backward',
            f'{user_db[message.from_user.id]["page"]}/len(book)',
            'forward'
        )
    )


@router.message(Command(commands='continue'))
async def process_continue_command(message: Message):
    text = book[user_db[message.from_user.id]['page']]
    await message.answer(
        text=text,
        reply_markup=create_pagination_keyboard(
            'backward',
            f'{user_db[message.from_user.id]["page"]}/{len(book)}',
            'forward',
        ),
    )

