#inline keyboard

from aiogram.types import InlineKeyboardMarkup
from aiogram.types import InlineKeyboardButton


#class constructor for inline keyboards
class InlineKeyboard(InlineKeyboardMarkup):
    def __init__(self, button_list: list):
        self.keyboard = InlineKeyboardMarkup()
        for button in button_list:
            self.keyboard.add(button)

#list of inline buttons
buttons = [InlineKeyboardButton(text = "profile", callback_data = "button_profile"),
            InlineKeyboardButton(text = "marathons", callback_data = "button_marathons"),
            InlineKeyboardButton(text = "help", callback_data = "button_help")]
markup = InlineKeyboard(buttons)

#markup = InlineKeyboardMarkup()
#markup.add(InlineKeyboardButton(text = "button_profile", callback_data = "button_profile_push"))
