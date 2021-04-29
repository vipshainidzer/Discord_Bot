import discord
from discord.ext import commands


class Example(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self) -> None:
        print("Bot is online")

    @commands.command()
    async def ping(self, ctx) -> None:
        await ctx.send(f"Pong {round(self.client.latency * 1000)} ms")


def setup(client) -> None:
    """
    კოგის სეთაფი
    :param client: გამშვები კლასი
    :return: None
    """
    client.add_cog(Example(client))
