from aiogram import Bot, types, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
from crud_functions import *


api = "7476203530:AAF5Q7A-NvIFtUd8jftEZGuwoWNXcn_2W3s"

bot = Bot(token = api)
dp = Dispatcher(bot, storage = MemoryStorage())
products = get_all_products()

kb = ReplyKeyboardMarkup()
button1 = KeyboardButton(text = 'Рассчитать')
kb.add(button1)
button2 = KeyboardButton(text = 'Информация')
kb.add(button2)
button3 = KeyboardButton(text = 'Купить')
kb.add(button3)
button4 = KeyboardButton(text = 'Регистрация')
kb.add(button4)


Button_menu = InlineKeyboardMarkup()
Button_menu.add(InlineKeyboardButton(text = 'Product1', callback_data='product_buying'))
Button_menu.add(InlineKeyboardButton(text = 'Product2', callback_data='product_buying'))
Button_menu.add(InlineKeyboardButton(text = 'Product3', callback_data='product_buying'))
Button_menu.add(InlineKeyboardButton(text = 'Product4', callback_data='product_buying'))
Button_menu.add(InlineKeyboardButton(text = 'Product5', callback_data='product_buying'))

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(commands=['start'])
async def start(message):
    await message.reply("Привет! Я бот помогающий твоему здоровью", reply_markup = kb)

@dp.message_handler(text='Рассчитать')
async def set_age(message):
    await message.reply('Введите свой возраст:')
    await UserState.age.set()

@dp.message_handler(text='Информация')
async def inform(message):
    await message.reply('Этот бот рассчитывает суточную норму каллорий для тебя')
    await message.answer('Норма каллорий рассчитывается по формуле: 10 x вес(кг) + 6,25 x рост(см) - 5 х возраст(г) - 161')

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
    await message.reply(f'Ваша суточная норма калорий: '
                        f'{int((10 * int(data["weight"])) + (6.25 * int(data["growth"])) - (5 * int(data["age"])) +5)}', reply_markup = kb)
    await state.finish()

@dp.message_handler(text = 'Купить')
async def get_buying_list(message):
    for n, i in enumerate(products, start=1):
        print(n, i)
        with open(f'{n}.jpg', 'rb') as photo:
            await message.answer_photo(photo, f'Название: {i[1]} | Описание: {i[2]} | Цена: {i[3]}')
    await message.answer('Выберите продукт для покупки:', reply_markup = Button_menu)

@dp.callback_query_handler(lambda call: call.data == 'product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')

class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = State()

@dp.message_handler(text=['Регистрация'])
async def sing_up(message):
    await message.reply('Введите имя пользователя (только латинский алфавит):')
    await RegistrationState.username.set()


@dp.message_handler(state=RegistrationState.username)
async def set_username(message, state):
    await state.update_data(username=message.text)
    if is_included(message.text):
        await message.reply('Пользователь существует. Введите другое имя')
        return
    await message.reply('Введите свой email:')
    await RegistrationState.email.set()

@dp.message_handler(state=RegistrationState.email)
async def set_email(message, state):
    await state.update_data(email=message.text)
    await message.reply('Введите свой возраст:')
    await RegistrationState.age.set()

@dp.message_handler(state=RegistrationState.age)
async def set_age(message, state):
    await state.update_data(age=message.text)
    data = await state.get_data()
    add_user(data['username'], data['email'], data['age'])
    await message.reply('Регистрация прошла успешно!', reply_markup = kb)
    await state.finish()




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)