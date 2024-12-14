# Utilisation:
# <p>delchannels
import discord
from discord.ext import commands
import aiohttp
import asyncio

class DeleteChannels(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def delchannels(self, ctx):
        guild = ctx.guild
        if not guild:
            await ctx.message.edit(content="❌ Impossible de détecter l'ID du serveur ❌")
            await asyncio.sleep(2)
            await ctx.message.delete()
            return

        msg1 = ctx.message
        await msg1.edit(content="🪐 intrusif delchannels 🪐")

        headers = {"Authorization": f"{self.bot.http.token}"}
        url = f"https://discord.com/api/v9/guilds/{guild.id}/channels"

        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(url, headers=headers) as response:
                    if response.status != 200:
                        print(f"❌ Erreur: \n\n{response.status}")
                        return

                    channels = await response.json()

                for channel in channels:
                    cid = channel["id"]
                    delurl = f"https://discord.com/api/v9/channels/{cid}"

                    async with session.delete(delurl, headers=headers) as dresponse:
                        if dresponse.status == 403:
                            print(f"❌ Pas assez de perms pour supprimer le salon: {channel['name']}")
                        elif dresponse.status in [200, 204]:
                            print(f"✅ Salon '{channel['name']}' supprimé")
                        else:
                            print(f"❌ Impossible de supprimer le salon: {channel['name']}\n{dresponse.status}")
                    await asyncio.sleep(0.6)

            except Exception as e:
                print(f"❌ Erreur: {e}")

        try:
            curl = f"https://discord.com/api/v9/guilds/{guild.id}/channels"
            payload = {
                "name": "deleted",
                "type": 0
            }

            async with aiohttp.ClientSession() as session:
                async with session.post(curl, headers=headers, json=payload) as cresponse:
                    if cresponse.status in [200, 201]:
                        print("salon deleted créé")
                    else:
                        print(f"❌ Impossible de créer le salon deleted: {cresponse.status}")

        except Exception as e:
            print(f"❌ Erreur pdnt la création de deleted: \n\n{e}")

def setup(bot):
    bot.add_cog(DeleteChannels(bot))
