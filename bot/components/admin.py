from aiogram import types, Dispatcher
from aiogram.types import ReplyKeyboardRemove
from bot_init import dp
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards import admin_kb
import aiohttp
from components.other import User, Project, usr_ident

ID = None

# Функции определения прав доступа

async def sudo_start(message : types.Message):
    global ID
    ID = message.from_user.id
    resp_api = await usr_ident(ID)
    if resp_api['stat'] == 0:
        await User.name.set()
        await message.answer(resp_api['msg'] + 'Давайте сначала зарегистрируемся.')
        await message.answer('Введите своё имя')
    if resp_api['stat'] == 1:
        await message.answer(resp_api['msg'] + 'У Вас нет прав администратора')
    if resp_api['stat'] == 100:
        await message.answer('ok')

def register_handlers_user_reg(dp : Dispatcher):
    dp.register_message_handler(sudo_start, commands = ['sudo'], state = None)