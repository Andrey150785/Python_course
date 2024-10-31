import asyncio
from aiogram import Bot, types, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup

api = '7476203530:AAF5Q7A-NvIFtUd8jftEZGuwoWNXcn_2W3s'
bot = Bot(token= api)
dp = Dispatcher(bot, storage=MemoryStorage())

class UserState(StatesGroup):
    name = State()
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(commands=['start'])
async def start(message):
    await message.reply("Привет! Я бот помогающий твоему здоровью.")

# @dp.message_handler()
# async def all_message(message):
#     await message.reply("Введите команду /start, чтобы начать общение.")

@dp.message_handler(text='Calories')
async def set_age(message):
    await message.reply('Введите свой возраст:')
    await UserState.age.set()

@dp.message_handler(state= UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.reply('Введите свою рост:')
    await UserState.growth.set()

@dp.message_handler(state= UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.reply('Введите свой вес:')
    await UserState.weight.set()

@dp.message_handler(state= UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    await message.reply(f'Ваша суточная норма калорий: {int((10 * data["weight"]) + (6.25 * data["growth"]) - (5 * data["age"]) - 161)}')

    await state.finish()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)