# Utilisation:
# <p>send {msg} {nb} {delay}

import discord
from discord.ext import commands
import asyncio

class SendMessage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.sending = False

    @commands.command(pass_context=True)
    async def send(self, ctx, message: str, number: int, delay: str = None):
        msg1 = ctx.message
        await msg1.edit(content=f"🪐 intrusif send 🪐 \n-# {number} fois | délai {delay if delay else 'pas de délai'}")

        if delay and delay.lower() == "off":
            self.sending = False
            await msg1.edit(content="✅ Send stoppé")
            return

        if not delay:
            delay = 0

        if self.sending:
            await ctx.send("Une boucle est déjà en cours, réessaye plus tard")
            return

        self.sending = True

        for i in range(number):
            if not self.sending:
                break
            try:
                await ctx.send(message)
                if delay:
                    await asyncio.sleep(float(delay))
            except Exception as e:
                print(f"Erreur:\n{e}")

        self.sending = False

def setup(bot):
    bot.add_cog(SendMessage(bot))
