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


@bot.command()
async def salut(ctx):
    await ctx.send("salut")


@bot.command()
@commands.has_permissions(manage_nicknames=True)
async def nume(ctx, member: discord.Member, *args):
    formatted_nickname = " ".join(args)
    await member.edit(nick=formatted_nickname)
    await ctx.send(f"gata acum {member.name} are numele {formatted_nickname}")


@bot.command()
async def injura(ctx, member: discord.Member):
    await ctx.send(
        f"{member.mention} {utils.swear_sentence()} {utils.swear_sentence()} {utils.swear_sentence()}"
    )


@bot.command()
async def complimenteaza(ctx, member: discord.Member):
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
    quotes = json.load(open("quotes.json"))
    quotes.append(quote)

    with open("quotes.json", "w") as file:
        json.dump(quotes, file, indent=4)

    await ctx.send("gata am memorat")


@bot.command()
async def vorbeste(ctx):
    quotes = json.load(open("quotes.json"))
    random_quote = random.choice(quotes)

    await ctx.send(random_quote)


@bot.command()
async def ajutor(ctx):
    await ctx.send(
        ""
        + "\nComenzi pentru Membrii:"
        + "\n1. Ca sa injuri pe cineva scrie `alex injura @membru`"
        + "\n2. Ca sa complimentezi pe cineva scrie `alex complimenteaza @membru`"
        + "\n3. Ca sa spun ceva scrie `alex spune propozitie`"
        + "\n4. Ca sa spun o propozitie memorata scrie `alex vorbeste`"
        + "\n"
        + "\nComenzi pentru Admini:"
        + "\n1. Ca sa setezi nume la alte persoane scrie `alex nume @membru nume nou`"
        + "\n2. Ca sa memorez ceva scrie `alex memoreaza propozitie`"
    )


@bot.event
async def on_member_remove(member: discord.Member):
    message = f"{member.mention} {utils.swear_sentence()} {utils.swear_sentence()} {utils.swear_sentence()}"

    channel = discord.utils.get(member.guild.channels, name="📩»welcome")
    if channel:
        await channel.send(message)


@bot.event
async def on_member_join(member: discord.Member):
    culori_channel_id = 1330600421680746688
    chat_channel_id = 1329881783910793321
    message = f"Bine ai venit {member.mention}! Iti poti alege o culoare in <#{culori_channel_id}> si trimite un mesaj pe <#{chat_channel_id}> sa vorbim."

    channel = discord.utils.get(member.guild.channels, name="📩»welcome")
    if channel:
        await channel.send(message)


bot.run(token)
