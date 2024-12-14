# marche pas, fix prochainement

# marche pas, fix prochainement

# marche pas, fix prochainement

# marche pas, fix prochainement

# marche pas, fix prochainement

# marche pas, fix prochainement









import asyncio
import discord
import requests
from discord.ext import commands


class SpamGC(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.spamgce = False

    @commands.command()
    async def spamgc(self, ctx, state: str, target: str = None, repeat: int = None):
        try:
            if state.lower() not in ["on", "off"]:
                await ctx.send("❌ Erreur : utilise `,spamgc on <id/@mention> <nb>` ou `,spamgc off`")
                return

            if state.lower() == "off":
                self.spamgce = False
                await ctx.send("✅ Spamgc a été stoppé")
                return

            if not target:
                await ctx.send("❌ Erreur: ajoutez une id ou une mention pour la cible")
                return

            group = ctx.channel
            if not isinstance(group, discord.GroupChannel):
                await ctx.send("❌ Erreur: la commande ne marche que dans un groupe")
                return

            if target.startswith("<@") and target.endswith(">"):  # Mention
                tid = int(target[3:-1]) if target[2] != '!' else int(target[3:-1])
            else:
                try:
                    tid = int(target)
                except ValueError:
                    await ctx.send("❌ Erreur: L'id n'est pas valide")
                    return

            try:
                user = await self.bot.fetch_user(tid)
            except discord.NotFound:
                await ctx.send("❌ Erreur: Utilisateur introuvable.")
                return

            if user not in self.bot.user.friends:
                await ctx.send("❌ Erreur: Impossible d'ajouter au groupe l'utilisateur, vérifiez que vous êtes amis avec lui")
                return

            self.spamgce = True
            count = 0

            async def kr():
                nonlocal count
                while self.spamgce and (repeat is None or count < repeat):
                    try:
                        url = f"https://discord.com/api/v9/channels/{group.id}/recipients/{user.id}"
                        headers = {
                            "Authorization": f"{self.bot.http.token}",
                            "Content-Type": "application/json"
                        }

                        response = requests.delete(url, headers=headers)
                        if response.status_code == 204:
                            print(f"{user.display_name} a été retiré du groupe")
                        elif response.status_code == 403:
                            print("❌ Erreur 403 : Vérifie le token ou les perms")
                            break
                        else:
                            print(f"Erreur lors du retrait de {user.display_name} : {response.status_code}, {response.text}")
                            await ctx.send(f"❌ Erreur: {response.status_code}\n{response.text}")
                            break


                        await asyncio.sleep(1)

                        response = requests.put(url, headers=headers)

                        if response.status_code == 204:
                            print(f"{user.display_name} a été ajouté au groupe")
                        else:
                            print(f"Erreur quand {user.display_name} a été ajouté:\n{response.status_code}")
                            break

                        count += 1
                        await asyncio.sleep(1)

                    except Exception as e:
                        await ctx.send(f"❌ Erreur:\n{str(e)}")
                        break

                if not self.spamgce:
                    await ctx.send("⏹ Spamgc stoppé")
                elif repeat is not None and count >= repeat:
                    await ctx.send(f"✅ Spam terminé\n-# (fait {count} fois)")

            await ctx.message.edit(content=f"intrusif spamgc\n-# pour {user.display_name}")
            await kr()

        except Exception as e:
            await ctx.send(content=f"❌ Erreur:\n{str(e)}")

def setup(bot):
    bot.add_cog(SpamGC(bot))
