import logging
import os
from Config import Messages as tr
from Config import Config as C
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant, UsernameNotOccupied, ChatAdminRequired, PeerIdInvalid
UPDATES_CHANNEL = C.UPDATES_CHANNEL
logging.basicConfig(level=logging.INFO)

@Client.on_message(filters.incoming & filters.command(['start', 'star@FSUB_VKTGBOT']))
def _start(client, message):
    update_channel = UPDATES_CHANNEL
    if update_channel:
        try:
            user = client.get_chat_member(update_channel, message.chat.id)
            if user.status == "kicked":
               client.send_message(
                   chat_id=message.chat.id,
                   text="Sorry Sir, You are Banned to use me. Contact my [Support Group](https://t.me/VkTgBotSupport).",
                   parse_mode="markdown",
                   disable_web_page_preview=True
               )
               return
        except UserNotParticipant:
            client.send_message(
                chat_id=message.chat.id,
                text="**Please Join My Updates Channel to use this Bot!**",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Join Updates Channel", url=f"https://t.me/VkTgBotz")
                        ]
                    ]
                ),
                parse_mode="markdown"
            )
            return
        except Exception:
            client.send_message(message.chat.id,
                text=tr.START_MSG.format(message.from_user.first_name, message.from_user.id),
	        reply_markup=InlineKeyboardMarkup(
                    [
                        [
                           InlineKeyboardButton("UPDATE AND NEWS✅", url="https://t.me/VKTGBOTZ"),
                           InlineKeyboardButton("🤖 Support Group", url="https://t.me/VKTGBOTSUPPORT")
                      ],
                     [
                           InlineKeyboardButton("DEVELOPER🥰", url="https://t.me/VIJAY1142")
                     ]
                 ]
             ),
        parse_mode="markdown",
        reply_to_message_id=message.message_id
        )
            return
    client.send_photo(chat_id=message.chat.id,
        photo="https://telegra.ph/file/77f93a3b170b0b5af9432.jpg"
        caption=tr.START_MSG.format(message.from_user.first_name, message.from_user.id),
	reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("UPDATE AND NEWS✅", url="https://t.me/VkTgBotz"),
                    InlineKeyboardButton("Support Group", url="https://t.me/VkTgBotSupport")
                ],
                [
                    InlineKeyboardButton("🥰DEVELOPER", url="https://t.me/VIJAY1142")
                ]
            ]
        ),
        parse_mode="markdown",
        reply_to_message_id=message.message_id
        )


@Client.on_message(filters.incoming & filters.command(['source_code', 'source_code@FSUB_VKTGBOT']))
def _source_code(client, message):
    client.send_message(message.chat.id,
        text=tr.SC_MSG.format(message.from_user.first_name, message.from_user.id),
	reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🎖️SOURCE CODE🎖️", url="https://github.com/I-AM-VIJAY/FORCESUB-BOT")
                ],
                [
                    InlineKeyboardButton("Join Updates Channel", url="https://t.me/VkTgBotz"),
                    InlineKeyboardButton("Support Group", url="https://t.me/VkTgBotSupport")
                ],
                [
                    InlineKeyboardButton("DEVELOPER💝", url="https://t.me/VIJAY1142")
                ]
            ]
        ),
        parse_mode="markdown",
        reply_to_message_id=message.message_id
        )

@Client.on_message(filters.incoming & filters.command(['help', 'help@FSUB_VKTGBOT']))
def _help(client, message):
    update_channel = UPDATES_CHANNEL
    if update_channel:
        try:
            user = client.get_chat_member(update_channel, message.chat.id)
            if user.status == "kicked":
               client.send_message(
                   chat_id=message.chat.id,
                   text="**SORRY SIR, YOU ARE BANNED TO USE ME. CONTACT MY** [Support Group](https://t.me/VkTgBotz).",
                   parse_mode="markdown",
                   disable_web_page_preview=True
               )
               return
        except UserNotParticipant:
            client.send_message(
                chat_id=message.chat.id,
                text="**1st YOU CAN JOIN MY CHANNEL. PLEASE JOIN MY UPDATES CHANNEL FOR USE ME!**",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("🎖️Join Updates Channel", url=f"https://t.me/{update_channel}")
                        ]
                    ]
                ),
                parse_mode="markdown"
            )
            return
        except Exception:
            client.send_message(
                chat_id=message.chat.id,
                text="HEY USE THIS COMMAND IN MY PM. \nFor MORE HELP ASK IN MY [Support Group](https://t.me/VKTGBOTSUPPORT).",
                parse_mode="markdown",
                disable_web_page_preview=True)
            return
    client.send_message(chat_id = message.chat.id,
        text = tr.HELP_MSG[1],
        disable_notification = True,
        reply_markup = InlineKeyboardMarkup(map(1)),
        reply_to_message_id = message.message_id
    )

help_callback_filter = filters.create(lambda _, __, query: query.data.startswith('help+'))

@Client.on_callback_query(help_callback_filter)
def help_answer(client, callback_query):
    chat_id = callback_query.from_user.id
    message_id = callback_query.message.message_id
    msg = int(callback_query.data.split('+')[1])
    client.edit_message_text(chat_id=chat_id,    message_id=message_id,
        text=tr.HELP_MSG[msg],    reply_markup=InlineKeyboardMarkup(map(msg))
    )


def map(pos):
    if(pos==1):
        button = [
            [InlineKeyboardButton(text = '👉', callback_data = "help+2")]
        ]
    elif(pos==len(tr.HELP_MSG)-1):
        button = [
            [InlineKeyboardButton(text = '👈', callback_data = f"help+{pos-1}")]
        ]
    else:
        button = [
            [
                InlineKeyboardButton(text = '👈', callback_data = f"help+{pos-1}"),
                InlineKeyboardButton(text = '👉', callback_data = f"help+{pos+1}")
            ],
        ]
    return button
