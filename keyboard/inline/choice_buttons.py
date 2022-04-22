from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import URL_Real, URL_Barcelona, URL_ManCity, URL_Chelsea
from keyboard.inline.callback_dates import buy_callback

choice = InlineKeyboardMarkup(row_width=2)

buy_pear = InlineKeyboardButton(text="Man City", callback_data=buy_callback.new(item_name="Man City", quantity=1))
choice.insert(buy_pear)

buy_apples = InlineKeyboardButton(text="Barcelona", callback_data="buy:Barcelona:5")
choice.insert(buy_apples)

buy_apples = InlineKeyboardButton(text="Real Madrid", callback_data="buy:Real Madrid:5")
choice.insert(buy_apples)

buy_apples = InlineKeyboardButton(text="Chelsea", callback_data="buy:Chelsea:5")
choice.insert(buy_apples)

cancel_button = InlineKeyboardButton(text="Cancel", callback_data="cancel")
choice.insert(cancel_button)

pear_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Visit", url=URL_ManCity)
    ]
])
apples_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="visit", url=URL_Barcelona)
    ]
])
apples_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="visit", url=URL_Real)
    ]
])
apples_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="visit", url=URL_Chelsea)
    ]
])