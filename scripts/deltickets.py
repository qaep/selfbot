# Utilisation:
# <p>deltickets
import discord
from discord.ext import commands
import aiohttp
import asyncio

class DeleteTickets(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def deltickets(self, ctx, server_id: int):
        msg1 = ctx.message
        await msg1.edit(content="🪐 intrusif deltickets 🪐")

        await asyncio.sleep(0.5)
        await msg1.delete()

        headers = {"Authorization": f"{self.bot.http.token}"}
        url = f"https://discord.com/api/v9/guilds/{server_id}/channels"

        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(url, headers=headers) as re:
                    if re.status != 200:
                        print(f"❌ Impossible de récupérer les salons: {re.status}")
                        return
                    channels = await re.json()

                for channel in channels:
                    if channel["name"].startswith("ticket"):
                        cid = channel["id"]
                        durl = f"https://discord.com/api/v9/channels/{cid}"

                        async with session.delete(durl, headers=headers) as dresponse:
                            if dresponse.status == 403:
                                print(f"❌ Pas assez de permissions pr supprimer le salon '{channel['name']}'")
                            elif dresponse.status == 200:
                                print(f"✅ Salon '{channel['name']}' supprimé")
                            else:
                                print(f"❌ Impossible de supprimer le salon '{channel['name']}':\n{dresponse.status}")
                        await asyncio.sleep(0.5)

            except Exception as e:
                print(f"❌ Une erreur est survenue:\n{e}")

def setup(bot):
    bot.add_cog(DeleteTickets(bot))
