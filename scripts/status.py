# Utilisation:
# <p>status help

import discord
from discord.ext import commands
import asyncio

class StatusChanger(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def status(self, ctx, statustype: str = None, activitytype: str = None, *, activite: str = None):
        """
        Change le statut et/ou l'activité
        """
        msg = ctx.message

        if statustype is None or statustype.lower() == "help":
            helpmsg = (
                "## 📜 **Commande status:** 📜\n\n"
                "**Description**: Permet de changer le statut et l'activité\n\n"
                "**options à mettre après <p>status**\n"
                "  `online`, `idle`, `dnd`, `invisible`\n"
                "  `clear`: supprime tout statut ou activité\n\n"
                "**options d'activité:**\n"
                "  `playing`: joue à <activité>\n"
                "  `streaming`: en direct <activité>\n"
                "  `listening`: écoute <activité>\n"
                "  `watching`: regarde <activité>\n\n"
                "**exemples:**\n"
                f"`{ctx.prefix}status online playing Minecraft`\n"
                f"`{ctx.prefix}status dnd streaming intrusif`\n"
                f"`{ctx.prefix}status clear`\n"
            )
            await ctx.message.edit(content=helpmsg)
            await asyncio.sleep(15)
            await msg.delete()
            return

        if statustype.lower() == "clear":
            # Réinitialiser le statut et supprimer l'activité
            await self.bot.change_presence(status=discord.Status.invisible, activity=None)
            await ctx.message.edit(content="✅ Statut réinitialisé ✅")
            await asyncio.sleep(2)
            await msg.delete()
            return

        statusdef = {
            "online": discord.Status.online,
            "idle": discord.Status.idle,
            "dnd": discord.Status.dnd,
            "invisible": discord.Status.invisible,
        }
        status = statusdef.get(statustype.lower(), discord.Status.online)

        # Définir l'activité
        activity = None
        if activitytype and activite:
            activitytype = activitytype.lower()
            if activitytype == "playing":
                activity = discord.Game(name=activite)
            elif activitytype == "streaming":
                activity = discord.Streaming(name=activite, url="https://twitch.tv/luther")  # Remplace par une URL réelle si besoin
            elif activitytype == "listening":
                activity = discord.Activity(type=discord.ActivityType.listening, name=activite)
            elif activitytype == "watching":
                activity = discord.Activity(type=discord.ActivityType.watching, name=activite)

        # Appliquer le statut et l'activité
        await self.bot.change_presence(status=status, activity=activity)
        await ctx.message.edit(content="✅ Statut changé ✅")
        await asyncio.sleep(2)
        await msg.delete()

def setup(bot):
    bot.add_cog(StatusChanger(bot))
