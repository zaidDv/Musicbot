import asyncio
from ZeMusic import app
from config import OWNER_ID
import os
import requests
import pyrogram
from pyrogram import Client, filters, emoji
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.errors import MessageNotModified
import config

@app.on_message(filters.regex(r"^(انا من|انا منو)$"))
async def BotMusic(client: Client, message: Message):
    
    italy = message.from_user.mention 
    user_id = message.from_user.id
    chat_id = message.chat.id
    try:
        member = await client.get_chat_member(chat_id, user_id)
        if user_id == 6811610440:
            rank = f"""مطور 🧚‍♀️ {italy}"""
        elif user_id == OWNER_ID:
            rank = f"""مطوري {italy}"""
        else:
            rank = italy
    except Exception as e:
        print(e)
    await message.reply_text(f"<b>⌯ انت </b>{rank}")


@app.on_message(filters.regex(r"^(بوت الحذف|رابط الحذف)$"))
async def DeletMusic(client: Client, message: Message):
    await message.reply_text(f"""<b>↯ بوت الحذف : ›</b> ( @DTeLebot )\n\n<b>↯ رابط الحذف : ›</b> ( <a href="https://my.telegram.org/auth?to=delete">اضغط هنا</a> )""")


