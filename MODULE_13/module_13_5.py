from aiogram import Bot, types, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio

api = "................"

bot = Bot(token = api)
dp = Dispatcher(bot, storage = MemoryStorage())

kb = ReplyKeyboardMarkup(resize_keyboard = True)
button = KeyboardButton(text = 'Рассчитать')
button2 = KeyboardButton(text = 'Информация')
kb.add(button)
kb.add(button2)

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(commands=['start'])
async def start(message):
    await message.reply("Привет! Я бот помогающий твоему здоровью",reply_markup = kb)

@dp.message_handler(text='Рассчитать')
async def set_age(message):
    await message.reply('Введите свой возраст:')
    await UserState.age.set()

@dp.message_handler(text='Информация')
async def inform(message):
    await message.reply('Этот бот рассчитывает суточную норму каллорий для тебя')

@dp.message_handler(state=UserState.age)
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
    await message.reply(f'Ваша суточная норма калорий: {int((10 * int(data["age"])) + (6.25 * int(data["growth"])) - (5 * int(data["weight"])) +5)}')
    await state.finish()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

