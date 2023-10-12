from config import BOT_TOKEN
from aiogram import Bot, Dispatcher

# Объект бота
bot = Bot(token=BOT_TOKEN,
          parse_mode='HTML')

# Диспетчер для бота
dp = Dispatcher(bot)

DOWNLOAD_FOLDER = './downloads'