import discord
from discord.ext import commands

from random import choice


class HorusEye(commands.Cog):

    def __init__(self, client):
        """
        ინიციალიზაცია
        :param client: გამშვები კლასი
        """
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Horus Eye is enabled")


def setup(client) -> None:
    """
    კოგის სეთაფი
    :param client: გამშვები კლასი
    :return: None
    """
    client.add_cog(HorusEye(client))
