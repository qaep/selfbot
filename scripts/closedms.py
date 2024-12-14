import discord
from discord.ext import commands
import aiohttp
import asyncio

class CloseDMs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def closedms(self, ctx):
        msg1 = ctx.message
        await msg1.edit(content="🪐 intrusif closedms 🪐")

        headers = {
            "Authorization": self.bot.http.token
        }

        async with aiohttp.ClientSession() as session:
            for channel in self.bot.private_channels:
                if isinstance(channel, (discord.DMChannel, discord.GroupChannel)):
                    try:
                        async with session.delete(
                            f"https://discord.com/api/v9/channels/{channel.id}?silent=false",
                            headers=headers
                        ) as res:
                            if res.status == 200:
                                print(f"Closed {channel.type} with ID: {channel.id}.")
                            else:
                                print(f"Failed to close {channel.type}. Status: {res.status}")
                    except Exception as e:
                        print(f"Error closing {channel.type} ID: {channel.id}. Exception: {e}")

        print("✅ Les dms ont été fermés")

def setup(bot):
    bot.add_cog(CloseDMs(bot))
