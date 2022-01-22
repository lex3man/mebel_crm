from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


test_kb = ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True)
b1 = KeyboardButton('/start')
b2 = KeyboardButton('/sudo')
b3 = KeyboardButton('Показать где я', request_location = True)
b4 = KeyboardButton('Поделиться своим контактом', request_contact = True)
test_kb.add(b1).insert(b2).add(b3).insert(b4)

# Клавиатура для выбора пола gender_kb
gender_kb = ReplyKeyboardMarkup(resize_keyboard = True)
gender_kb_b1 = KeyboardButton('муж')
gender_kb_b2 = KeyboardButton('жен')
gender_kb.add(gender_kb_b1).insert(gender_kb_b2)

# Старктовая клавиатура бота
start_kb = ReplyKeyboardMarkup(resize_keyboard = True)
start_kb_b1 = KeyboardButton('Оставить заявку для связи с менеджером')
start_kb_b2 = KeyboardButton('Я сотрудник компании')
start_kb.add(start_kb_b1).add(start_kb_b2)

# Кнопка "поделиться контактом"
contact_share = ReplyKeyboardMarkup(resize_keyboard = True)
contact_share.add(b4)