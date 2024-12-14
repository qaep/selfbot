# Utilisation:
# <p>block
# <p>block {id/mention}

import discord
from discord.ext import commands
import requests
import asyncio

class BlockUser(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def blockuser(self, uid):
        """Envoie une requête PUT pour bloquer l'utilisateur via l'API de Discord."""
        url = f"https://discord.com/api/v9/users/@me/relationships/{uid}"
        headers = {
            "Authorization": f"{self.bot.http.token}"
        }
        payload = { 
            "type": 2
        }
        response = requests.put(url, headers=headers, json=payload)
        return response.status_code == 204

    @commands.command()
    async def block(self, ctx, user: discord.User = None):
        msg = ctx.message
        if user is None:
            if isinstance(ctx.channel, discord.DMChannel):
                uid = str(ctx.channel.recipient.id)
                success = self.blockuser(uid)
                if success:
                    blocked1 = await msg.edit(content="🪐 intrusif block 🪐\n-# gg bg t'es bloqué")
                else:
                    await ctx.send(f"❌ Impossible de bloquer {user.name} ❌")
            else:
                await ctx.send("❌ Erreur: tu dois être dans un dm pour bloquer qqn sans mention")
            return

        uid = str(user.id) if isinstance(user, discord.User) else str(user)
        success = self.blockuser(uid)
        if success:
            blocked2 = await msg.edit(content=f"🪐 intrusif block 🪐\n-# utilisateur bloqué")
        else:
            await ctx.send(f"❌ Impossible de bloquer {user.name} ❌")

def setup(bot):
    bot.add_cog(BlockUser(bot))
