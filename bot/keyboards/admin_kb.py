from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Клавиатура для выбора пола gender_kb
gender_kb = ReplyKeyboardMarkup(resize_keyboard = True)
gender_kb_b1 = KeyboardButton('муж')
gender_kb_b2 = KeyboardButton('жен')
gender_kb.add(gender_kb_b1).insert(gender_kb_b2)

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