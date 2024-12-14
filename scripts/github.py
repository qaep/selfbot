# Utilisation:
# <p>github {nb de charactères}[l][n] {delay}
# <p>github off
import random
import string
import time
import requests
import asyncio
from discord.ext import commands
class Github(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.generating = False
        self.valid_pseudos = []
        self.delay = 0.5 
        self.num_letters = 3
        self.max_pseudos = float('inf')
        self.char_type = 'l'

    def verif(self, username):
        url = f"https://github.com/{username}"
        try:
            response = requests.get(url)    
            return response.status_code == 404
        except requests.RequestException as e:
            print(f"Erreur: {e}")
            return False

    def gen(self):
        if self.char_type == 'l':
            chars = string.ascii_lowercase
        elif self.char_type == 'n':
            chars = string.digits
        elif self.char_type == 'ln':
            chars = string.ascii_lowercase + string.digits
        else:
            chars = ""
        return ''.join(random.choice(chars) for _ in range(self.num_letters))

    @commands.command()
    async def github(self, ctx, *args):
        if len(args) == 1 and args[0].lower() == "off":
            if self.generating:
                self.generating = False
                await ctx.send("✅ Boucle arrêtée")
            else:
                await ctx.send("❌ Aucune boucle n'est en cours")
            return

        if self.generating:
            await ctx.send("❌ Une autre boucle est déjà en cours")
            return

        try:
            mode = args[0].lower()
            self.num_letters = int(''.join(filter(str.isdigit, mode)))
            self.char_type = ''.join(filter(str.isalpha, mode))
            self.max_pseudos = int(args[1]) if len(args) > 1 and args[1].isdigit() else float('inf')
            self.delay = int(args[2][:-1]) if len(args) > 2 and args[2].endswith('s') and args[2][:-1].isdigit() else 1
        except (IndexError, ValueError):
            await ctx.send("❌ Erreur de syntaxe")
            return

        self.generating = True
        self.valid_pseudos.clear()
        await ctx.send("🪐 intrusif github 🪐")

        count = 0
        while self.generating and count < self.max_pseudos:
            username = self.gen()
            is_available = self.verif(username)
            if is_available:
                self.valid_pseudos.append(username)
                print(f"✅ {username}")
            else:
                print(f"❌ {username}")
            count += 1
            await asyncio.sleep(self.delay)

        self.generating = False
        if self.valid_pseudos:
            await ctx.send(f"✅ Pseudos disponibles: ```{', '.join(self.valid_pseudos)}```")
        else:
            await ctx.send("❌ Aucun pseudo disponible trouvé")

def setup(bot):
    bot.add_cog(Github(bot))
