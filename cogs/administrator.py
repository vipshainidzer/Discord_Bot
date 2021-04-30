import discord
from discord.ext import commands

from random import choice


class Administrator(commands.Cog):

    def __init__(self, client):
        """
        ინიციალიზაცია
        :param client: გამშვები კლასი
        """
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int) -> None:
        """
        შეტყობინებების წაშლა ჩენელიდან კონკ რაოდენობით
        :param ctx: ბრძანების კონტექსტი
        :param amount: რამდენი სმს-ც გვინდა რო წაიშალოს ჩენელში
        :return: None
        """
        await ctx.channel.purge(limit=amount)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None) -> None:
        """
        მემბერების ბანი
        :param ctx: ბრძანების კონტექსტი
        :param member: discord.Member
        :param reason: ბანის მიზეზი
        :return: None
        """
        mbed = discord.Embed(
            title="Success",
            description=f"ბანი დაედო მომხმარებელს: {member.display_name}",
        )
        await ctx.send(embed=mbed)
        await member.ban(reason=reason)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, user: discord.User) -> None:
        """
        # TODO ეს ფუნგცია დასახვეწია
        მემბერზე ბანის მოხსნა
        :param ctx: ბრძანების კონტექსტი
        :param user: discord.Member
        :return: None
        """
        guild = ctx.guild
        mbed = discord.Embed(
            title="Success",
            description=f"ბანის მოხსნა: {user}",
        )

        await guild.unban(user=user)
        await ctx.send(embed=mbed)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None) -> None:
        """
        მემბერების გაქიქვა
        :param ctx: ბრძანების კონტექსტი
        :param member: discord.Member
        :param reason: გაქიქვის მიზეზი
        :return: None
        """
        await member.kick(reason=reason)

    # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # TODO ERROR HANDLING METHODS BELOW                 #
    # # # # # # # # # # # # # # # # # # # # # # # # # # #
    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            mbed = discord.Embed(title="დაფიქსირდა შელოცვის ხმარების შეცდომა",
                                 description="```clear(self, ctx, amount: int)```",
                                 colour=discord.Colour.dark_red())
            await ctx.send(embed=mbed)


def setup(client) -> None:
    """
    კოგის სეთაფი
    :param client: გამშვები კლასი
    :return: None
    """
    client.add_cog(Administrator(client))
