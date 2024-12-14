# Utilisation:
# <p>autoleave {on/off}

# dsl elle marche pas
# marche pas si vous voulez l'utiliser, fixez-la d'abord

# marche pas si vous voulez l'utiliser, fixez-la d'abord

# marche pas si vous voulez l'utiliser, fixez-la d'abord

# marche pas si vous voulez l'utiliser, fixez-la d'abord

# marche pas si vous voulez l'utiliser, fixez-la d'abord

# marche pas si vous voulez l'utiliser, fixez-la d'abord

# marche pas si vous voulez l'utiliser, fixez-la d'abord

# marche pas si vous voulez l'utiliser, fixez-la d'abord

# marche pas si vous voulez l'utiliser, fixez-la d'abord

# marche pas si vous voulez l'utiliser, fixez-la d'abord

# marche pas si vous voulez l'utiliser, fixez-la d'abord

# g trop la flm de le fix sah surtout que la cmd est plutôt useless




import asyncio
import os
import discord
from discord.ext import commands
class AutoLeave(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.autoleaveactif = False
        self.configf = "config/autoleave.txt"

        self.loadconfig()

    def loadconfig(self):
        """Charge le statu  d'autoleave depuis autoleave.txt"""
        if os.path.exists(self.configf):
            with open(self.configf, "r") as file:
                state = file.read().strip()
                if state.lower() in ["on", "off"]:
                    self.autoleaveactif = state.lower() == "on"
                else:
                    self.autoleaveactif = False
        else:
            self.savestate("off")

    def savestate(self, state: str):
        """sauvegarde le statut de autoleave dans config"""
        with open(self.configf, "w") as file:
            file.write(state)

    @commands.command()
    async def autoleave(self, ctx, state: str):
        msg1 = ctx.message
        await msg1.edit(content="🪐 intrusif autoleave 🪐")

        await asyncio.sleep(0.5)
        await msg1.delete()

        try:
            if state.lower() not in ["on", "off"]:
                await ctx.send("❌ Erreur: utilise `,autoleave on` ou `,autoleave off`")
                return

            self.autoleaveactif = state.lower() == "on"
            status = "activé" if self.autoleaveactif else "désactivé"

            self.savestate(state.lower())

            await ctx.send(f"✅ Autoleave: {status}")
        except Exception as e:
            await ctx.send(f"❌ Erreur: {e}")

    @commands.Cog.listener()
    async def groupejoin(self, channel):
        try:
            if self.autoleaveactif and isinstance(channel, discord.GroupChannel):
                await channel.leave()
        except Exception as e:
            print(f"erreur pendant l'essaie pour quitter le groupe: {e}")

def setup(bot):
    bot.add_cog(AutoLeave(bot))
