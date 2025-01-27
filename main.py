import discord
from discord.ext import commands
import random
import json

env = json.load(open(".env.json"))
token = env["TOKEN"]

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="alex ", intents=intents)


def swear_sentence():
    start = ["ba", "sa-mi bag pula in", "futu-te in"]

    mid0 = [
        "retardatule",
        "handicapatule",
        "prostule",
        "muist imputit",
        "jegos infect",
        "pula bleaga",
        "muistu pulii",
        "retardat infect",
        "jegos cu sperma la gura",
        "sloboz de cal",
        "cacat de om",
    ]

    mid1 = [
        "fata ta de retardat libidinos",
        "nasu ala stramb de handicapat",
        "ochii tai blegi",
        "nasu ala de raton imputit",
        "fata aia de bulangiu fara viata",
        "ma-ta aia stramba fara dinti",
        "ma-ta aia stramba",
        "familia ma-tii",
        "toata rasa ta de retardati",
        "moaca aia de prost care sugi pula",
        "gaozu tau infect",
        "mutra ta de prost",
        "mutra aia de retardat",
        "gatu ma-tii pana ii iese sperma pe ochi",
        "gaozu ma-tii",
        "gura ta pana iti cad dintii",
    ]

    mid2 = [
        "gatu ala de gazela",
        "gura aia scarboasa",
        "nasu ala stramb",
        "gaozu ala infect",
        "mutra aia de balena",
        "gura de retardat",
        "mormantu ma-tii",
        "gatu ala de sobolan",
        "ochii aia beliti",
    ]

    mid = [mid0, mid1, mid2]

    end = [
        "fute-m-as pe rasa ma-tii",
        "sa-ti bag toata pula pe gat",
        "te fut in gura, iti dau muie, si mi-o si sugi",
        "baga-ti-as pula pe nas",
        "handicapat infect",
        "sa-mi bag pula in rasa ma-tii",
        "retardat handicapat",
        "manca-mi-ai coaiele",
        "baga-te-as in mormant",
        "sa ma fut in gatu ma-tii",
        "sa-mi bag pula in ce ai mai sfant",
        "sa iti iau toata rasa in pula",
        "sa iti trag chilotii pe ochi",
        "baga-mi-as pula in gatu tau de orfan",
        "manca-mi-ai toata pula libidinosule",
        "fute-m-as pe toata familia ta",
    ]

    result = random.choice([0, 1, 2])
    result_mid = random.choice(mid[result])
    result_end = random.choice(end)
    x = f"{start[result]} {result_mid} {result_end}"

    return x


print(swear_sentence())


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
        f"{member.name} {swear_sentence()} {swear_sentence()} {swear_sentence()}"
    )


@bot.command()
async def ajutor(ctx):
    await ctx.send(
        '1. Ca sa setezi nume la alte persoane scrie "alex nume @membru nume-nou-cu-liniute"'
    )
    await ctx.send('2. Ca sa injuri pe cineva scrie "alex injura @membru"')


bot.run(token)
