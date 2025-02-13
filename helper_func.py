# (©) CodeFlix_Bots
# rohit_1888 on Tg - Ne pas retirer cette ligne

import base64
import re
import asyncio
from pyrogram import filters
from pyrogram.enums import ChatMemberStatus
from config import *
from pyrogram.errors import FloodWait, UserNotParticipant
from shortzy import Shortzy
from database.database import *

# ---- Vérification d'abonnement ----
async def is_subscribed(filter, client, update, channel):
    if not channel:
        return True
    user_id = update.from_user.id
    if user_id in ADMINS:
        return True
    try:
        member = await client.get_chat_member(chat_id=channel, user_id=user_id)
    except UserNotParticipant:
        return False
    return member.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.MEMBER]

subscribed1 = filters.create(lambda f, c, u: is_subscribed(f, c, u, FORCE_SUB_CHANNEL1))
subscribed2 = filters.create(lambda f, c, u: is_subscribed(f, c, u, FORCE_SUB_CHANNEL2))
subscribed3 = filters.create(lambda f, c, u: is_subscribed(f, c, u, FORCE_SUB_CHANNEL3))
subscribed4 = filters.create(lambda f, c, u: is_subscribed(f, c, u, FORCE_SUB_CHANNEL4))

# ---- Encodage/Décodage Base64 ----
async def encode(string):
    return base64.urlsafe_b64encode(string.encode("ascii")).decode("ascii").strip("=")

async def decode(base64_string):
    base64_string = base64_string.strip("=")
    padded = base64_string + "=" * (-len(base64_string) % 4)
    return base64.urlsafe_b64decode(padded.encode("ascii")).decode("ascii")

# ---- Récupération des messages en lot ----
async def get_messages(client, message_ids):
    messages, total_messages = [], 0
    while total_messages != len(message_ids):
        temp_ids = message_ids[total_messages:total_messages+200]
        try:
            msgs = await client.get_messages(chat_id=client.db_channel.id, message_ids=temp_ids)
        except FloodWait as e:
            await asyncio.sleep(e.x)
            msgs = await client.get_messages(chat_id=client.db_channel.id, message_ids=temp_ids)
        except Exception:
            break
        total_messages += len(temp_ids)
        messages.extend(msgs)
    return messages

# ---- Extraction de l'ID du message ----
async def get_message_id(client, message):
    if message.forward_from_chat and message.forward_from_chat.id == client.db_channel.id:
        return message.forward_from_message_id
    if message.text:
        pattern = r"https://t.me/(?:c/)?([^/]+)/(\d+)"
        match = re.match(pattern, message.text)
        if match:
            channel_id, msg_id = match.groups()
            if channel_id.isdigit() and f"-100{channel_id}" == str(client.db_channel.id):
                return int(msg_id)
            elif channel_id == client.db_channel.username:
                return int(msg_id)
    return 0

# ---- Formatage du temps en lecture humaine ----
def get_readable_time(seconds: int) -> str:
    time_list, time_suffix_list = [], ["s", "m", "h", "days"]
    for i in range(4):
        remainder, result = divmod(seconds, 60 if i < 2 else 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(f"{int(result)}{time_suffix_list[i]}")
        seconds = int(remainder)
    return ":".join(time_list[::-1])

# ---- Gestion du statut de vérification ----
async def get_verify_status(user_id):
    return await db_verify_status(user_id)

async def update_verify_status(user_id, verify_token="", is_verified=False, verified_time=0, link=""):
    current = await db_verify_status(user_id)
    current.update({"verify_token": verify_token, "is_verified": is_verified, "verified_time": verified_time, "link": link})
    await db_update_verify_status(user_id, current)

# ---- Raccourcissement de lien ----
async def get_shortlink(url, api, link):
    return await Shortzy(api_key=api, base_site=url).convert(link)

# ---- Calcul du temps restant ----
def get_exp_time(seconds):
    periods = [('days', 86400), ('hours', 3600), ('mins', 60), ('secs', 1)]
    result = [f"{int(seconds // s)} {name}" for name, s in periods if seconds >= s]
    return " ".join(result) if result else "0 secs"
