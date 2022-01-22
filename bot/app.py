from aiogram.utils import executor
from bot_init import dp
from components import client, admin, other

async def start(_):
    print('Бот онлайн')

admin.register_handlers_user_reg(dp)
client.register_handlers(dp)
other.register_handlers_managment(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates = True, on_startup = start)