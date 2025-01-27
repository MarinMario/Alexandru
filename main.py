import discord
from discord.ext import commands
import json
import utils

env = json.load(open(".env.json"))
token = env["TOKEN"]

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="alex ", intents=intents)


@bot.command()
async def salut(ctx):
    await ctx.send("salut")


@bot.command()
@commands.has_permissions(manage_nicknames=True)
async def nume(ctx, member: discord.Member, new_nickname: str):
    formatted_nickname = new_nickname.replace("-", " ")
    await member.edit(nick=formatted_nickname)
    await ctx.send(f"gata acum {member.name} are numele {formatted_nickname}")


@bot.command()
async def injura(ctx, member: discord.Member):
    await ctx.send(
        f"{member.name} {utils.swear_sentence()} {utils.swear_sentence()} {utils.swear_sentence()}"
    )


@bot.command()
async def compliment(ctx, member: discord.Member):
    await ctx.send(
        f"{member.name} {utils.compliment_sentence()} {utils.compliment_sentence()} {utils.compliment_sentence()}"
    )


@bot.command()
async def ajutor(ctx):
    await ctx.send(
        "1. Ca sa setezi nume la alte persoane scrie `alex nume @membru nume-nou-cu-liniute`"
        + "\n2. Ca sa injuri pe cineva scrie `alex injura @membru`"
        + "\n3. Ca sa complimentezi pe cineva scrie `alex compliment @membru`"
    )


bot.run(token)
