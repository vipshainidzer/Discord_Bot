import discord
from discord.ext import commands
from random import choice


class Test(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Test is online")

    @commands.command()
    async def tester(self, ctx) -> None:
        await ctx.send("tested")

    @commands.command(aliases=["ასწორებს", "ძერსკია"])
    async def _8ball(self, ctx, *, question) -> None:
        """
        პროსტა იძახის რაღაცაებს რა
        :param ctx: ბრძანების კონტექსტი
        :param question: ქასთომ შეკითხვა
        :return:
        """
        responses = [
            "ძაან მაგარია!",
            "აუუ თესლია ძმაო!",
            "ჰაჰ პერფექტოსია!",
            "სიგიჟეა!",
            "არაუშავს რა!",
            "წავა კი!",
        ]
        await ctx.send(f"Question: {question}\nAnswer: {choice(responses)}")


def setup(client) -> None:
    """
    კოგის სეთაფი
    :param client: გამშვები კლასი
    :return: None
    """
    client.add_cog(Test(client))
