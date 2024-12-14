# Utilisation:

# <p>help
# <p>utils
# <p>server
# <p>user
# <p>lookup



# g mis !help pr que ça soit en haut et facile de trouver

import discord
from discord.ext import commands
import asyncio

class CHelp(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='help')
    async def chelp(self, ctx):
        helpmsg = (
            "## 🪐 __**intrusif**__ 🪐\n"
            "*donnez moi des idées d'options à rajouter svp*\n\n"
            f"`{ctx.prefix}help`\n"
            "-# ➜ ***Affiche le menu d'aide***\n"
            f"`{ctx.prefix}utils`\n"
            "-# ➜ ***Commandes d'utilitaire***\n"
            f"`{ctx.prefix}server`\n"
            "-# ➜ ***Commande de serveur***\n"
            f"`{ctx.prefix}user`\n"
            "-# ➜ ***Commande d'utilisateur***\n"
            f"`{ctx.prefix}lookup` -- SOON\n"
            "-# ➜ ***Commandes pour lookup qqn mdr***\n"
            f"`{ctx.prefix}reload`\n"
            "-# ➜ ***Redémarre intrusif***\n\n"
            "-# *Bot dev by <@1119309218340671639>*"
        )
        try:
            await ctx.message.edit(content=helpmsg)
            await asyncio.sleep(15)
            await ctx.message.delete()
        except discord.DiscordException as e:
            print(f"Erreur : {e}")

    @commands.command(name='utils')
    async def utils(self, ctx):
        utilsmsg = (
            "## 🪐 __**intrusif**__ 🪐\n\n"
            f"`{ctx.prefix}clear`\n"
            "-# ➜ ***Efface des messages***\n"
            f"`{ctx.prefix}closedms`\n"
            "-# ➜ ***Ferme tous les dms***\n"
            f"`{ctx.prefix}autoreact`\n"
            "-# ➜ ***Ajoute une réaction aux messages d'une personne***\n"
            f"`{ctx.prefix}send`\n"
            "-# ➜ ***Envoie des messages***\n"
            f"`{ctx.prefix}autoleave`\n"
            "-# ➜ ***Quitte automatiquement les groupes***\n\n"
            "-# *Bot dev by <@1119309218340671639>*"
        )
        try:
            await ctx.message.edit(content=utilsmsg)
            await asyncio.sleep(15)
            await ctx.message.delete()
        except discord.DiscordException as e:
            print(f"Erreur : {e}")

    @commands.command(name='user')
    async def user(self, ctx):
        usermsg = (
            "## 🪐 __**intrusif**__ 🪐\n\n"
            f"`{ctx.prefix}avatar`\n"
            "-# ➜ ***Affiche l'avatar d'un utilisateur'***\n"
            f"`{ctx.prefix}stealpfp`\n"
            "-# ➜ ***Met en photo de profil l'avatar d'un utilisateur***\n"
            f"`{ctx.prefix}stealbanner`\n"
            "-# ➜ ***Met en bannière la bannière d'un utilisateur***\n"
            f"`{ctx.prefix}userinfo`\n"
            "-# ➜ ***Affiche les informations d'un utilisateur***\n"
            f"`{ctx.prefix}pseudo`\n"
            "-# ➜ ***Génére des pseudos (4l)***\n"
            f"`{ctx.prefix}setpfp`\n"
            "-# ➜ ***Met en photo de profil une image***\n"
            f"`{ctx.prefix}setbanner`\n"
            "-# ➜ ***Met en bannière une image***\n\n"
            "-# *Bot dev by <@1119309218340671639>*"
        )
        try:
            await ctx.message.edit(content=usermsg)
            await asyncio.sleep(15)
            await ctx.message.delete()
        except discord.DiscordException as e:
            print(f"Erreur : {e}")

    @commands.command(name='server')
    async def server(self, ctx):
        servermsg = (
            "## 🪐 __**intrusif**__ 🪐\n\n"
            f"`{ctx.prefix}leaveall`\n"
            "-# ➜ ***Quitte tous les serveurs***\n"
            f"`{ctx.prefix}delchannels`\n"
            "-# ➜ ***Supprime tous les channels d'un serveur***\n"
            f"`{ctx.prefix}delroles`\n"
            "-# ➜ ***Supprime tous les rôles d'un serveur***\n"
            f"`{ctx.prefix}deltickets`\n"
            "-# ➜ ***Supprime tous les tickets d'un serveur***\n"
            f"`{ctx.prefix}serveravatar`\n"
            "-# ➜ ***Affiche l'avatar d'un serveur***\n"
            f"`{ctx.prefix}clone`\n"
            "-# ➜ ***Clone un serveur***\n\n"
            "-# *Bot dev by <@1119309218340671639>*"
        )
        try:
            await ctx.message.edit(content=servermsg)
            await asyncio.sleep(15)
            await ctx.message.delete()
        except discord.DiscordException as e:
            print(f"Erreur : {e}")

    @commands.command(name='lookup')
    async def lookup(self, ctx):
        lookupmsg = (
            "## 🪐 __**intrusif**__ 🪐\n"
            "**--__SOON__--**\n\n"
            f"`{ctx.prefix}snusbase`\n"
            "-# ➜ ***lookup db snusbase***\n"
            f"`{ctx.prefix}oathnet`\n"
            "-# ➜ ***lookup db oathnet***\n\n"
            "-# *Bot dev by <@1119309218340671639>*"
        )
        try:
            await ctx.message.edit(content=lookupmsg)
            await asyncio.sleep(15)
            await ctx.message.delete()
        except discord.DiscordException as e:
            print(f"Erreur : {e}")

    @commands.command(name='more')
    async def more(self, ctx):
        moremsg = (
            "## 🪐 __**intrusif**__ 🪐\n"
            "**--__SOON__--**\n\n"
            f"`{ctx.prefix}discord`\n"
            "-# ➜ ***discord officiel du sb***\n\n"
            "-# *Bot dev by <@1119309218340671639>*"
        )
        try:
            await ctx.message.edit(content=moremsg)
            await asyncio.sleep(15)
            await ctx.message.delete()
        except discord.DiscordException as e:
            print(f"Erreur : {e}")

def setup(bot):
    bot.add_cog(CHelp(bot))
