from pyrogram import filters
from pyrogram.types import Message

from ZeMusic import app
from ZeMusic.misc import SUDOERS
from ZeMusic.utils.database import autoend_off, autoend_on

@app.on_message(filters.command("مغادرة") & SUDOERS)
async def auto_end_stream(_, message: Message):
    usage = "<b>ᴇxᴀᴍᴘʟᴇ :</b>\n\n/مغادرة [تفعيل | تعطيل]"
    if len(message.command) != 2:
        return await message.reply_text(usage)

    state = message.text.split(None, 1)[1].strip().lower()
    if state == "enable" or state == "تفعيل":
        await autoend_on()
        await message.reply_text(
            "تم تفعيل المغادرة التلقائية بنجاح.\n\nسيقوم الحساب المساعد بمغادرة الدردشة تلقائياً عندما لا يوجد أعضاء في المكالمة."
        )
    elif state == "disable" or state == "تعطيل":
        await autoend_off()
        await message.reply_text("تم تعطيل المغادرة التلقائية بنجاح.")
    else:
        await message.reply_text(usage)
