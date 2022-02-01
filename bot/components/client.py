from aiogram import types, Dispatcher
from bot_init import dp, bot, config_request
from keyboards import client_kb
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from components.other import Managment, usr_ident
from keyboards import admin_kb
from aiogram.dispatcher.filters import Text

bot_conf = config_request("Dobromebel")

class Controller(StatesGroup):
    start = State()
    order = State()
    name = State()

#@dp.message_handler(commands = ['start', 'help'])
async def send_welcome(message : types.Message):
    # Бота можно добавить в группу и он может отвечать в личку или там, если ранее пользователь боту не писал
    global ID
    ID = message.from_user.id
    resp_api = await usr_ident(ID)
    if resp_api['stat'] == 0:
        try:
            await bot.send_message(message.from_user.id, bot_conf['start_message'], reply_markup = client_kb.start_kb)
            await message.delete()
            await Controller.start.set()
        except: await message.reply("Напиши сначала болу в ЛС")
    if resp_api['stat'] == 1:
        await message.answer('Выберете нужный раздел', reply_markup = admin_kb.manager_menu_kb)
        await Managment.step_2.set()

async def fist_step(message : types.Message, state : FSMContext):
    async with state.proxy() as data:
        data['start'] = message.text
    if data['start'] == 'Оставить заявку для связи с менеджером': 
        await Controller.next()
        await message.answer('Оставьте свои контакты и менеджер в скором времени свяжется с Вами', reply_markup = client_kb.contact_share)
    if data['start'] == 'Я сотрудник компании':
        await Managment.step_1.set()
        await message.answer('Введи пароль: ', reply_markup = ReplyKeyboardRemove())

async def get_contact(message : types.Message, state : FSMContext):
    async with state.proxy() as data:
        data['order'] = message.contact.phone_number
        data['name'] = message.contact.first_name
    await message.answer('Спасибо! Мы с Вами обязательно свяжемся!', reply_markup = ReplyKeyboardRemove())
    await state.finish()

def register_handlers(dp : Dispatcher):
    dp.register_message_handler(send_welcome, commands = ['start', 'help'])
    dp.register_message_handler(send_welcome, Text(equals = 'Главное меню', ignore_case = True), state = "*")
    dp.register_message_handler(fist_step, state = Controller.start)
    dp.register_message_handler(get_contact, content_types = 'contact', state = Controller.order)