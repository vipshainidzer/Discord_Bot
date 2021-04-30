import discord
from discord.ext import commands, tasks

from itertools import cycle


class Tasks(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.statuses = cycle(["Human Free Will",
                               "Only Men Free Will",
                               "Only Women Free Will",
                               "Animals Free Will",
                               "Bots Free Will",
                               "Roman Gods Free Will",
                               "Georgian Gods Free Will",])

    @commands.Cog.listener()
    async def on_ready(self) -> None:
        self.change_status.start()
        print("Tasks is activated")

    @tasks.loop(seconds=10)
    async def change_status(self):
        await self.client.change_presence(activity=discord.Game(next(self.statuses)))


def setup(client) -> None:
    """
    კოგის სეთაფი
    :param client: გამშვები კლასი
    :return: None
    """
    client.add_cog(Tasks(client))


if __name__ == '__main__':
    pass
