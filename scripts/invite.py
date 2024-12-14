# Utilisation:
# <p>discord
import discord
from discord.ext import commands
import asyncio

class Invite(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def discord(self, ctx):
        msg = ctx.message
        await msg.edit(content=f"discord du sb:\nhttps://discord.gg/LienIci")
        await asyncio.sleep(15)
        await msg.delete()

def setup(bot):
    bot.add_cog(Invite(bot))