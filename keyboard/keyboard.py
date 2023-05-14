#inline keyboard

from aiogram.types import InlineKeyboardMarkup
from aiogram.types import InlineKeyboardButton


class InlineButton(InlineKeyboardButton):
    def __init__(self, button_text, callback_data):
        super().__init__(text = button_text, callback_data = callback_data, parse_mode="HTML")



#buttons
profile_button = InlineButton(button_text = "profile", callback_data = "button_profile")
marathons_button = InlineButton(button_text = "marathons", callback_data = "button_marathons")
#help_button = InlineButton(button_text = "help", callback_data = "button_help")
back_button = InlineButton(button_text = "back", callback_data = "button_back")

#markups
#main menu
main_menu = InlineKeyboardMarkup()
main_menu.add(profile_button)
main_menu.add(marathons_button)

#profile
profile_menu = InlineKeyboardMarkup()
profile_menu.add(back_button)

#marathons
marathons_menu = InlineKeyboardMarkup()
marathons_menu.add(back_button)
