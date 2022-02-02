from aiogram import types, Dispatcher
from aiogram.types import ReplyKeyboardRemove
from bot_init import dp, bot
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards import admin_kb
from aiogram.dispatcher.filters import Text
import aiohttp
from components.other import User, Project, usr_ident

ID = None

# Функции обращения к API системы
async def new_contact(data):
    data.update({'head':'new_client'})
    async with aiohttp.ClientSession() as session:
        async with session.post('http://152.67.75.74/crm/sets_api/', json = data) as resp:
            response = await resp.json()
            return(response)

# Функции определения прав доступа

async def new_client(message : types.Message):
    content = message.text
    words_list = content.splitlines()
    contact_data = {'name':'Заявка на квиз'}
    phone_number = words_list[2].split()[-1]
    contact_data.update({'phone':phone_number})
    contact_data.update({'type':'U'})
    if words_list[words_list.index('Какой тип кухни интересует') + 1] == 'Угловая': contact_data.update({'type':'C'})
    if words_list[words_list.index('Какой тип кухни интересует') + 1] == 'П образная': contact_data.update({'type':'P'})
    if words_list[words_list.index('Какой тип кухни интересует') + 1] == 'Прямая': contact_data.update({'type':'L'})
    if words_list[words_list.index('Какой тип кухни интересует') + 1] == 'Островная': contact_data.update({'type':'I'})
    contact_data.update({'material':words_list[words_list.index('Вы уже выбрали материал фасадов?') + 1]})
    contact_data.update({'time':words_list[words_list.index('Планируемое время заказа кухни?') + 1]})
    contact_data.update({'pay':words_list[words_list.index('Как вы бы хотели оплатить кухню?') + 1]})
    contact_data.update({'present':words_list[words_list.index('Выберете свой подарок') + 1]})
    #await bot.send_message(message.from_user.id, str(contact_data))
    resp_api = await new_contact(contact_data)

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
    dp.register_message_handler(new_client, Text(contains = 'Заявка на квиз', ignore_case = True))
    dp.register_message_handler(sudo_start, commands = ['sudo'], state = None)