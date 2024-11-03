from aiogram import Bot, types, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

api = "....."

bot = Bot(token = api)
dp = Dispatcher(bot, storage = MemoryStorage())

# kb = ReplyKeyboardMarkup(resize_keyboard = True)
# button = KeyboardButton(text = 'Рассчитать')
# button2 = KeyboardButton(text = 'Информация')
# kb.add(button)
# kb.add(button2)

kb = InlineKeyboardMarkup()
button1 = InlineKeyboardButton(text = 'Рассчитать норму калорий',
                              callback_data='calories')
kb.add(button1)

button2 = InlineKeyboardButton(text = 'Формулы расчёта',
                               callback_data='formulas')
kb.add(button2)

# Inline_menu = ReplyKeyboardMarkup(
#     keyboard=[
#     [KeyboardButton(text = '1')],
#     [KeyboardButton(text = '2')],
#     [KeyboardButton(text = '3')]],
#     resize_keyboard = True
# )

@dp.message_handler(text = "Рассчитать")
async def main_menu(message):
    await message.answer("Выберите опцию:", reply_markup = kb)

@dp.callback_query_handler(text = 'formulas')
async def get_formulas(call):
    await call.message.answer('10 x вес(кг) + 6,25 x рост(см) - 5 х возраст(г) - 161')

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(commands=['start'])
async def start(message):
    await message.reply("Привет! Я бот помогающий твоему здоровью")

@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()

@dp.message_handler(text='Информация')
async def inform(message):
    await message.reply('Этот бот рассчитывает суточную норму каллорий для тебя')

@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.reply('Введите свой рост:')
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
    await message.reply(f'Ваша суточная норма калорий: {int((10 * int(data["weight"])) + (6.25 * int(data["growth"])) - (5 * int(data["age"])) +5)}')
    await state.finish()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

