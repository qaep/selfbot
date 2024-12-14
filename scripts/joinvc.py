# Utilisation:
# <p>joinvc {id}

import discord
from discord.ext import commands

class VoiceCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def joinvc(self, ctx, cid: int):
        msg1 = ctx.message
        await msg1.edit(content="🪐 intrusif joinvc 🪐")
        channel = self.bot.get_channel(cid)
        if isinstance(channel, discord.VoiceChannel):
            try:
                if ctx.voice_client:
                    print("❌ déjà connecté à un salon vocal, déconnexion...")
                    await ctx.voice_client.disconnect()
                    print("✅ déconnecté")
                await channel.connect()
                print(f"connecté au vc: {channel.name}")                
                await msg1.edit(content=f"✅ salon <#{channel.id}> rejoint ✅")
            except Exception as e:
                print(f"Erreur: {e}")
                await msg1.edit(content="❌ Erreur: le sb n'a pas pu se connecter au salon vocal ❌")
        else:
            print("❌ Erreur: ce salon n'existe pas ou alors c'est pas un salon vocal ❌")
            await msg1.edit(content="❌ Erreur: ce salon n'existe pas ou alors c'est pas un salon vocal ❌")

def setup(bot):
    bot.add_cog(VoiceCommands(bot))
