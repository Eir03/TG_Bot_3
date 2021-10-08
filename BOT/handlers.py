 # Import library
import aiogram
import sqlite3
import csv, datetime
from main import bot, dp
from aiogram import types
from aiogram.types import Message

keyboard_markup = types.ReplyKeyboardMarkup(row_width=3)
array_keyboard = ['Кнопочка', 'Съесть почку']

# Send message to admin
async def send_to_admin(dp):
	await bot.send_message(chat_id=admin_id, text="Bot start")
 # Start bot using func
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
        keyboard_markup.add(*(types.KeyboardButton(text) for text in array_keyboard))
        await message.answer(text='Здрасть',reply_markup=keyboard_markup)
        array_keyboard.clear()
        statistic(message.chat.id,message.text)
        stat(message.chat.id,message.text)

def stat(user_id, command):
        conn = sqlite3.connect('DataBa.db')
        cursor = conn.cursor()
        data = datetime.datetime.today().strftime("%d-%m-%Y %H:%M")
        cursor.execute("INSERT INTO stata(user_id, user_command, date) VALUES ('%s', '%s', '%s')" % (user_id, command, data))
        conn.commit()
        cursor.close()

def statistic(user_id, command):
    data = datetime.datetime.today().strftime("%Y-%m-d %H:%M")
    with open('data.csv','a',newline="") as fil:
            wr = csv.writer(fil, delimiter=';')
            wr.writerow([data, user_id, command])
