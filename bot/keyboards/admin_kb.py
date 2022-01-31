from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

# Клавиатура для выбора пола gender_kb
gender_kb = ReplyKeyboardMarkup(resize_keyboard = True)
gender_kb_b1 = KeyboardButton('муж')
gender_kb_b2 = KeyboardButton('жен')
gender_kb.add(gender_kb_b1).insert(gender_kb_b2)

# Кнопка "Главное меню"

default_kb = ReplyKeyboardMarkup(resize_keyboard = True).add(KeyboardButton('Главное меню'))

# Меню сотрудника
manager_menu_kb = ReplyKeyboardMarkup(resize_keyboard = True)
manager_menu_kb_b1 = KeyboardButton('Личный кабинет')
manager_menu_kb_b2 = KeyboardButton('Обращение в поддержку')
manager_menu_kb_b3 = KeyboardButton('Проекты')
manager_menu_kb.add(manager_menu_kb_b1).insert(manager_menu_kb_b2).add(manager_menu_kb_b3)

# Меню управления проектами
proj_managment_kb = ReplyKeyboardMarkup(resize_keyboard = True)
proj_managment_kb_b1 = KeyboardButton('Добавить новый проект')
proj_managment_kb_b2 = KeyboardButton('Редавтировать существующий проект')
proj_managment_kb.add(proj_managment_kb_b1).add(proj_managment_kb_b2)

# Да/Нет
yes_no_kb = ReplyKeyboardMarkup(resize_keyboard = True)
yes_no_kb_b1 = KeyboardButton('Да')
yes_no_kb_b2 = KeyboardButton('Нет')
yes_no_kb.add(yes_no_kb_b1).insert(yes_no_kb_b2)

# Выбор должности
async def position_choise(data):
    position_choise_kb = InlineKeyboardMarkup(row_width = 2)
    pc_kb_b = []
    for i in range(data['positions']['pos_counter'] - 2):
        content = data['positions'][str(i + 3)]
        pc_kb_b.append(InlineKeyboardButton(content, callback_data = str(i)))
        position_choise_kb.add(pc_kb_b[i])
    return position_choise_kb

# Выбор проекта
async def project_choise(data):
    project_choise_kb = InlineKeyboardMarkup(row_width = 2)
    proj_choise_kb_b = []
    for i in range(data['projects']['projects_counter']):
        content = data['projects'][str(i + 1)]['name']
        proj_choise_kb_b.append(InlineKeyboardButton(content, callback_data = str(i + 1)))
        project_choise_kb.add(proj_choise_kb_b[i])
    return project_choise_kb

#  Поля для редактирования проекта
async def proj_attributes(data, proj_id):
    proj_attributes_kb = InlineKeyboardMarkup(row_width = 2)
    proj_attributes_b = []
    i = 0
    for attr in data['projects'][str(proj_id)].items():
        content = str(attr[0]) + ' : ' + str(attr[1])
        proj_attributes_b.append(InlineKeyboardButton(content, callback_data = str(i)))
        proj_attributes_kb.add(proj_attributes_b[i])
        i += 1
    return proj_attributes_kb