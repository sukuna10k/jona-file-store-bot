import asyncio
from aiohttp import web
from plugins import web_server
import pyromod.listen
from pyrogram import Client
from pyrogram.enums import ParseMode
import sys
from datetime import datetime
from config import *

class Bot(Client):
    def __init__(self):
        super().__init__(
            name="Bot",
            api_hash=API_HASH,
            api_id=APP_ID,
            plugins={"root": "plugins"},
            workers=TG_BOT_WORKERS,
            bot_token=TG_BOT_TOKEN
        )
        self.LOGGER = LOGGER
        self.uptime = datetime.now()

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()
        self.username = usr_bot_me.username

        # Vérification et exportation des liens d'invitation pour les channels obligatoires
        for index, channel in enumerate([FORCE_SUB_CHANNEL1, FORCE_SUB_CHANNEL2, FORCE_SUB_CHANNEL3, FORCE_SUB_CHANNEL4], start=1):
            if channel:
                try:
                    link = (await self.get_chat(channel)).invite_link
                    if not link:
                        await self.export_chat_invite_link(channel)
                        link = (await self.get_chat(channel)).invite_link
                    setattr(self, f"invitelink{index}", link)
                except Exception as e:
                    self.LOGGER(__name__).warning(f"Erreur lors de l'exportation du lien d'invitation : {e}")
                    self.LOGGER(__name__).warning(f"Vérifiez que le bot est admin dans la chaîne avec la permission d'inviter. Chaîne : {channel}")
                    sys.exit()

        # Vérification du DB Channel
        if not isinstance(CHANNEL_ID, int):
            self.LOGGER(__name__).error("CHANNEL_ID doit être un entier. Corrigez-le dans la configuration.")
            sys.exit()

        try:
            db_channel = await self.get_chat(CHANNEL_ID)
            self.db_channel = db_channel

            # Vérifier si le bot est admin avant d'envoyer un message
            admins = [admin.user.id async for admin in self.get_chat_members(CHANNEL_ID, filter="administrators")]
            if self.me.id not in admins:
                raise PermissionError("Le bot n'est pas administrateur du canal de base de données.")

            test_msg = await self.send_message(chat_id=db_channel.id, text="Test Message")
            await test_msg.delete()
        except Exception as e:
            self.LOGGER(__name__).warning(f"Erreur avec le canal DB: {e}")
            self.LOGGER(__name__).info("\nBot Stopped. Rejoignez https://t.me/weebs_support pour le support.")
            sys.exit()

        # Lancement du serveur web
        app = web.AppRunner(await web_server())
        await app.setup()
        await web.TCPSite(app, "0.0.0.0", PORT).start()

        # Notification au propriétaire
        try:
            await self.send_message(OWNER_ID, text="<b><blockquote>🤖 Bot Redémarré par @bot_kingDOX</blockquote></b>")
        except Exception as e:
            self.LOGGER(__name__).warning(f"Impossible d'envoyer un message au propriétaire: {e}")

        self.LOGGER(__name__).info("🚀 Bot en cours d'exécution...")

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("🛑 Bot arrêté.")

    def run(self):
        """Démarrer le bot en boucle."""
        try:
            asyncio.run(self.start())
        except KeyboardInterrupt:
            self.LOGGER(__name__).info("Arrêt manuel détecté. Fermeture...")
        finally:
            asyncio.run(self.stop())

if __name__ == "__main__":
    bot = Bot()
    bot.run()
