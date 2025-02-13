from aiohttp import web
from plugins import web_server
import asyncio
import pyromod.listen
from pyrogram import Client
from pyrogram.enums import ParseMode
import sys
from datetime import datetime
#rohit_1888 on Tg
from config import *


name ="""
 BY CODEFLIX BOTS
"""


class Bot(Client):
    def __init__(self):
        super().__init__(
            name="Bot",
            api_hash=API_HASH,
            api_id=APP_ID,
            plugins={
                "root": "plugins"
            },
            workers=TG_BOT_WORKERS,
            bot_token=TG_BOT_TOKEN
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()
        self.uptime = datetime.now()

        if FORCE_SUB_CHANNEL1:
            try:
                link = (await self.get_chat(FORCE_SUB_CHANNEL1)).invite_link
                if not link:
                    await self.export_chat_invite_link(FORCE_SUB_CHANNEL1)
                    link = (await self.get_chat(FORCE_SUB_CHANNEL1)).invite_link
                self.invitelink1 = link
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning("Bot can't Export Invite link from Force Sub Channel!")
                self.LOGGER(__name__).warning(f"Please Double check the FORCE_SUB_CHANNEL1 value and Make sure Bot is Admin in channel with Invite Users via Link Permission, Current Force Sub Channel Value: {FORCE_SUB_CHANNEL1}")
                self.LOGGER(__name__).info("\nBot Stopped. https://t.me/weebs_support for support")
                sys.exit()
        if FORCE_SUB_CHANNEL2:
            try:
                link = (await self.get_chat(FORCE_SUB_CHANNEL2)).invite_link
                if not link:
                    await self.export_chat_invite_link(FORCE_SUB_CHANNEL2)
                    link = (await self.get_chat(FORCE_SUB_CHANNEL2)).invite_link
                self.invitelink2 = link
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning("Bot can't Export Invite link from Force Sub Channel!")
                self.LOGGER(__name__).warning(f"Please Double check the FORCE_SUB_CHANNEL2 value and Make sure Bot is Admin in channel with Invite Users via Link Permission, Current Force Sub Channel Value: {FORCE_SUB_CHANNEL2}")
                self.LOGGER(__name__).info("\nBot Stopped. https://t.me/weebs_support for support")
                sys.exit()
        if FORCE_SUB_CHANNEL3:
            try:
                link = (await self.get_chat(FORCE_SUB_CHANNEL3)).invite_link
                if not link:
                    await self.export_chat_invite_link(FORCE_SUB_CHANNEL3)
                    link = (await self.get_chat(FORCE_SUB_CHANNEL3)).invite_link
                self.invitelink3 = link
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning("Bot can't Export Invite link from Force Sub Channel!")
                self.LOGGER(__name__).warning(f"Please Double check the FORCE_SUB_CHANNEL3 value and Make sure Bot is Admin in channel with Invite Users via Link Permission, Current Force Sub Channel Value: {FORCE_SUB_CHANNEL3}")
                self.LOGGER(__name__).info("\nBot Stopped. https://t.me/weebs_support for support")
                sys.exit()
        if FORCE_SUB_CHANNEL4:
            try:
                link = (await self.get_chat(FORCE_SUB_CHANNEL4)).invite_link
                if not link:
                    await self.export_chat_invite_link(FORCE_SUB_CHANNEL4)
                    link = (await self.get_chat(FORCE_SUB_CHANNEL4)).invite_link
                self.invitelink4 = link
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning("Bot can't Export Invite link from Force Sub Channel!")
                self.LOGGER(__name__).warning(f"Please Double check the FORCE_SUB_CHANNEL4 value and Make sure Bot is Admin in channel with Invite Users via Link Permission, Current Force Sub Channel Value: {FORCE_SUB_CHANNEL4}")
                self.LOGGER(__name__).info("\nBot Stopped. https://t.me/weebs_support for support")
                sys.exit()
        try:
            db_channel = await self.get_chat(CHANNEL_ID)
            self.db_channel = db_channel
            message_test = await self.send_message(chat_id=db_channel.id, text="Message de test")
            await message_test.delete()
            self.LOGGER(name).info(f"Connexion réussie à la chaîne de base de données&nbsp;: {CHANNEL_ID}")
        except pyrogram.errors.exceptions.bad_request_400.PeerIdInvalid as e: # exception plus spécifique
            self.LOGGER(name).error(f"ID de la chaîne de base de données invalide&nbsp;: {e}")
            self.LOGGER(name).error(f"Veuillez vérifier la valeur de CHANNEL_ID. Valeur actuelle&nbsp;: {CHANNEL_ID}")
            self.LOGGER(name).info("\nBot arrêté. Rejoignez https://t.me/weebs_support pour obtenir de l'aide")
            sys.exit(1)
        except Exception as e:  # pour les autres erreurs
            self.LOGGER(name).exception(f"Erreur lors de la connexion à la chaîne de base de données {CHANNEL_ID}&nbsp;: {e}")
            self.LOGGER(name).error(f"Assurez-vous que le bot est administrateur dans la chaîne de base de données et que CHANNEL_ID est correct. Valeur actuelle&nbsp;: {CHANNEL_ID}")
            self.LOGGER(name).info("\nBot arrêté. Rejoignez https://t.me/weebs_support pour obtenir de l'aide")
            sys.exit(1)


        self.LOGGER(name).info(f"Bot en fonctionnement&nbsp;!\n\nCréé par \nhttps://t.me/weebs_support")
        self.LOGGER(name).info(f"""       
  ___ ___  ___  ___ ___ _    _____  _____  ___ _____ ___ 
 / / _ \|   \| | | |  |_ _\ \/ / _ )/ _ \_   _/ |
| (_| (_) | |) | _|| _|| | | | >  <| _ \ (_) || | \ \
 \___\___/|___/|___|_| |____|___/_/\_\___/\___/ |_| |___/

 """)

        self.username = usr_bot_me.username
        self.LOGGER(name).info(f"Bot en fonctionnement&nbsp;! Fait par @Codeflix_Bots")

        # Démarrage du serveur Web (Gestion des erreurs ajoutée)
        try:
            app = web.AppRunner(await web_server())
            await app.setup()
            await web.TCPSite(app, "0.0.0.0", PORT).start()
            self.LOGGER(name).info(f"Serveur web démarré sur le port {PORT}")
        except Exception as e:
            self.LOGGER(name).exception(f"Erreur lors du démarrage du serveur web&nbsp;: {e}")
            self.LOGGER(name).info("\nBot arrêté. Rejoignez https://t.me/weebs_support pour obtenir de l'aide")
            sys.exit(1)


        try:
            await self.send_message(OWNER_ID, text=f"<b><blockquote>🤖 Bot redémarré par @bot_kingDOX</blockquote></b>")
        except Exception as e:
            self.LOGGER(name).warning(f"Impossible d'envoyer le message de redémarrage au propriétaire&nbsp;: {e}")

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(name).info("Bot arrêté.")

    def run(self):
        """Run the bot."""
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.start())
        self.LOGGER(__name__).info("Bot is now running. Thanks to @KIngcey")
        try:
            loop.run_forever()
        except KeyboardInterrupt:
            self.LOGGER(__name__).info("Shutting down...")
        finally:
            loop.run_until_complete(self.stop())

     #@rohit_1888 on Tg
