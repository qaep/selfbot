# Utilisation:
# <p>pseudo {nb de charactères}[l][n] {delay}
# <p>pseudo off
import discord
import random
import string
import time
import requests
import asyncio
from discord.ext import commands
from colorama import Fore, init

URL = "https://discord.com/api/v9/users/@me/pomelo-attempt"

class Pseudo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.generating = False
        self.vpseudos = []
        self.delay = 2
        self.nletters = 4
        self.mpseudos = float('inf')
        self.type1 = 'l'
    def cua(self, username):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"{self.bot.http.token}"
        }
        body = {"username": username}
        response = requests.post(URL, headers=headers, json=body)

        if response.status_code == 200:
            return response.json().get("taken") is False
        elif response.status_code == 429:
            rafter = response.json().get("retry_after", 5)
            print(f"Rate limited, le bot réessaiera dans {rafter}s")
            time.sleep(rafter)
            return self.cua(username)
        else:
            print(f"Erreur pendant la validation de '{username}': {response.json().get('message', 'Erreur inconnue')}")
            return False


    def genusername(self):
        if self.type1 == 'l':
            chars = string.ascii_lowercase
        elif self.type1 == 'n':
            chars = string.digits
        elif self.type1 == 'ln':
            chars = string.ascii_lowercase + string.digits
        username = ''.join(random.choice(chars) for _ in range(self.nletters))
        return username


    @commands.command()
    async def pseudo(self, ctx, *args):
        if len(args) == 1 and args[0].lower() == "off":
            if self.generating:
                self.generating = False
                genarrete = await ctx.send("✅ Génération arrêtée ✅")
                await asyncio.sleep(1)
                await genarrete.delete()
            else:
                await ctx.send("❌ Aucune boucle ❌")
            return

        mode = args[0].lower()
        if 'l' in mode:
            try:
                self.nletters = int(mode.replace('l', '').replace('n', '').replace(' ', ''))
                self.type1 = 'l'
                if 'n' in mode:
                    self.type1 = 'ln'
            except ValueError:
                await ctx.send("❌ Erreur : tu dois ajouter l ou n après le nombre de caractères dans le pseudo ❌")
                return
        elif 'n' in mode:
            try:
                self.nletters = int(mode.replace('n', '').replace(' ', ''))
                self.type1 = 'n'
            except ValueError:
                await ctx.send("❌ Erreur : tu dois ajouter un nombre après le 'n' dans le mode ❌")
                return
        if len(args) > 1 and args[1].isdigit():
            self.mpseudos = int(args[1])
        else:
            self.mpseudos = float('inf')
        if len(args) > 2 and args[2][-1] == 's' and args[2][:-1].isdigit():
            self.delay = int(args[2][:-1])
        else:
            self.delay = 1

        if not self.generating:
            self.generating = True
            intrusifpseudo = await ctx.send("🪐 intrusif pseudo 🪐")
            await asyncio.sleep(2)
            await intrusifpseudo.delete()

            count = 0
            self.vpseudos.clear()

            while self.generating and count < self.mpseudos:
                pseudo = self.genusername()

                valid = self.cua(pseudo)
                if valid:
                    self.vpseudos.append(pseudo)
                    print(f"✅ {pseudo}")
                else:
                    print(f"❌ {pseudo}")

                count += 1
                await asyncio.sleep(self.delay)

                if not self.generating:
                    if self.vpseudos:
                        vpseudostrouve = await ctx.send(f"✅ Génération terminée, pseudos trouvés: \n```{', '.join(self.vpseudos)}```")
                        await asyncio.sleep(15)
                        await vpseudostrouve.delete()
                    else:
                        aucuntrouve = await ctx.send("✅ Génération terminée, pseudos trouvés: aucun")
                        await asyncio.sleep(5)
                        await aucuntrouve.delete()
        else:   
            await ctx.send("❌ La commande est déjà en cours")

def setup(bot):
    bot.add_cog(Pseudo(bot))
