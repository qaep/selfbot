# Utilisation:
# <p>serveravatar {id}

import discord
from discord.ext import commands
import aiohttp
import asyncio

class ServerAvatar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def serveravatar(self, ctx, guild_id: int):
        url1 = f"https://discord.com/api/v9/guilds/{guild_id}"

        headers = {
            "Authorization": f"{self.bot.http.token}"
        }

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url1, headers=headers) as response:
                    if response.status == 200:
                        data = await response.json()
                        aid = data.get("icon")

                        if aid:
                            aurl = f"https://cdn.discordapp.com/icons/{guild_id}/{aid}.png?size=4096"
                            await ctx.message.edit(content=f"[avatar du serveur {aid}]({aurl})")
                        else:
                            print("⚠️ Le serv n'a pas d'avatar")
                        
                        await asyncio.sleep(15)
                        await ctx.message.delete()
                    else:
                        print(f"❌ Erreur:\n{response.status}")
        except Exception as e:
            print(f"❌ Erreur:\n{e}")
def setup(bot):
    bot.add_cog(ServerAvatar(bot))
