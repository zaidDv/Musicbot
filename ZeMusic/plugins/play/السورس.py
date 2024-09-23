import asyncio

import os
import time
import requests
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZeMusic import app
from random import  choice, randint

                
@app.on_message(
    command(["سورس","‹ 🧚‍♀️ ›"," ","🧚‍♀️"])
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/d030044dbdc7c4133b0c5.jpg",
        caption = f"""<b>  <b>\n<a href="https://t.me/fzfffzz"> ➮ 𝒲𝑒𝓁𝒸𝑜𝓂𝑒 𝓉𝑜 𝒮𝑜𝓊𝓇𝒸𝑒 𝒲𝒽𝒾𝓉𝑒 🧚‍♀</a></b>""",
reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                         "🧚‍♀", url=f"https://t.me/fzfffzz"), 
                 ],[
                   InlineKeyboardButton(
                        "𝒮𝑜𝓊𝓇𝒸𝑒 𝒲𝒽𝒾𝓉𝑒 🧚‍♀", url=f"https://t.me/z_llllli"),
                ],

            ]

        ),

    )
