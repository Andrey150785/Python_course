import logging

from aiogram import Bot, types, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

from config import *
import texts
from keyboards import *

logging.basicConfig(level=logging.INFO)
bot = Bot(token = API)
dp = Dispatcher(bot, storage = MemoryStorage())

@dp.message_handler(commands = ['start'])
async def start(message):
    await message.answer(texts.start, reply_markup = start_kb)

@dp.message_handler(text = 'О нас')
async def price(message):
    await message.answer(texts.about, reply_markup = start_kb)

@dp.message_handler(text = 'Стоимость')
async def info(message):
    await message.answer('Что вас интересует?', reply_markup = catalog_kb)

@dp.callback_query_handler(text = 'medium')
async def buy_game_M(call):
    await call.message.answer(texts.Mgame, reply_markup = buy_kb)
    await call.answer()

@dp.callback_query_handler(text = 'big')
async def buy_game_L(call):
    await call.message.answer(texts.Lgame, reply_markup = buy_kb)
    await call.answer()

@dp.callback_query_handler(text = 'mega')
async def buy_game_XL(call):
    await call.message.answer(texts.XLgame, reply_markup = buy_kb)
    await call.answer()

@dp.callback_query_handler(text = 'other')
async def buy_game_other(call):
    await call.message.answer(texts.other, reply_markup = buy_kb)
    await call.answer()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)