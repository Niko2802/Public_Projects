import os
import random
import string
import asyncio
import logging
import configparser
from aiogram import Bot, Dispatcher, types, Router, F
from aiogram.filters.command import Command
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message


class Passw(StatesGroup):
    passw = State()


class Minutes(StatesGroup):
    min = State()


logging.basicConfig(level=logging.INFO)
config = configparser.ConfigParser()
config.read('TG_comp_tools.ini', encoding="utf8")
token_bot = config['Telegram']['Token']
bot = Bot(token=token_bot)
dp = Dispatcher()
autorization_code = ["28fev1980M07"]
router = Router()


def generate_password(length=8, complexity=2):
    if complexity == 1:
        characters = string.digits
    elif complexity == 2:
        characters = string.ascii_letters + string.digits
    elif complexity == 3:
        characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def change_password_current_user(new_password):
    login = os.getlogin()
    config['Password']['last_password'] = new_password
    with open('TG_comp_tools.ini', 'w', encoding="utf8") as configfile:
        config.write(configfile)
    return os.system(f"net user {login} {new_password}")


def declension_minutes(num):
    if num % 10 == 1 and num % 100 != 11: 
        return "минуту"
    elif 2 <= num % 10 <= 4 and (num % 100 < 10 or num % 100 >= 20):
        return "минуты"
    else:
        return "минут"
    

async def on_startup(_):
    await typing()
    for key in config:
        if key.isdigit():
            await bot.send_message(key, f"Компьютер включен.\nБот онлайн :)\n\nТекущий пароль {config['Password']['last_password']}")

def shutdown_computer(minutes=5):
    return os.system(f"shutdown /s /t {minutes}")

async def typing():
    for key in config:
        if key.isdigit():
            await bot.send_chat_action(key, action="TYPING")

@dp.message(Command("start"))
async def process_start_command(message: types.Message):
    if str(message.from_user.id) in config:
        kb = [
            [types.KeyboardButton(text="Создать новый пароль")],
            [types.KeyboardButton(text="Выключить компьютер")]
        ]
        keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
        await message.answer("Привет!\nЯ умею менять пароль на вход в Windows.\nУмею выключать компьютер.\nДля управления, выбери нужную кнопку.", reply_markup=keyboard)
    else:
        kb = [
            [types.KeyboardButton(text="Ввести пароль")]
        ]
        keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
        await message.answer("Вы не авторизованы!\nНажмите кнопку 'Ввести пароль'", reply_markup=keyboard)

@dp.message(StateFilter(None), F.text == "Ввести пароль")
async def input_password(message: Message, state: FSMContext):
    await message.answer(text="Введите пароль:")
    await state.set_state(Passw.passw)

@dp.message(Passw.passw, F.text.in_(autorization_code))
async def check_input_password(message: Message, state: FSMContext):
    await typing()
    await message.answer("Вы авторизованы!")
    await bot.delete_message(message.chat.id, message.message_id)
    config.add_section(str(message.from_user.id))
    config[str(message.from_user.id)
            ]['first_name'] = message.from_user.first_name
    config[str(message.from_user.id)
            ]['last_name'] = message.from_user.last_name
    config[str(message.from_user.id)
            ]['username'] = message.from_user.username
    with open('TG_comp_tools.ini', 'w', encoding="utf8") as configfile:
        config.write(configfile)
    await process_start_command(message)
    await state.clear()

@dp.message(Passw.passw)
async def password_incorrectly(message: Message):
    await typing()
    await message.answer(text="Пароль введен не верно.\n\n" "Введите пароль:")

@dp.message(F.text =="Создать новый пароль")
async def new_password(message: types.Message):
    await typing()
    password = generate_password(8, 2)
    res = change_password_current_user(password)
    if res == 0:
        for key in config:
            if key.isdigit():
                await bot.send_message(key, f"Пароль был изменен на:\n{password}")
    else:
        await message.answer("Пароль не изменен ", res)

@dp.message(StateFilter(None), F.text == "Выключить компьютер")
async def input_minutes(message: Message, state: FSMContext):
    await typing()
    await message.answer(text="Через сколько минут выключить компьютер?:")
    await state.set_state(Minutes.min)

@dp.message(Minutes.min, lambda message: message.text.isdigit())
async def check_minutes(message: Message, state: FSMContext):
    await typing()
    shutdown_computer(message.text)
    await message.answer(text=f"Компьютер будет выключен через {message.text} {declension_minutes(int(message.text))}")
    await state.clear()

@dp.message(Minutes.min)
async def minutes_incorrectly(message: Message):
    await typing()
    await message.answer(text="Нужно ввести число.\n\n" "Введите минуты:")

@dp.message(F.text)
async def nothing(message: types.Message):
    await typing()
    await message.answer(text="Компьютер работает!")


async def main():
    await on_startup(None)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())