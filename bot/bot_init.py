from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import requests

def config_request(bot_name):
    config = requests.post('http://152.67.75.74/crm/sets_api/', json = {"head":"bot_config", "bot_name":bot_name})
    return config.json()
bot_conf = config_request("Dobromebel")

bot = Bot(token = bot_conf["TOKEN"])
dp = Dispatcher(bot, storage = MemoryStorage())