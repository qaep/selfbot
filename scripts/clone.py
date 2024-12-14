# Utilisation:
# <p>clone {id du serv source}
import discord
from discord.ext import commands
import aiohttp
import asyncio
import json

REQDELAY = 0.65

class CloneServer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def clone(self, ctx, srcserverid: int):
        tgtserverid = ctx.guild.id

        origmsg = ctx.message
        await origmsg.edit(content="🪐 intrusif clone 🪐")
        await asyncio.sleep(2)
        await origmsg.delete()

        headers = {
            "Authorization": f"{self.bot.http.token}",
            "Content-Type": "application/json"
        }

        srcurl = f"https://discord.com/api/v9/guilds/{srcserverid}"
        tgturlroles = f"https://discord.com/api/v9/guilds/{tgtserverid}/roles"
        srcchannelsurl = f"https://discord.com/api/v9/guilds/{srcserverid}/channels"
        tgturlchannels = f"https://discord.com/api/v9/guilds/{tgtserverid}/channels"

        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(f"https://discord.com/api/v9/guilds/{tgtserverid}/roles", headers=headers) as res:
                    if res.status != 200:
                        print(f"❌ Récupération des rôles échouée. Code: {res.status}")
                        return
                    tgtroles = await res.json()

                for role in tgtroles:
                    if role["name"] == "@everyone":
                        continue
                    deleteurl = f"https://discord.com/api/v9/guilds/{tgtserverid}/roles/{role['id']}"
                    async with session.delete(deleteurl, headers=headers) as delres:
                        if delres.status == 204:
                            print(f"✅ Rôle '{role['name']}' supprimé")
                        await asyncio.sleep(REQDELAY)

                async with session.get(f"https://discord.com/api/v9/guilds/{tgtserverid}/channels", headers=headers) as res:
                    if res.status != 200:
                        print(f"❌ Récupération des canaux échouée. Code: {res.status}")
                        return
                    tgtchannels = await res.json()

                for channel in tgtchannels:
                    deletechannelurl = f"https://discord.com/api/v9/channels/{channel['id']}"
                    async with session.delete(deletechannelurl, headers=headers) as delres:
                        if delres.status == 200:
                            print(f"✅ Canal '{channel['name']}' supprimé.")
                        await asyncio.sleep(REQDELAY)

                async with session.get(srcurl, headers=headers) as res:
                    if res.status != 200:
                        print(f"❌ Récupération des rôles source échouée. Code: {res.status}")
                        return
                    srcdata = await res.json()
                    roles = srcdata.get("roles", [])
                print(f"Rôles récupérés : {len(roles)}")

                for role in roles:
                    if role["name"] == "@everyone":
                        continue

                    roledata = {
                        "name": role["name"],
                        "permissions": role.get("permissions", 0),
                        "color": role.get("color", 0),
                        "hoist": role.get("hoist", False),
                        "mentionable": role.get("mentionable", False),
                    }

                    async with session.post(tgturlroles, headers=headers, json=roledata) as roleres:
                        if roleres.status == 201:
                            createdrole = await roleres.json()
                            print(f"✅ Rôle '{role['name']}' cloné (ID : {createdrole['id']}).")
                        await asyncio.sleep(REQDELAY)

                async with session.get(srcchannelsurl, headers=headers) as res:
                    if res.status != 200:
                        print(f"❌ Récupération des canaux source échouée. Code: {res.status}")
                        return
                    channels = await res.json()
                print(f"Canaux récupérés : {len(channels)}")

                catmapping = {}
                for channel in channels:
                    channeldata = {
                        "name": channel["name"],
                        "type": channel["type"],
                        "position": channel["position"],
                        "permission_overwrites": [
                            {
                                "id": overwrite["id"],
                                "type": overwrite["type"],
                                "allow": overwrite["allow"],
                                "deny": overwrite["deny"]
                            } for overwrite in channel.get("permission_overwrites", [])
                        ]
                    }

                    if channel["type"] == 4:
                        async with session.post(tgturlchannels, headers=headers, json=channeldata) as catres:
                            if catres.status == 201:
                                createdcat = await catres.json()
                                catmapping[channel["id"]] = createdcat["id"]
                                print(f"✅ Catégorie '{channel['name']}' cloné")
                            await asyncio.sleep(REQDELAY)
                    else:
                        if channel["parent_id"] in catmapping:
                            channeldata["parent_id"] = catmapping[channel["parent_id"]]
                        async with session.post(tgturlchannels, headers=headers, json=channeldata) as chan_res:
                            if chan_res.status == 201:
                                print(f"✅ Channel '{channel['name']}' cloné")
                            await asyncio.sleep(REQDELAY)

                print("✅ Clonage terminé")

            except Exception as e:
                print(f"❌ Erreur : {e}")

def setup(bot):
    bot.add_cog(CloneServer(bot))
