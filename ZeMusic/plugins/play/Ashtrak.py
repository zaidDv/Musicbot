from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardMarkup as Markup, InlineKeyboardButton as Button
from pyrogram.enums import ChatType
from pyrogram.errors import UserNotParticipant
from ZeMusic import app
import config

channel = "YMMYC"
Nem = config.BOT_NAME + " شغل"
async def subscription(_, __: Client, message: Message):
    user_id = message.from_user.id
    try: 
        await app.get_chat_member(channel, user_id)
    except UserNotParticipant: 
        return False
    return True
    
subscribed = filters.create(subscription)

# تعريف دالة لمعالجة الأوامر
@app.on_message(filters.command(["تشغيل", "بحث", "تخطي", "استئناف", "تقديم", "تحميل", "توقف", "مؤقت", "كمل", "كملي", "لارين بحث", "غنيلي", "شعر", "قران", "اذكار", "ادعيه", "play", "شغلي", "/start", "vplay", "vتشغيل", "cplay", "cvplay", "playforce", "vplayforce", "cplayforce", "cvplayforce", "start", "stats", "الاوامر", "اوامر", "ميوزك", "بنج", "سرعه", "song", "/song", "شغل",Nem], "") & ~subscribed)
async def command_handler(_: Client, message: Message):
    if message.chat.type in [ChatType.GROUP, ChatType.SUPERGROUP]:
        user_id = message.from_user.id
        user = message.from_user.first_name
        markup = Markup([
            [Button(text="اضغط للإشتراك", url=f"https://t.me/{channel}")]
        ])
        await message.reply(
            f"<b>↤عذراً عزيزي {user}\n↤عليك الإشتراك في قناة البوت اولاً",
            reply_markup=markup
        )
