from aiogram import types, Dispatcher, Bot


async def cmd_start(message: types.Message):
    poll_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    poll_keyboard.add(types.KeyboardButton(text="Создать викторину",
                                           request_poll=types.KeyboardButtonPollType(type=types.PollType.REGULAR)))
    poll_keyboard.add(types.KeyboardButton(text="Cancel"))
    await message.answer("Нажмите на кнопку ниже и создайте викторину!", reply_markup=poll_keyboard)


async def action_cancel(message: types.Message):
    remove_keyboard = types.ReplyKeyboardRemove()
    await message.answer(
        "Действие отменено. Введите /start, чтобы начать заново.", reply_markup=remove_keyboard)


async def send_photo(bot: Bot, message: types.Message):
    await bot.send_photo(chat_id=message.chat.id,
                         photo="https://images.unsplash.com/"
                               "photo-1508921912186-1d1a45ebb3c1?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8cGhvdG98ZW58MHx8MHx8&w=1000&q=80")


def register_client_handlers(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands=["start"])

    cancel_filter = lambda message: message.text == "Cancel"
    dp.register_message_handler(action_cancel, cancel_filter)

    dp.register_message_handler(lambda message: send_photo(dp.bot, message), commands=['photo'])
