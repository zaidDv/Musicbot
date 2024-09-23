import math
import config
from ZeMusic import app 

from pyrogram.types import InlineKeyboardButton

from ZeMusic.utils.formatters import time_to_seconds


def track_markup(_, videoid, user_id, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
    ]
    return buttons


def stream_markup_timer(_, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    umm = math.floor(percentage)
    if 0 < umm <= 5:
        bar = "▁▄▂▇▄▅▄▅▃"
    elif 5 < umm < 10:
        bar = "▁▃▇▂▅▇▄▅▃"
    elif 10 <= umm < 15:
        bar = "▃▁▇▂▅▃▄▃▅"
    elif 15 <= umm < 20:
        bar = "▃▄▂▄▇▅▃▅▁"
    elif 20 <= umm < 25:
        bar = "▁▃▄▂▇▃▄▅▃"
    elif 25 <= umm < 30:
        bar = "▃▁▄▂▅▃▇▃▅"
    elif 30 <= umm < 35:
        bar = "▁▇▄▂▅▄▅▃▄"
    elif 35 <= umm < 40:
        bar = "▁▃▅▇▂▅▄▃▇"
    elif 40 <= umm < 45:
        bar = "▃▅▂▅▇▁▄▃▁"
    elif 45 < umm <= 50:
        bar = "▁▄▂▇▄▅▄▅▃"
    elif 50 < umm < 55:
        bar = "▁▃▇▂▅▇▄▅▃"
    elif 55 <= umm < 60:
        bar = "▃▁▇▂▅▃▄▃▅"
    elif 60 <= umm < 65:
        bar = "▃▄▂▄▇▅▃▅▁"
    elif 65 <= umm < 70:
        bar = "▁▃▄▂▇▃▄▅▃"
    elif 70 <= umm < 75:
        bar = "▃▁▄▂▅▃▇▃▅"
    elif 75 <= umm < 80:
        bar = "▁▇▄▂▅▄▅▃▄"
    elif 80 <= umm < 85:
        bar = "▁▃▅▇▂▅▄▃▇"
    elif 85 <= umm < 90:
        bar = "▃▅▂▅▇▁▄▃▁"
    elif 90 < umm < 95:
        bar = "▁▃▇▂▅▇▄▅▃"
    else:
        bar = "▃▇▂▅▁▅▄▃▁"
    buttons = [
                [
            InlineKeyboardButton(
                text=f"{played} {bar} {dur}",
                callback_data="GetTimer",
            )
        ],[
            InlineKeyboardButton(text="إستئناف ⋆", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="إيقاف مؤقت", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="⋆ إعاده", callback_data=f"ADMIN Replay|{chat_id}"),
        ],[
            InlineKeyboardButton(text="⋆ تخطي ⋆", callback_data=f"ADMIN Skip|{chat_id}"),
            InlineKeyboardButton(text="⋆ توقف ⋆", callback_data=f"ADMIN Stop|{chat_id}"),
        ],[
            InlineKeyboardButton(text="🧚‍♀️", url=config.CHANNEL_LINK),
            InlineKeyboardButton(text="المتجر", url=f"https://t.me/YMMYN"),
      ],
    ]
    return buttons


def stream_markup(_, chat_id):
    buttons = [
        [
            InlineKeyboardButton(text="إستئناف ⋆", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="إيقاف مؤقت", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="⋆ إعاده", callback_data=f"ADMIN Replay|{chat_id}"),
        ],[
            InlineKeyboardButton(text="⋆ تخطي ⋆", callback_data=f"ADMIN Skip|{chat_id}"),
            InlineKeyboardButton(text="⋆ توقف ⋆", callback_data=f"ADMIN Stop|{chat_id}"),
        ],[
            InlineKeyboardButton(text="🧚‍♀️", url=config.CHANNEL_LINK),
            InlineKeyboardButton(text="المتجر", url=f"https://t.me/YMMYN"),
      ],
    ]
    return buttons


def playlist_markup(_, videoid, user_id, ptype, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"ModyPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"ModyPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


def livestream_markup(_, videoid, user_id, mode, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_3"],
                callback_data=f"LiveStream {videoid}|{user_id}|{mode}|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


def slider_markup(_, videoid, user_id, query, query_type, channel, fplay):
    query = f"{query[:20]}"
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="◁",
                callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {query}|{user_id}",
            ),
            InlineKeyboardButton(
                text="𖣂 𝒓𝒆𝒔𝒖𝒎𝒆 𖣂",
                callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
        ],
    ]
    return buttons
