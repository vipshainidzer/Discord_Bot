import discord
from discord.ext import commands

from random import choice
import os

client = commands.Bot(command_prefix=".")


@client.event
async def on_ready() -> None:
    """
    ამოწმებს ნამდვილად დაისტარტა თუ არა
    :return: None
    """
    print("Bot is ready")

#
# @client.command()
# async def ping(ctx):
#     await ctx.send(f"Pong {round(client.latency * 1000)} ms")


@client.command(aliases=["8ball", "test"])
async def _8ball(ctx, *, question):
    responses = [
        "ძაან მაგარია.",
        "აუუ თესლია ძმაო.",
        "ჰაჰ პერფექტოსია.",
        "სიგიჟეა.",
        "არაუშავს რა.",
        "წავა კი.",
    ]
    await ctx.send(f"Question: {question}\nAnswer: {choice(responses)}")


@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=1, ):
    """
    შეტყობინებების წაშლა ჩენელიდან კონკ რაოდენობით
    :param ctx: ბრძანების კონტექსტი
    :param amount: რამდენი სმს-ც გვინდა რო წაიშალოს ანუ ჩენელში
    :return: None
    """
    await ctx.channel.purge(limit=amount)


@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None) -> None:
    """
    მემბერების გაქიქვა
    :param ctx: ბრძანების კონტექსტი
    :param member: discord.Member
    :param reason: გაქიქვის მიზეზი
    :return: None
    """
    await member.kick(reason=reason)


@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None) -> None:
    """
    # TODO ეს ფუნგცია დასახვეწია
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


@client.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, user: discord.User) -> None:
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


@client.command()
@commands.has_permissions(administrator=True)
async def load(ctx, extension) -> None:
    """
    COGS LOADER
    :param ctx: ბრძანების კონტექსტი
    :param extension: კოგ კლასი
    :return: None
    """
    client.load_extension(f"cogs.{extension}")


@client.command()
@commands.has_permissions(administrator=True)
async def unload(ctx, extension) -> None:
    """
    COGS UNLOAD
    :param ctx: ბრძანების კონტექსტი
    :param extension: კოგ კლასი
    :return: None
    """
    client.unload_extension(f"cogs.{extension}")


# @client.command()
# async def unban(ctx, member):
#     banned_users = await ctx.guild.bans()
#     member_name, member_discriminator = member.split("#")
#
#     for ban_entry in banned_users:
#         user = ban_entry.user
#
#         if (user.name, user.discriminator) == (member_name, member_discriminator):
#             await ctx.guild.unban(user)
#             await ctx.send(f"unbanned {user.mention}")
#             return

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):  # თუ პითონის ფაილია
        client.load_extension(f"cogs.{filename[:-3]}")  # :-3 რადგან პითონის ფაილის სახელია საჭირო გაფართოების გარეშე

client.run(os.getenv('TOKEN'))
