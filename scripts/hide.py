# Utilisation:
# <p>hide
# <p>hide {nb de ligne}

import discord
from discord.ext import commands


class HideCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hide(self, ctx, lines: int = 50):
        inv = "\u200b"
        hmsg = (inv + "\n") * lines
        await ctx.message.edit(content=hmsg)

def setup(bot):
    bot.add_cog(HideCommand(bot))
