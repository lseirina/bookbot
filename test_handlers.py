import unittest
from unittest import IsolatedAsyncioTestCase
from unittest.mock import MagicMock, AsyncMock, patch

from lexicon.lexicon import LEXICON
from aiogram.types import Message
from handlers.user_handlers import router
import database


class UserHandlerTest(IsolatedAsyncioTestCase):

    async def test_start_command(self):
        message = MagicMock()
        message.test = '/start'
        message.answer = AsyncMock()

        await router.process_start_command(message)
        message.answer.assert_called_with(LEXICON['/start'])
        print("Тест test_start_command успешно пройден!")

    async def test_bookmark_command(self):
        message = MagicMock()
        message.from_user.id = 123
        message.text = '/bookmarks'
        message.answer = AsyncMock()
        user_db = {123: {'bookmarks': [1, 2, 3]}}
        with patch(database.user_db, user_db):
            await router.process_bookmark_command(message)
            message.answer.assert_called_with('This the list of your bookmarks:\n1\n2\n3')


if __name__ == "__main__":
    unittest.main()
