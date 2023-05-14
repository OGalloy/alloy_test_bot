from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.utils import executor
from keyboard.keyboard import main_menu, profile_menu, marathons_menu


from config import TOKEN


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

#print(bot.get_chat())

@dp.callback_query_handler(Text("button_profile"))
async def button_profile_answer(callback_query: types.CallbackQuery):
    await bot.delete_message(chat_id = callback_query["message"]["chat"]["id"], message_id = callback_query["message"]["message_id"])
    await bot.send_message(chat_id = callback_query["from"]["id"], text= "profile", reply_markup=profile_menu)

#lambda callback_query: "button_marathons"
@dp.callback_query_handler(Text("button_marathons"))
async def button_marathons_answer(callback_query: types.CallbackQuery):
    await bot.delete_message(chat_id = callback_query["message"]["chat"]["id"], message_id = callback_query["message"]["message_id"])
    await bot.send_message(chat_id = callback_query["from"]["id"], text= "marathons", reply_markup= marathons_menu)

@dp.callback_query_handler(Text("button_back"))
async def button_back_answer(callback_query: types.CallbackQuery):
    await bot.delete_message(chat_id = callback_query["message"]["chat"]["id"], message_id = callback_query["message"]["message_id"])
    await bot.send_message(chat_id = callback_query["from"]["id"], text= "menu", reply_markup=main_menu)



@dp.message_handler(commands =["start"])
async def cmd_start(message: types.Message):
    await message.answer("menu", reply_markup = main_menu)




if __name__ == '__main__':
    executor.start_polling(dp)