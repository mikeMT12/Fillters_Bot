import logging
from aiogram import executor
from loader import dp
import handlers

if __name__ == "__main__":
    # Включаем логирование, чтобы не пропустить важные сообщения
    logging.basicConfig(level=logging.DEBUG)
    # Запуск бота
    executor.start_polling(dispatcher=dp,
                           skip_updates=True)
