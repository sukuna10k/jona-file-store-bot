#credit @codeflix_bots (telegram)

"""Obtenez l'id de l'utilisateur repondu
Syntax: /id"""

from pyrogram import filters, enums
from pyrogram.types import Message

from bot import Bot


@Bot.on_message(filters.command("id") & filters.private)
async def showid(client, message):
    chat_type = message.chat.type

    if chat_type == enums.ChatType.PRIVATE:
        user_id = message.chat.id
        await message.reply_text(
            f"<b>Votre ID est🫧:</b> <code>{user_id}</code>", quote=True
        )
