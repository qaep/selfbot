# Utilisation:
# <p>avatar {id/mention}
import discord
from discord.ext import commands
import aiohttp
import asyncio

class AvatarCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def avatar(self, ctx, userid: int):
        url = f"https://discord.com/api/v9/users/{userid}/profile?with_mutual_guilds=true&with_mutual_friends=true&with_mutual_friends_count=false"
        headers = {"Authorization": self.bot.http.token}

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, headers=headers) as response:
                    if response.status == 200:
                        data = await response.json()
                        icon_id = data["user"].get("avatar")
                        if icon_id:
                            avatar_url = f"https://cdn.discordapp.com/avatars/{userid}/{icon_id}.png?size=4096"
                            await ctx.message.edit(content=f"[Avatar de {data['user']['username']}:]({avatar_url})")
                        else:
                            await ctx.message.edit(content="⚠️ Cet user n'a pas d'avatar")
                        
                        await asyncio.sleep(15)
                        await ctx.message.delete()
                    else:
                        print(f"Erreur HTTP: {response.status}")
        except Exception as e:
            print(f"Erreur : {e}")

def setup(bot):
    bot.add_cog(AvatarCommand(bot))
