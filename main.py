import discord
from discord.ext import commands
import json
import utils as utils
import random

env = json.load(open(".env.json"))
token = env["TOKEN"]

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="alex ", intents=intents)

quotes_path = "quotes.json"

utils.init_file(quotes_path, "[]")


@bot.command()
async def salut(ctx: commands.Context):
    await ctx.send("salut")


@bot.command()
@commands.has_permissions(manage_nicknames=True)
async def nume(ctx, member: discord.Member, *args):
    formatted_nickname = " ".join(args)
    await member.edit(nick=formatted_nickname)
    await ctx.send(f"gata acum {member.name} are numele {formatted_nickname}")


@bot.command()
async def injura(ctx: commands.Context, member: discord.Member):
    await ctx.send(
        f"{member.mention} {utils.swear_sentence()} {utils.swear_sentence()} {utils.swear_sentence()}"
    )


@bot.command()
async def complimenteaza(ctx: commands.Context, member: discord.Member):
    await ctx.send(
        f"{member.mention} {utils.compliment_sentence()} {utils.compliment_sentence()} {utils.compliment_sentence()}"
    )


@bot.command()
async def spune(ctx, *args):
    message = " ".join(args)
    await ctx.send(message)


@bot.command()
@commands.has_permissions(administrator=True)
async def memoreaza(ctx, *args):
    quote = " ".join(args)
    quotes = json.load(open(quotes_path))
    quotes.append(quote)

    with open(quotes_path, "w") as file:
        json.dump(quotes, file, indent=4)

    await ctx.send("gata am memorat")


@bot.command()
@commands.has_permissions(administrator=True)
async def uita(ctx, *args):
    quote = " ".join(args)
    quotes = json.load(open(quotes_path))
    if quote in quotes:
        quotes.remove(quote)
        with open(quotes_path, "w") as file:
            json.dump(quotes, file, indent=4)
        await ctx.send("gata am uitat")
    else:
        await ctx.send("nici macar n-am memorat asta")


@bot.command()
async def vorbeste(ctx: commands.Context):
    quotes = json.load(open(quotes_path))
    if len(quotes) == 0:
        await ctx.send("n-am memorat nimic")
        return

    random_quote = random.choice(quotes)

    await ctx.send(random_quote)


@bot.command()
async def memorie(ctx: commands.Context):
    quotes = json.load(open(quotes_path))
    if len(quotes) == 0:
        await ctx.send("n-am memorat nimic")
        return

    str_quotes = "\n".join(quotes)
    await ctx.send(str_quotes)


@bot.command()
async def ajutor(ctx: commands.Context):
    await ctx.send(
        ""
        + "\nComenzi pentru Membrii:"
        + "\n1. Ca sa injuri pe cineva scrie `alex injura @membru`"
        + "\n2. Ca sa complimentezi pe cineva scrie `alex complimenteaza @membru`"
        + "\n3. Ca sa spun ceva scrie `alex spune propozitie`"
        + "\n4. Ca sa spun o propozitie memorata scrie `alex vorbeste`"
        + "\n5. Ca sa dai ca zarul scrie `alex barbut`"
        + "\n6. Ca sa vezi ce am memorat scrie `alex memorie`"
        + "\n"
        + "\nComenzi pentru Admini:"
        + "\n1. Ca sa setezi nume la alte persoane scrie `alex nume @membru nume nou`"
        + "\n2. Ca sa memorez ceva scrie `alex memoreaza propozitie`"
        + "\n3. Ca sa uit ceva memorat scrie `alex uita propozitie`"
    )


@bot.command()
async def barbut(ctx: commands.Context):
    choices = [1, 2, 3, 4, 5, 6]
    dice1 = random.choice(choices)
    dice2 = random.choice(choices)

    await ctx.send(f"{ctx.author.mention} ai dat {dice1} {dice2}")


@bot.event
async def on_member_remove(member: discord.Member):
    message = f"{member.mention} {utils.swear_sentence()} {utils.swear_sentence()} {utils.swear_sentence()}"
    embed = discord.Embed(
        title=f"{member.name} a iesit",
        description=message,
        color=discord.Color.red(),
    )

    channel = discord.utils.get(member.guild.channels, name="📩»welcome")
    if channel:
        await channel.send(embed=embed)


@bot.event
async def on_member_join(member: discord.Member):
    culori_channel_id = 1330600421680746688
    chat_channel_id = 1329881783910793321
    message = f"Bine ai venit {member.mention}! Iti poti alege o culoare in <#{culori_channel_id}> si trimite un mesaj pe <#{chat_channel_id}> sa vorbim."

    embed = discord.Embed(
        title=f"{member.name} s-a alaturat",
        description=message,
        color=discord.Color.green(),
    )

    channel = discord.utils.get(member.guild.channels, name="📩»welcome")
    if channel:
        await channel.send(member.mention)
        await channel.send(embed=embed)


@bot.event
async def on_message(message: discord.Message):
    if message.author == bot.user:
        return

    lower_msg = message.content.lower()
    if "alex" not in lower_msg:
        return

    thanks = ["mersi", "multumesc"]

    if any(word in lower_msg for word in thanks):  # If someone says "hello", respond
        await message.channel.send("cu placere")

    await bot.process_commands(message)  # Ensure commands still work


bot.run(token)
