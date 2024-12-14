import discord
from discord.ext import commands
import logging
import os
from json import load
import multiprocessing

green = "\033[92m"
blanc = "\033[0m"
logging.basicConfig(level=logging.INFO)

with open('config.json') as f:
    d = load(f)
    tokens = d["tokens"]
    prefix = d["prefix"]

def start1(token):
    bot = commands.Bot(command_prefix=prefix, self_bot=True, fetch_offline_members=False)

    bot.remove_command('help')
    @bot.event
    async def on_ready():
        print(f"Prêt avec le token: {token}")

        for filename in os.listdir('./scripts/'):
            if filename.endswith('.py'):
                try:
                    await bot.load_extension(f'scripts.{filename[:-3]}')
                    print(f"✅ Extension {filename} chargée")
                except Exception as e:
                    print(f"❌ Erreur pdnt le chargement de l'extension {filename}: {e}")
        
        logging.info("pret ✅")
# ici ajouter os cls si vous voulez enlever les prints du dessus
        print(green + "Bot prêt" + blanc)

    @bot.event
    async def on_message(msg):
        if msg.author == bot.user:
            return

        await bot.process_commands(msg)

    bot.run(token, bot=False)

def run_bot(token):
    start1(token)

if __name__ == "__main__":
    processes = []
    for token in tokens:
        process = multiprocessing.Process(target=run_bot, args=(token,))
        processes.append(process)
        process.start()