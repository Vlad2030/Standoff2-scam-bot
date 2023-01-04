# SO2 SCAM BOT BY github.com/Vlad2030


from modules import donate
from modules import text
from aiogram import types

def BuyKeyboard():
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        types.InlineKeyboardButton(
            text=text.buy1_keyboard_text,
            callback_data='callback_buy1'
        ),
        types.InlineKeyboardButton(
            text=text.buy2_keyboard_text,
            callback_data='callback_buy2'
        ),
        types.InlineKeyboardButton(
            text=text.buy3_keyboard_text,
            callback_data='callback_buy3'
        ),
        types.InlineKeyboardButton(
            text=text.buy4_keyboard_text,
            callback_data='callback_buy4'
        )
    )
    return keyboard

def Buy1LinkKeyboard():
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        types.InlineKeyboardButton(
            text=text.buy1_keyboard_text,
            url=donate.donate_link
        ),
        types.InlineKeyboardButton(
            text=text.menu_text,
            callback_data='callback_menu'
        )
    )
    return keyboard

def Buy2LinkKeyboard():
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        types.InlineKeyboardButton(
            text=text.buy2_keyboard_text,
            url=donate.donate_link
        ),
        types.InlineKeyboardButton(
            text=text.menu_text,
            callback_data='callback_menu'
        )
    )
    return keyboard

def Buy3LinkKeyboard():
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        types.InlineKeyboardButton(
            text=text.buy3_keyboard_text, 
            url=donate.donate_link
        ),
        types.InlineKeyboardButton(
            text=text.menu_text,
            callback_data='callback_menu'
        )
    )
    return keyboard

def Buy4LinkKeyboard():
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        types.InlineKeyboardButton(
            text=text.buy4_keyboard_text,
            url=donate.donate_link
        ),
        types.InlineKeyboardButton(
            text=text.menu_text,
            callback_data='callback_menu'
        )
    )
    return keyboard