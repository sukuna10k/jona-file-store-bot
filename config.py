# Don't Remove Credit @CodeFlix_Bots, @rohit_1888
# Ask Doubt on telegram @CodeflixSupport


import os
from os import environ,getenv
import logging
from logging.handlers import RotatingFileHandler

#rohit_1888 on Tg

#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7783135016:AAEDA3NoMMtHpgjf5CroaQAHMkP-VC859k0")
#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "24817837"))
#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "acd9f0cc6beb08ce59383cf250052686")
#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002491166640"))
# NAMA OWNER
OWNER = os.environ.get("OWNER", "jnthree3")
#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "6120299142"))
#Port
PORT = os.environ.get("PORT", "8030")
#Database
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://jonat:botrebot@jonat.y6x6t.mongodb.net/?retryWrites=true&w=majority&appName=jonat")
DB_NAME = os.environ.get("DATABASE_NAME", "jonat")

#Time in seconds for message delete, put 0 to never delete
TIME = int(os.environ.get("TIME", "230"))


#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL1 = int(os.environ.get("FORCE_SUB_CHANNEL1", "-1002268712639"))
#put 0 to disable
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "0"))#put 0 to disable
FORCE_SUB_CHANNEL3 = int(os.environ.get("FORCE_SUB_CHANNEL3", "0"))#put 0 to disable
FORCE_SUB_CHANNEL4 = int(os.environ.get("FORCE_SUB_CHANNEL4", "0"))#put 0 to disable

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

START_PIC = os.environ.get("START_PIC", "https://envs.sh/V7E.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://envs.sh/V7D.jpg")

# Turn this feature on or off using True or False put value inside  ""
# TRUE for yes FALSE if no 
TOKEN = True if os.environ.get('TOKEN', "True") == "True" else False 
SHORTLINK_URL = os.environ.get("SHORTLINK_URL", "publicearn.online")
SHORTLINK_API = os.environ.get("SHORTLINK_API", "adabe1c0675be8ffc5ccbc84a9a65bc5a5d3ec69")
VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', 600)) # Add time in seconds
IS_VERIFY = os.environ.get("IS_VERIFY", "True")
TUT_VID = os.environ.get("TUT_VID","https://t.me/hwdownload/3")


HELP_TXT = "<b><blockquote>Ceci est un bot de stockage de fichiers  @bot_kingdox\n\n❏ commandes du bot\n├/start : Demarrer le bot\n├/about : Nos informations\n└/help : Aide relative du bot\n\nC'est simple. cliquez sur un lien du bot, rejoignez les canaux, puis cliquez sur Ressayer pour retrouver votre Film ou Serie.....!\n\n Créé par <a href=https://t.me/universboxfilmvf>Séries & films Vf</a></blockquote></b>"


ABOUT_TXT = "<b><blockquote>◈ Créteur: <a href=https://t.me/Kingcey</a>\n◈ Depot : <a href=https://t.me/bot_kingdox>bot KingDOX</a>\n◈ Chaine Anime : <a href=https://t.me/+H8FGCuZzfTo3NTFk>Anime Crow</a>\n◈ Séries & films Vf : <a href=https://t.me/serieetfilmsvfnet>Univers box film vf</a>\n◈ ᴀᴅᴜʟᴛ ᴍᴀɴʜᴡᴀ : <a href=https://t.me/Otakukingcey1>Persos</a>\n◈ ᴅᴇᴠᴇʟᴏᴘᴇʀ : <a href=https://t.me/Kingcey>🇰ιηg¢єу</a></blockquote></b>"


START_MSG = os.environ.get("START_MESSAGE", "<b><blockquote>Avengersssssss!! {first}\n\n Je suis un bot de stockage de fichiers, Je peux Stocker des fichiers puis vous pouvez les retrouvés Grâce à un lien Spetial .</blockquote></b>")
try:
    ADMINS=[7428552084]
    for x in (os.environ.get("ADMINS", "7428552084 6120299142 5760201151 1740287480").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Salut {first}\n\nTu dois d'abord rejoindre mes chaine pour retrouvés tes Fichiers. Après Cliquer sur ressayer")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>• ʙʏ @bot_KingDOX</b>")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "Désolé je ne comprends pas votre requête demandé à @jnthree3 !!"

ADMINS.append(OWNER_ID)
ADMINS.append(6120299142)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   
