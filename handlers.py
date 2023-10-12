from aiogram import types
import aiogram.utils.markdown as fmt
from loader import dp, DOWNLOAD_FOLDER
from filters import ChatIdFilter

@dp.message_handler(ChatIdFilter(1463229321))
async def send_spec(message: types.Message):
    await message.answer("Только для тебя")

@dp.message_handler(text='Привет')
async def greet_user(message: types.Message):
    await message.reply(f"Привет <i>{message.from_user.full_name}!</i>")

@dp.message_handler(text='Цена')
async def cmd_test1(message: types.Message):
   await message.answer(
       fmt.text(
           fmt.text(fmt.hunderline("Яблоки"), ", вес 1 кг."),
           fmt.text("Старая цена:", fmt.hstrikethrough(50), "рублей"),
           fmt.text("Новая цена:", fmt.hbold(25), "рублей"),
           fmt.text("AAAAA:", fmt.hspoiler(50), "рублей"),
           sep="\n"
       ), parse_mode="HTML"
   )


