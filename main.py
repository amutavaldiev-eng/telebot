from aiogram import Bot, Dispatcher
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from dotenv import load_dotenv 
from service import *
from connection import *
import asyncio
import os
from datetime import *

load_dotenv()

token = os.getenv("BOT_TOKEN")
bot = Bot(token=token)
dp = Dispatcher()


@dp.message(CommandStart())
async def start_bot(message: Message):
    if await  get_user_by_id(message.from_user.id):
        await message.answer(f"Hello @{message.from_user.username}")
    else:
        user = message.from_user
        await create_user(user.username, user.full_name, user.id)
        await message.answer(f"Hello @{message.from_user.username}")


@dp.message(Command("help"))
async def help(message: Message):
    await message.answer(f"""
                         
This bot have 6 commands ⚙️

💫 /start - start bot

👥 /get_all_user - get users info

ℹ️ /info - info about me

📃 /about - about bot

🆘 /help - help?

⏰ /date - current date

""")
    
@dp.message(Command("about")) 
async def about(messeage: Message):
    await messeage.answer(f"💻It is my first bot I build it in 2026💻")
@dp.message(Command("info")) 
async def about(messeage: Message):
    await messeage.answer(f"""
Hello 👋🏻
My name is Akbar, I am 15 years old, I had created this bot                      
                          
                          """)
    
@dp.message(Command("date")) 
async def about(messeage: Message):
    await messeage.answer(f"""
Today is {datetime.now().strftime("%d-%m-%Y")} 📆
Time is {datetime.now().strftime("%H:%M:%S")} 🕐
                          """)
    
    
@dp.message(Command("get_all_user"))
async def help(message: Message):
    users = await get_users()
    for user in users:
        await message.answer(f"""
User ID: {user['telegram_id']}
Username: {user['username']}  
Full name: {user['full_name']}
                             """) 
        
async def main():
    await create_table()
    print("Bot started.....")
    await dp.start_polling(bot)
    
    
    
if __name__ == "__main__":
    asyncio.run(main())


