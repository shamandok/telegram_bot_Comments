import logging

from aiogram import Bot, Dispatcher, executor, types
from src import keyboard, comments_API
import config
import emoji



logging.basicConfig(level=logging.INFO)


bot = Bot(token=config.MY_BOT_API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler()
async def send_welcome(message: types.Message):
    answer = 'Опубліковано'
    comments_link = comments_API.create_post(message.text, message.from_user.id, config.COMMENTS_BOT_API_TOKEN)
    try:
        await bot.send_message(chat_id='@chanel_13V', text=message.text, reply_markup=keyboard.create_Inline_Keyboard(comments_link))
    except Exception as ex:
        answer = 'Виникла проблема: '+ str(ex)
    await message.answer(answer)



@dp.callback_query_handler(lambda c: c.data and c.data.startswith('btn'))
async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
    code = callback_query.data[-1]
    if code.isdigit():
        code = int(code)
    if code == 2:
        new_markup = callback_query.message.reply_markup
        emj, count = new_markup['inline_keyboard'][1][0]['text'].split(' ')
        new_markup['inline_keyboard'][1][0]['text'] = emj + ' ' + str(int(count) + 1)
        await bot.edit_message_reply_markup(chat_id='@chanel_13V', message_id=callback_query.message.message_id, reply_markup=new_markup)
    if code == 3:
        new_markup = callback_query.message.reply_markup
        emj, count = new_markup['inline_keyboard'][1][1]['text'].split(' ')
        new_markup['inline_keyboard'][1][1]['text'] = emj + ' ' + str(int(count) + 1)
        await bot.edit_message_reply_markup(chat_id='@chanel_13V', message_id=callback_query.message.message_id, reply_markup=new_markup)





if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)