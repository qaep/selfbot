# Utilisation:
# <p>userinfo
# <p>userinfo {id/mention}

import discord
from discord.ext import commands
import base64
import aiohttp

class UserInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def userinfo(self, ctx, user: discord.User = None):
        """
        Donne des informations sur un utilisateur.
        Utilisation : ,userinfo <mention ou ID>
        """
        try:
            if user is None:
                user = ctx.author

            username = user.name
            discriminator = user.discriminator
            avurl = user.avatar_url if user.avatar_url else None
            bot1 = "Oui" if user.bot else "Non"
            createdat = user.created_at.strftime("%d/%m/%Y à %H:%M:%S")

            activity = "Aucune activité"
            eid = base64.b64encode(str(user.id).encode('utf-8')).decode('utf-8').rstrip("=")
            burl = None

            url1 = f"https://discord.com/api/v9/users/{user.id}/profile"
            headers = {
                "Authorization": f"{self.bot.http.token}"
            }

            async with aiohttp.ClientSession() as session:
                async with session.get(url1, headers=headers) as response:
                    if response.status == 200:
                        data = await response.json()
                        bhash = data["user"].get("banner")
                        if bhash:
                            burl = f"https://cdn.discordapp.com/banners/{user.id}/{bhash}?size=4096"
                    else:
                        burl = "Pas de bannière trouvée"

            joinedat = None
            roles = None

            if ctx.guild:
                member = ctx.guild.get_member(user.id)

                if member:
                    joinedat = member.joinedat.strftime("%d/%m/%Y à %H:%M:%S") if member.joinedat else None
                    roles = ", ".join([role.name for role in member.roles if role.name != "@everyone"]) or None
                    activity = member.activity.name if member.activity else "Aucune activité"

            imsg = f"""
Informations sur **{username}**#{discriminator} :
- **ID** : {user.id}
- **Avatar** : {avurl if avurl else 'Pas d\'avatar'}
- **Bot** : {bot1}
- **Compte créé le** : {createdat}
- **Début du token** : {eid}
- **Activité** : {activity}
- **Bannière**: {(burl) if burl else 'Pas de bannière'}
            """

            if joinedat:
                imsg += f"- **A rejoint le serveur le** : {joinedat}\n"
            if roles:
                imsg += f"- **Rôles** : {roles}\n"

            await ctx.send(imsg)

        except Exception as e:
            await print(f"❌ Erreur:\n{str(e)}")

def setup(bot):
    bot.add_cog(UserInfo(bot))
