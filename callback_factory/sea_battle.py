import copy

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message
)
from aiogram.filters.callback_data import CallbackData


BOT_TOKEN = '6883498485:AAGtOZFurG3T-H2oDNwhQcUqeUzlMfqcJHE'
bot = Bot(BOT_TOKEN)
dp = Dispatcher()


FIELD_SIZE = 8

LEXICON = {
    '/start': 'Вот твое поле. Можешь делать ход',
    0: ' ',
    1: '🌊',
    2: '💥',
    'miss': 'Мимо!',
    'hit': 'Попал!',
    'used': 'Вы уже стреляли сюда!',
    'next_move': 'Делайте ваш следующий ход'
}

users: dict[int, dict[str, list]] = {}

ships: list[list[int]] = [
    [1, 0, 1, 1, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0]
]


class FieldCallbackFactory(CallbackData, prifix='user_field'):
    x: int
    y: int


def reset_field(user_id: int) -> None:
    users[user_id]['ships'] = copy.deepcopy(ships)
    users[user_id]['filds'] = [
# The loop [0 for _ in range(FIELD_SIZE)] for _ in range(FIELD_SIZE) is
# a nested list comprehension
        [0 for _ in range(FIELD_SIZE)]
        for _ in range(FIELD_SIZE)
    ]
