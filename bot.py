import discord
from discord.ext import commands, tasks

from random import choice
import os
from itertools import cycle
from colorama import Back, Style
import json


def get_prefix(client, message):
    """
    სერვერის აიდის მიხედვით მისი პრეფიქსის მიღება
    :param client: დისქორდის სერვერის სოკეტთან კონექტორი
    :param message: კონკ მესიჯი სერვერძე შგაწევრიანება/გასვლაზე
    :return: None
    """
    with open("prefix.json", "r") as file:
        prefixes = json.load(file)

    return prefixes[str(message.guild.id)]


client = commands.Bot(command_prefix=get_prefix)


def is_it_me(ctx) -> bool:
    return ctx.author.id == 630654405045256192


@client.event
async def on_ready() -> None:
    """
    ამოწმებს ნამდვილად დაისტარტა თუ არა
    :return: None
    """
    print("Bot is ready")


@client.event
async def on_guild_join(guild) -> None:
    """
    დიფალტ პრეფიქსის შექმნა ახალ სერვერებზე
    :param guild: კონკრეტული სერვერი
    :return: None
    """
    with open("prefix.json", "r") as file:
        prefixes = json.load(file)

    prefixes[str(guild.id)] = "$"

    with open("prefix.json", "w") as file:
        json.dump(prefixes, file, indent=4)


@client.event
async def on_guild_remove(guild) -> None:
    """
    სერვეროდან გასვლის შემდეგ კონკრეტული პრეფიქსის წაშლა
    :param guild: კონკრეტული სერვერი
    :return: None
    """
    with open("prefix.json", "r") as file:
        prefixes = json.load(file)

    prefixes.pop(str(guild.id))

    with open("prefix.json", "w") as file:
        json.dump(prefixes, file, indent=4)


@client.command()
@commands.check(is_it_me)
async def change_prefix(ctx, prefix) -> None:
    """
    ბრაძანებების პრეფიქსის ცვლილება
    :param ctx: ბრძანების კონტექსტი
    :param prefix: ახალი პრეფიქსი
    :return: None
    """
    with open("prefix.json", "r") as file:
        prefixes = json.load(file)

    prefixes[str(ctx.guild.id)] = prefix

    with open("prefix.json", "w") as file:
        json.dump(prefixes, file, indent=4)
    mbed = discord.Embed(title="DAVID",
                         description=f"``` შელოცვა განხორციელდა თხილის ჯოხით! ახალი ჯოხი: {prefix} ```",
                         colour=discord.Colour.dark_red())
    await ctx.send(embed=mbed)


@client.command()
async def ping(ctx) -> None:
    """
    იპინგება და კავშირის სიხშირეს აჩვენებს
    :param ctx: ბრძანების კონტექსტი
    :return: None
    """
    await ctx.send(f"Pong {round(client.latency * 1000)} ms")


@client.command()
@commands.check(is_it_me)
async def load(ctx, extension) -> None:
    """
    COGS LOADER
    :param ctx: ბრძანების კონტექსტი
    :param extension: კოგ კლასი
    :return: None
    """
    client.load_extension(f"cogs.{extension}")
    mbed = discord.Embed(title="DAVID",
                         description="```შელოცვა განხორციელდა თხილის ჯოხით!```",
                         colour=discord.Colour.dark_red())
    await ctx.send(embed=mbed)


@client.command()
@commands.check(is_it_me)
async def unload(ctx, extension) -> None:
    """
    COGS UNLOAD
    :param ctx: ბრძანების კონტექსტი
    :param extension: კოგ კლასი
    :return: None
    """
    client.unload_extension(f"cogs.{extension}")
    mbed = discord.Embed(title="DAVID",
                         description="```შელოცვა განხორციელდა თხილის ჯოხით!```",
                         colour=discord.Colour.dark_red())
    await ctx.send(embed=mbed)


@client.event
async def on_command_error(ctx, error) -> None:
    """
    ზოგადი ერორ ჰენდლერი
    :param ctx: ბრძანების კონტექსტი
    :param error: command მოდულის რომელიღაც ერორ კლასისი ობიექტი
    :return: None
    """

    if isinstance(error, commands.CommandNotFound):
        mbed = discord.Embed(title="ჰა?!",
                             description="```ნუ ხაკერობ ბიძი!```",
                             colour=discord.Colour.dark_red())
        await ctx.send(embed=mbed)

    if isinstance(error, commands.MissingPermissions):
        mbed = discord.Embed(title="დაფიქსირდა შემლოცველის შეცდომა",
                             description="```ჯერ მზად არ ხარ ამ შელოცვისთვის შვილო ჩემო.```",
                             colour=discord.Colour.dark_red())
        await ctx.send(embed=mbed)


@client.command()
@commands.check(is_it_me)

async def example(ctx) -> None:
    await ctx.send(f"Hi, {ctx.author}!")


for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):  # თუ პითონის ფაილია
        client.load_extension(f"cogs.{filename[:-3]}")  # :-3 რადგან პითონის ფაილის სახელია საჭირო გაფართოების გარეშე

# client.run(os.getenv(os.getenv("TOKEN")))
client.run("ODM3MzUzNDk2OTE4NDkxMjI3.YIrUNg.tDU6FaqA-CG3DZt_ePaNLpNjniQ")
