# Utilisation:
# <p>delroles
import discord
from discord.ext import commands
import aiohttp
import asyncio

class DeleteRoles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def delroles(self, ctx):
        """
        Supprime tous les rôles du serveur où la commande est exécutée, sauf le rôle @everyone.
        """
        guild = ctx.guild
        if not guild:
            await ctx.message.edit(content="❌ Impossible de détecter l'ID du serveur ❌")
            await asyncio.sleep(2)
            await ctx.message.delete()
            return
        
        msg1 = ctx.message
        await msg1.edit(content="🪐 intrusif delroles 🪐")


        await asyncio.sleep(0.5)
        await msg1.delete()

        headers = {"Authorization": f"{self.bot.http.token}"}
        url = f"https://discord.com/api/v9/guilds/{guild.id}/roles"

        async with aiohttp.ClientSession() as session:
            try:

                async with session.get(url, headers=headers) as response:
                    if response.status != 200:
                        print(f"❌ Impossible de récupérer les rôles. Code HTTP : {response.status}")
                        return
                    roles = await response.json()


                for role in roles:
                    if role["name"] == "@everyone":
                        continue
                    rid = role["id"]
                    durl = f"{url}/{rid}"

                    async with session.delete(durl, headers=headers) as dresponse:
                        if dresponse.status == 403:
                            print(f"❌ Pas assez de permissions pr supprimer le rôle '{role['name']}'")
                        elif dresponse.status in [200, 204]:
                            print(f"✅ Rôle '{role['name']}' supprimé")
                        else:
                            print(f"❌ Impossible de supprimer le rôle '{role['name']}':\n{dresponse.status}")
                    await asyncio.sleep(0.6)

            except Exception as e:
                print(f"❌ Une erreur est survenue : {e}")

def setup(bot):
    bot.add_cog(DeleteRoles(bot))
