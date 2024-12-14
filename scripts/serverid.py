# Utilisation:
# <p>serveravatar {invite}

import discord
from discord.ext import commands
import re
import asyncio

class ServerInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def serverid(self, ctx, invitation: str):
        msg = ctx.message
        await ctx.message.edit(content="🔍")

        match = re.search(r"(https?://)?(www\.)?(discord\.(gg|com/invite)/)?(?P<code>[a-zA-Z0-9\-]+)", invitation)
        if not match:
            await ctx.message.edit(content="❌ Erreur: Invitation invalide")
            return

        invcode = match.group("code")

        try:
            invite = await self.bot.fetch_invite(invcode)
            gid = invite.guild.id
            gname = invite.guild.name

            await ctx.message.edit(content=f"serv : ```{gname}```\nid : ```{gid}```")
            await asyncio.sleep(15)
            await msg.delete()

        except discord.NotFound:
            await ctx.message.edit(content="❌ Erreur: l'invitation est introuvable ou elle est expirée ❌")
            await asyncio.sleep(15)
            await msg.delete()
        except discord.HTTPException as e:
            await ctx.message.edit(content=f"❌ Erreur:\n{e} ❌")
            await asyncio.sleep(15)
            await msg.delete()

def setup(bot):
    bot.add_cog(ServerInfo(bot))
