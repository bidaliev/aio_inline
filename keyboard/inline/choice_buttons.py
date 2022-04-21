from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import URL_JIHC, URL_APPLE
from keyboard.inline.callback_dates import buy_callback

choice = InlineKeyboardMarkup(row_width=2)

buy_pear = InlineKeyboardButton(text="College site", callback_data=buy_callback.new(item_name="pear", quantity=1))
choice.insert(buy_pear)

buy_apples = InlineKeyboardButton(text="Apple", callback_data="buy:apple:5")
choice.insert(buy_apples)

cancel_button = InlineKeyboardButton(text="Cancel", callback_data="cancel")
choice.insert(cancel_button)

pear_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Visit", url=URL_JIHC)
    ]
])
apples_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="visit", url=URL_APPLE)
    ]
])