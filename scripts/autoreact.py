# Utilisation:
# <p>autoreact {on/off} {id/mention} {emoji}

#        exemple d'utilisation: 
#        <p>autoreact on @intrusif 🪐
#        <p>autoreact off @intrusif
#        <p>autoreact remove @intrusif

import discord
from discord.ext import commands
import asyncio

class AutoReact(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.settings = {}

    @commands.command()
    async def autoreact(self, ctx, mode: str, tgt: str, emo: str = None):
        try:
            msg = await ctx.message.edit(content="🪐intrusif autoreact🪐")
            if mode.lower() not in ["on", "off", "remove"]:
                await ctx.send("Erreur: syntaxe invalide, utilise on off ou remove")
                return
            try:
                if tgt.isdigit():
                    uid = int(tgt)
                elif tgt.startswith("<@") and tgt.endswith(">"):
                    uid = int(tgt.replace("<@", "").replace("!", "").replace(">", ""))
                else:
                    await ctx.send("Erreur: utilise une id ou une mention!")
                    return
            except ValueError:
                await ctx.send("Erreur: id ou mention invalide.")
                return
            if mode.lower() == "on":
                if not emo:
                    await ctx.send("Spécifie un emoji à la fin pour on")
                    return
                self.settings[ctx.channel.id] = {"uid": uid, "emo": emo}
                await ctx.send(f"Réaction auto activée pour <@{uid}> avec {emo}.")
            elif mode.lower() == "off":
                if ctx.channel.id in self.settings:
                    del self.settings[ctx.channel.id]
                    await ctx.send("Réaction auto désactivée.")
                else:
                    await ctx.send("Déjà désactivé.")
            elif mode.lower() == "remove":
                count = 0
                async for msg in ctx.channel.history(limit=100):
                    if msg.author.id == uid:
                        for react in msg.reactions:
                            if ctx.me in await react.users().flatten():
                                await react.remove(ctx.me)
                                count += 1
                await ctx.send(f"Réactions supprimées pour <@{uid}> ({count} au total).")
        except Exception as e:
            print(f"Erreur : {e}")
        await asyncio.sleep(0.5)
        await msg.delete()

    @commands.Cog.listener()
    async def onmessage(self, msg):
        if msg.author.bot:
            return
        cfg = self.settings.get(msg.channel.id)
        if cfg and cfg["uid"] == msg.author.id:
            try:
                await msg.add_reaction(cfg["emo"])
            except Exception as e:
                print(f"Erreur : {e}")
        await self.bot.process_commands(msg)

def setup(bot):
    bot.add_cog(AutoReact(bot))
