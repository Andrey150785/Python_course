from aiogram import Bot, types, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

api = "......"

bot = Bot(token = api)
dp = Dispatcher(bot, storage = MemoryStorage())

kb = ReplyKeyboardMarkup()
button1 = KeyboardButton(text = 'Рассчитать')
kb.add(button1)
button2 = KeyboardButton(text = 'Информация')
kb.add(button2)
button3 = KeyboardButton(text = 'Купить')
kb.add(button3)


Button_menu = InlineKeyboardMarkup()
Button_menu.add(InlineKeyboardButton(text = 'Product1', callback_data='product_buying'))
Button_menu.add(InlineKeyboardButton(text = 'Product2', callback_data='product_buying'))
Button_menu.add(InlineKeyboardButton(text = 'Product3', callback_data='product_buying'))
Button_menu.add(InlineKeyboardButton(text = 'Product4', callback_data='product_buying'))

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
    for i in range(1, 5):
        with open(f'{i}.jpg', 'rb') as photo:
            await message.answer_photo(photo, f'Название: Product{i} | Описание: описание {i} | Цена: {i * 100}')
    await message.answer('Выберите продукт для покупки:', reply_markup = Button_menu)

@dp.callback_query_handler(lambda call: call.data == 'product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

