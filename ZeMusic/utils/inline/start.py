from pyrogram.types import InlineKeyboardButton
import config
from ZeMusic import app

Lnk= "https://t.me/" +config.CHANNEL_LINK

def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="أضفني إلى مجموعتك او قناتك",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text="الأوامر", callback_data="zzzback")],
        [
            InlineKeyboardButton(text="🧚‍♀️", url=config.CHANNEL_LINK),
            InlineKeyboardButton(text="🥇", url=f"https://t.me/fzfffzz")
        ],

    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="أضفني إلى مجموعتك او قناتك",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text="الأوامر", callback_data="zzzback")],
        [
            InlineKeyboardButton(text="🧚‍♀️", url=config.CHANNEL_LINK),
            InlineKeyboardButton(text="🥇", url=f"https://t.me/fzfffzz")
        ],

    ]
    return buttons
