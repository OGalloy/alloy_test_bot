from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from keyboard.keyboard import markup


from config import TOKEN




bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands =["start"])
async def cmd_start(message: types.Message):
    await message.answer("MENU", reply_markup = markup.keyboard)

@dp.callback_query_handler(lambda callback_query: "button_profile_push")
async def button_profile_answer(callback_query: types.CallbackQuery):
    await callback_query.answer("you push \'profile\' button") 


if __name__ == '__main__':
    executor.start_polling(dp)