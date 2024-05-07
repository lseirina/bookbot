from unittest import IsolatedAsyncioTestCase
from unittest.mock import MagicMock, AsyncMock

from lexicon.lexicon import LEXICON
from aiogram.types import Message
from handlers.user_handlers import router


class UserHandlerTest(IsolatedAsyncioTestCase):

    async def test_start_command(self):
        message = Message(text='/start')
        message.answer = AsyncMock()

        await router.procces_start_command(message)
        message.answer.assert_called_with(LEXICON['/start'])
