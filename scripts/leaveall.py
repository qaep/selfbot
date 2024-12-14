# Utilisation:
# <p>leaveall

import discord
from discord.ext import commands
import asyncio

class LeaveAll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def leaveall(self, ctx):
        try:
            message = await ctx.message.edit(content="🪐intrusif leaveall🪐")            
            await asyncio.sleep(0.5)
            await message.delete()
            for guild in ctx.bot.guilds:
                try:
                    if ctx.author in guild.members:
                        await guild.leave()
                        print(f"✅ serveur {guild.name} quitté")
                except Exception as e:
                    print(f"❌ Erreur le sb n'a pas pu quitter {guild.name}:\n{e}")

            print(f"✅ Serveurs quittés pour {ctx.author}")
        
        except Exception as e:
            print(f"Erreur: {e}")

def setup(bot):
    bot.add_cog(LeaveAll(bot))
