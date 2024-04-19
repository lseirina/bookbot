
import asyncio
import logging
from aiogram import Bot, Dispatcher
from handlers import user_handler, other_handler
from config_data.config import Config, load_config
from keyboards.main_menu import set_main_menu


logger = logging.getlogger(__name__)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s'
    )
    logger.info('Starting bot')

    config: Config = load_config()
    bot = Bot(
        token=config.tg_bot.token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()

    await set_main_menu(bot)

    dp.include_router(user_handler)
    dp.include_router(other_handler)

    await bot.delete_web_hook(drop_pending_updates=True)
    await dp.start_polling(bot)

asyncio.run(main())
