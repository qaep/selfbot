# Utilisation:
# <p>clear
# <p>clear {nb} {délai}
# <p>clear off

import discord
from discord.ext import commands
import asyncio

class Clear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.clearing = False
        self.delcount = 0
        
    @commands.command()
    async def clear(self, ctx, amount: str = None):
        if amount == "off":
            if self.clearing:
                self.clearing = False
                stopmsg = await ctx.send(f"⚠️ Clear arrêté ⚠️")
                await asyncio.sleep(1)
                await stopmsg.delete()
            else:
                await ctx.send("❌ Aucun clear actif")
            return
        
        if amount is None:
            amount = 100

        try:
            amount = int(amount)
        except (ValueError, TypeError):
            errormsg = await ctx.send(f"❌ Mets un nombre valide ou 'off'")
            await asyncio.sleep(3)
            await errormsg.delete()
            return

        self.clearing = True
        self.delcount = 0
        clearingmsg = await ctx.message.edit(content="🪐 intrusif clear 🪐")

        async for msg in ctx.channel.history(limit=amount):
            if not self.clearing:
                break
            if msg.type == discord.MessageType.default and msg.author.id == self.bot.user.id:
                await msg.delete()
                self.delcount += 1
                await asyncio.sleep(0.25)

        if self.delcount > 0:
            delmsg = await ctx.send(f"✅ {self.delcount} messages supprimés ✅")
            await asyncio.sleep(2)
            await delmsg.delete()
        else:
            errormsg = await ctx.send("❌ Aucun message trouvé à supprimer")
            await asyncio.sleep(3)
            await errormsg.delete()

        await asyncio.sleep(0.5)
        await clearingmsg.delete()

def setup(bot):
    bot.add_cog(Clear(bot))
