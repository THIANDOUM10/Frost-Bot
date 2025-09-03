import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

# Charge les variables du .env
load_dotenv()
token = os.getenv("DISCORD_TOKEN")  # Récupère ton token depuis le .env

class FrostBot(commands.Bot):
    async def setup_hook(self):
        for extension in ['fun', 'moderator', 'menu', 'info']:
            await self.load_extension(f'cogs.{extension}')

intents = discord.Intents.all()
bot = FrostBot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Connecté en tant que {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"⚡ {len(synced)} commande(s) par KINGFROST synchronisée(s) ❄️")
    except Exception as e:
        print(f"❌ Erreur lors de la synchronisation : {e}")

bot.run(token=token)
