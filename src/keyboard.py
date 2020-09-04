from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton, \
    LoginUrl

import emoji


def __create_btn_for_comments(url):
    return InlineKeyboardButton('Коментарии', login_url=LoginUrl(url = url,bot_username='@CommentsBot', request_write_access=True ))

def __create_btn_for_likes(likes = 0, dislikes = 0):
    left_button = InlineKeyboardButton(emoji.emojize(':thumbsup:', use_aliases=True) + ' ' + str(likes), callback_data='btn2')
    right_button = InlineKeyboardButton(emoji.emojize(':-1:', use_aliases=True) + ' ' + str(dislikes), callback_data='btn3')
    return left_button, right_button


def create_Inline_Keyboard(url):
    button_for_comments = __create_btn_for_comments(url)
    left_button, right_button = __create_btn_for_likes()
    
    
    keyboard = InlineKeyboardMarkup(row_width=2).add(button_for_comments)
    keyboard.add(left_button, right_button)
    return keyboard
