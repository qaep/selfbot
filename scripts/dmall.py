# cmd marche pas, je la fix bientôt
# cmd marche pas, je la fix bientôt
# cmd marche pas, je la fix bientôt
# cmd marche pas, je la fix bientôt


# Utilisation:
# <p>dmall {msg}
import discord
from discord.ext import commands
import asyncio

class DmAll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.user = bot.user

    @commands.command()
    async def dmall(self, ctx, *, message: str):
        msg1 = ctx.message
        await msg1.edit(content="🪐 intrusif dmall 🪐")
        await asyncio.sleep(0.5)
        await msg1.delete()

        try:
            if not message.strip():
                await ctx.send("❌ Erreur: le msg est vide")
                return
            
            friends = [user for user in self.user.relationships if user.type == discord.RelationshipType.friend]

            if not friends:
                await ctx.send("❌ Erreur: pas d'ami")
                return

            fmsg = message.replace("\\n", "\n")

            failed = []
            for friend in friends:
                try:
                    await friend.send(fmsg)
                except Exception:
                    failed.append(friend.name)
            
            if failed:
                await ctx.send(f"✅ Dmall envoyé, mais échec pour: {', '.join(failed)}")
            else:
                await ctx.send("✅ Dmall envoyé")

        except Exception as e:
            await print(f"❌ Erreur: {e}")

def setup(bot):
    bot.add_cog(DmAll(bot))
