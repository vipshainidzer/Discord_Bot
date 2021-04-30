import json

import discord
from discord.ext import commands

from os import chdir

chdir(r'C:\PycharmProjects\Discord_Bot')


class LevelSystem(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.user = None
        self.users = None
        self.channel = None

    def __set_user(self, new_user):
        self.user = new_user

    def __set_users(self, new_users):
        self.users = new_users

    def __set_channel(self, new_channel):
        self.channel = new_channel

    @commands.Cog.listener()
    async def on_member_join(self, member):
        """
        სერვერზე ახალი წევრის გაწევრიანებისას მისი არსებულ წევრთა დატაში დამატება
        :param member: ახალი წევრი
        :return: None
        """
        # ვხსნი ჯეისონ ფაილს
        with open("C:\\PycharmProjects\\Discord_Bot\\users.json", "r") as file:
            users = json.load(file)

        await self.update_data(users, member)

        # ვწერ განხორციელებულ ცვლილებებს ჯეისონ ფაილში
        with open("C:\\PycharmProjects\\Discord_Bot\\users.json", "r") as file:
            json.dump(users, file)

    @commands.Cog.listener()
    async def on_message(self, message):
        """
        სერვერზე არსებული წევრების აქტიურობის აღრიცხვა და შესაბამისობის დადგენა დასაწინაურებლად
        :param message: მემბერის მესიჯი
        :return: None
        """
        # ვხსნი ჯეისონ ფაილს
        with open("C:\\PycharmProjects\\Discord_Bot\\users.json", "r") as file:
            users = json.load(file)

        self.__set_users(users)
        self.__set_user(message.author)
        self.__set_channel(message.channel)

        await self.update_data()
        await self.add_experience(5)
        await self.level_up()

        # ვწერ განხორციელებულ ცვლილებებს ჯეისონ ფაილში
        with open("C:\\PycharmProjects\\Discord_Bot\\users.json", "w") as file:
            json.dump(self.users, file)

    @commands.command()
    async def update_data(self):
        """
        ლეველინგ სისტემის დატას  განახლება იუზერებთან მიმართებით
        :return: None
        """
        if self.user.id not in self.users:  # თუ მომხმარებლი აღრიცხვაზე არ მყავს ...
            self.users[self.user.id] = {}  # ... ამყავს მომხმარებელი აღრიცხვაზე
            self.users[self.user.id]["experience"] = 0
            self.users[self.user.id]["level"] = 1

    @commands.command()
    async def add_experience(self, exp):
        """
        მომხმარებლის იქსფერიენსის აღრიცხვა. კერძოდ: არსებული იოქსფერიენსის გაზრდა
        :param exp: იქსპერიენსის ქულა
        :return: None
        """
        self.users[self.user.id]["experience"] += exp

    @commands.command()
    async def level_up(self):
        """
        მომხმარებლის ახალ ლეველზე გადაყვანა
        :return: None
        """
        experience = self.users[self.user.id]["experience"]
        lvl_start = self.users[self.user.id]["level"]
        lvl_end = int(experience ** (1/4))  # დისქრდის ფორმულა ლეველის გამოსათვლელად

        if lvl_start < lvl_end:
            mbed = discord.Embed(title="მლოცველის გადაკურთხვა",
                                 description=f"``` {self.user.mention} გადაკურთხულია ლეველზე: {lvl_end} ```",
                                 colour=discord.Colour.dark_red())
            await self.client.send_message(self.channel, embed=mbed)
            self.users[self.user.id]["level"] = lvl_end


def setup(client) -> None:
    """
    კოგის სეთაფი
    :param client: გამშვები კლასი
    :return: None
    """
    client.add_cog(LevelSystem(client))
