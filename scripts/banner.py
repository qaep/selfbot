# Utilisation:
# <p>banner {id/mention}

import discord
from discord.ext import commands
import aiohttp
import asyncio

class BannerCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def banner(self, ctx, useri: str = None):
        userid = ctx.author.id if useri is None else int(useri.strip('<@!>')) if not useri.isdigit() else int(useri)
        api_url = f"https://discord.com/api/v9/users/{userid}/profile"
        headers = {"Authorization": self.bot.http.token}

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(api_url, headers=headers) as response:
                    if response.status == 200:
                        data = await response.json()
                        bhash = data["user"].get("banner")
                        if bhash:
                            burl = f"https://cdn.discordapp.com/banners/{userid}/{bhash}?size=4096"
                            await ctx.send(f"[bannière de**{data['user']['username']}**]({burl})")
                        else:
                            await ctx.send("⚠️ Cet utilisateur n'a pas de bannière")
                    else:
                        await ctx.send(f"❌ Erreur API : {response.status}")
        except Exception as e:
            await ctx.send(f"❌ Une erreur s'est produite : {str(e)}")

def setup(bot):
    bot.add_cog(BannerCommand(bot))
