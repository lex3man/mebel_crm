from datetime import date
from aiogram import types, Dispatcher
from bot_init import dp, bot
from keyboards import admin_kb
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
import aiohttp

ID = None

class User(StatesGroup):
    name = State()
    birthdate = State()
    teleg = State()
    gender = State()
    position = State()
    ID = State()

class Project(StatesGroup):
    caption = State()
    name = State()
    description = State()
    manager = State()
    designerless = State()
    discount = State()
    map_price = State()
    construct = State()
    shipping = State()
    up_shipping = State()
    additional_tools = State()
    total_price = State()

class Managment(StatesGroup):
    step_1 = State()
    step_2 = State()
    step_3 = State()
    step_4 = State()
    step_5 = State()
    proj_manage = State()

# Функции обращения к API системы

async def get_positions():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://152.67.75.74/crm/main_data/') as resp:
            response = await resp.json()
            return(response)

async def usr_ident(usr_id):
    async with aiohttp.ClientSession() as session:
        async with session.post('http://152.67.75.74/crm/sets_api/', json = {'ID':usr_id, 'head':'user_ident'}) as resp:
            response = await resp.json()
            return(response)

async def new_user(usr):
    usr.update({'head':'new_user'})
    async with aiohttp.ClientSession() as session:
        async with session.post('http://152.67.75.74/crm/sets_api/', json = usr) as resp:
            response = await resp.json()
            return(response)

async def new_project(prjt):
    prjt.update({'head':'new_proj'})
    async with aiohttp.ClientSession() as session:
        async with session.post('http://152.67.75.74/crm/sets_api/', json = prjt) as resp:
            response = await resp.json()
            return(response)

# Функции регистрации польователя

async def save_name(message : types.Message, state : FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await User.next()
    await message.answer('Дата Вашего рождения')

async def save_bdate(message : types.Message, state : FSMContext):
    async with state.proxy() as data:
        data['birthdate'] = message.text
    await User.gender.set()
    await message.answer('Укажите свой пол', reply_markup = admin_kb.gender_kb)

async def save_gender(message : types.Message, state : FSMContext):
    async with state.proxy() as data:
        data['gender'] = message.text
        data['teleg'] = message.from_user.username
        data['ID'] = message.from_user.id
    await User.next()
    resp_api = await get_positions()
    keyboard = await admin_kb.position_choise(resp_api)
    await message.answer('Хорошо!', reply_markup = ReplyKeyboardRemove())
    await message.answer('Теперь выберите свою должность:', reply_markup = keyboard)

async def save_position(callback_query : types.CallbackQuery, state : FSMContext):
    async with state.proxy() as data:
        data['position'] = callback_query.data
        resp_api = await new_user(data._data)
    await callback_query.answer(resp_api['msg'] + 'Дождитесь назначения уровня доступа')
    await bot.send_message(callback_query.from_user.id, text = 'Спасибо, Вы зарегистрированны!', reply_markup = admin_kb.default_kb)
    await state.finish()

# Отмена процесса

async def cancel_handler(message : types.Message, state : FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.answer('Ok')

# Проверка  пароля сотрудника

async def get_pass(message : types.Message, state : FSMContext):
    async with state.proxy() as data:
        data['step_1'] = message.text
    if data['step_1'] == '12345':
        global ID
        ID = message.from_user.id
        resp_api = await usr_ident(ID)
        if resp_api['stat'] == 0:
            await User.name.set()
            await message.answer(resp_api['msg'] + 'Давайте сначала зарегистрируемся.')
            await message.answer('Введите своё имя')
        if resp_api['stat'] == 1:
            await Managment.next()
            await message.answer('Выберите нужный раздел', reply_markup = admin_kb.manager_menu_kb)
    else: await message.answer('Пароль неверный, попробуйте ещё раз')

async def staff_second_level_menu(message : types.Message, state : FSMContext):
    async with state.proxy() as data:
        data['step_2'] = message.text
    if data['step_2'] == 'Проекты':
        await Managment.proj_manage.set()
        await message.answer('Раздел проекты', reply_markup = admin_kb.proj_managment_kb)

# Функции добавления нового проекта

async def add_proj(message : types.Message, state : FSMContext):
    await Project.name.set()
    await message.answer('Название проекта', reply_markup = ReplyKeyboardRemove())

async def save_proj_name(message : types.Message, state : FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await Project.next()
    await message.answer('Теперь опишите этот проект своими словами')

async def save_proj_description(message : types.Message, state : FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
    await Project.designerless.set()
    await message.answer('Делаем скидку 10% по промо (толлько если нет заинтересованного дизайнера)', reply_markup = admin_kb.yes_no_kb)

async def designerless_check(message : types.Message, state : FSMContext):
    async with state.proxy() as data:
        data['designerless'] = 2
        if message.text == 'Да': 
            data['designerless'] = 1
    await Project.construct.set()
    await message.answer('Сборка нужна будет?', reply_markup = admin_kb.yes_no_kb)
    
async def construct_check(message : types.Message, state : FSMContext):
    async with state.proxy() as data:
        data['construct'] = 2
        if message.text == 'Да': 
            data['construct'] = 1
    await Project.next()
    await message.answer('А доставка?', reply_markup = admin_kb.yes_no_kb)

async def shipping_check(message : types.Message, state : FSMContext):
    async with state.proxy() as data:
        data['shipping'] = 2
        if message.text == 'Да': 
            data['shipping'] = 1
    await Project.next()
    await message.answer('С подъёмом?', reply_markup = admin_kb.yes_no_kb)

async def upshipping_check(message : types.Message, state : FSMContext):
    async with state.proxy() as data:
        data['up_shipping'] = 2
        if message.text == 'Да': 
            data['up_shipping'] = 1
    await Project.next()
    await message.answer('Дополнительная техника будет в заказе? (можно будет добавить потом)', reply_markup = admin_kb.yes_no_kb)

async def additional_tools_check(message : types.Message, state : FSMContext):
    if message.text == 'Да':
        await message.answer('Выберете дополнительную технику:', reply_markup = ReplyKeyboardRemove())
        resp_api = await get_positions()
        for i in range(resp_api['tools']['tool_counter']):
            content = 'Вариант ' + str(i + 1) + ': ' + resp_api['tools'][str(i + 1)]
            await message.answer(content)
        await message.answer('Напиши номера вариантов через запятую')
    elif message.text == 'Нет':
        async with state.proxy() as data:
            data['additional_tools'] = 0
        await Project.total_price.set()
        await message.answer('Введи расчётную стоимость проекта', reply_markup = ReplyKeyboardRemove())
    else:
        async with state.proxy() as data:
            data['additional_tools'] = str(message.text)
        await Project.total_price.set()
        await message.answer('Введи расчётную стоимость проекта', reply_markup = ReplyKeyboardRemove())

async def add_new_proj(message : types.Message, state : FSMContext):
    async with state.proxy() as data:
        data['total_price'] = float(message.text)
        caption = data['name'] + ' / ' + str(data['total_price']) + ' руб. / ' + str(date.today())
        data['caption'] = caption
        data['manager'] = str(message.from_user.id)
        await message.answer(data._data)
        resp_api = await new_project(data._data)
    await state.finish()
    await message.answer('OK. ' + resp_api['msg'], reply_markup = admin_kb.default_kb)

# Регистрация хедлеров

def register_handlers_managment(dp : Dispatcher):

    dp.register_message_handler(cancel_handler, Text(equals = 'отмена', ignore_case = True), state = "*")

    dp.register_message_handler(get_pass, state = Managment.step_1)
    dp.register_message_handler(staff_second_level_menu, state = Managment.step_2)
    dp.register_message_handler(add_proj, Text(equals = 'Добавить новый проект'), state = Managment.proj_manage)

    dp.register_message_handler(save_proj_name, state = Project.name)
    dp.register_message_handler(save_proj_description, state = Project.description)
    dp.register_message_handler(designerless_check, state = Project.designerless)
    dp.register_message_handler(construct_check, state = Project.construct)
    dp.register_message_handler(shipping_check, state = Project.shipping)
    dp.register_message_handler(upshipping_check, state = Project.up_shipping)
    dp.register_message_handler(additional_tools_check, state = Project.additional_tools)
    dp.register_message_handler(add_new_proj, state = Project.total_price)

    dp.register_message_handler(save_name, state = User.name)
    dp.register_message_handler(save_bdate, state = User.birthdate)
    dp.register_message_handler(save_gender, state = User.gender)
    dp.register_callback_query_handler(save_position, state = User.position)