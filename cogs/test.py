import discord
from discord.ext import commands


class Test(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Test is online")

    @commands.command()
    async def tester(self, ctx) -> None:
        await ctx.send("tested")


def setup(client) -> None:
    """
    კოგის სეთაფი
    :param client: გამშვები კლასი
    :return: None
    """
    client.add_cog(Test(client))
